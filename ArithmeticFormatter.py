# Define a function named arithmetic_arranger with two parameters problems and show_answer = False as default
def arithmetic_arranger(problems, show_answer=False):
    # Check if the number of problems is greater than 5, if so, return an error message
    if len(problems) > 5:
        return "Error: Too many problems."

    # Create a dictionary to store different lines of arranged problems
    arranged_problems = {
        "first_line": "",    # Store the first line of each problem for example operand1
        "second_line": "",   # Store the second line of each problem for example operator(+,-) + operand2
        "dash_line": "",     # Store the line containing dashes for formatting i.e. -----
        "answer_line": ""    # Store the line containing answers (if show_answer is True) i.e. result or answer
    }

    # Loop through each problem in the list
    for problem in problems:
        # Split the problem into its components: operand1, operator, and operand2
        operand1, operator, operand2 = problem.split()

        # Check if the operator is either '+' or '-'; if not, return an error message
        if operator not in ["+", "-"]:
            return "Error: Operator must be '+' or '-'."

        # Check if both operands contain only digits; if not, return an error message
        if not operand1.isdigit() or not operand2.isdigit():
            return "Error: Numbers must only contain digits."

        # Check if the length of operands is greater than 4 digits; if so, return an error message
        if len(operand1) > 4 or len(operand2) > 4:
            return "Error: Numbers cannot be more than four digits."

        # Calculate the width needed for formatting based on the length of the operands
        width = max(len(operand1), len(operand2)) + 2

        # Build the first line by right-aligning operand1 and appending it with four spacing
        arranged_problems["first_line"] += operand1.rjust(width) + "    "
        
        # Build the second line by adding the operator operand2 right-aligned, and four spacing
        arranged_problems["second_line"] += operator + " " + operand2.rjust(width - 2) + "    "
        
        # Build the dash line by adding dashes to match the width of the operands
        arranged_problems["dash_line"] += "-" * width + "    "

        # If show_answer is True calculate the answer and build the answer line
        if show_answer:
            if operator == "+":
                answer = str(int(operand1) + int(operand2))
            else:
                answer = str(int(operand1) - int(operand2))
            arranged_problems["answer_line"] += answer.rjust(width) + "    "

    # Concatenate the first line, second line, and dash line to form the arranged output
    arranged_output = arranged_problems["first_line"].rstrip() + "\n"
    arranged_output += arranged_problems["second_line"].rstrip() + "\n"
    arranged_output += arranged_problems["dash_line"].rstrip()
    
    # If show_answer is True add the answer line to the arranged output
    if show_answer:
        arranged_output += "\n" + arranged_problems["answer_line"].rstrip()

    # Return the arranged output
    return arranged_output
