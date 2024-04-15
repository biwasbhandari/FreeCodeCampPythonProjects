class Category:
    def __init__(self, name):
        # iniitalizing catagory object
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=""):
        # Add a deposit to the ledger
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=""):
        # Add a withdrawal to the ledger 
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        else:
            return False

    def get_balance(self):
        # Calculate the current balance 
        return sum(item["amount"] for item in self.ledger)

    def transfer(self, amount, category):
        # Transfer funds from this category to another category
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {category.name}")
            category.deposit(amount, f"Transfer from {self.name}")
            return True
        else:
            return False

    def check_funds(self, amount):
        # Check if there are enough funds for a given amount
        return amount <= self.get_balance()

    def __str__(self):
        # Create a string representation of the Category object for printing
        title = f"{self.name:*^30}\n"  # Center the category name 
        items = ""
        total = 0
        # Add each ledger item to the string representation
        for item in self.ledger:
            items += f"{item['description'][:23]:23}{item['amount']:>7.2f}\n"  # Format description and amount
            total += item["amount"]  # Calculate the total amount
        output = title + items + "Total: " + str(total)  # Combine title, items, and total
        return output


def create_spend_chart(categories):
    # Function to create a spend chart based on a list of categories
    category_names = []
    spent = []
    spent_percentages = []

    # Calculate total spent for each category and store category names
    for category in categories:
        total_spent = 0
        for item in category.ledger:
            if item["amount"] < 0:
                total_spent -= item["amount"]
        spent.append(round(total_spent, 2))
        category_names.append(category.name)

    # Calculate spent percentages for each category
    for amount in spent:
        spent_percentages.append(round(amount / sum(spent), 2) * 100)

    graph = "Percentage spent by category\n"
    labels = range(100, -10, -10)

    # Generate the graph based on spent percentages
    for label in labels:
        graph += str(label).rjust(3) + "| "
        for percent in spent_percentages:
            if percent >= label:
                graph += "o  "
            else:
                graph += "   "
        graph += "\n"

    graph += "    ----------\n     "

    # Add category names below the graph
    longest_name_length = max([len(name) for name in category_names])
    for i in range(longest_name_length):
        for name in category_names:
            if len(name) > i:
                graph += name[i] + "  "
            else:
                graph += "   "
        if i < longest_name_length - 1:
            graph += "\n     "

    return graph

# Example usage
food = Category("Food")
food.deposit(1000, "deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant and more food for dessert")
clothing = Category("Clothing")
food.transfer(50, clothing)
print(food)

# Example of create_spend_chart
categories = [food, clothing]
print(create_spend_chart(categories))
