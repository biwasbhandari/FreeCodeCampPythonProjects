import copy  # Importing the copy module to create deep copies of objects
import random  # Importing the random module for random selection

class Hat:
    def __init__(self, **kwargs):
        self.contents = []  # Initialize an empty list to store the contents of the hat
        # Loop through the keyword arguments (color: count) and add balls to the contents list
        for color, count in kwargs.items():
            self.contents.extend([color] * count)
    
    def draw(self, num_balls):
        drawn_balls = []  # Initialize an empty list to store the drawn balls
        if num_balls >= len(self.contents):
            return self.contents  # If the number of balls to draw exceeds available quantity, return all balls
        # Randomly draw balls from the hat without replacement
        for _ in range(num_balls):
            ball = random.choice(self.contents)  # Randomly select a ball from the contents list
            self.contents.remove(ball)  # Remove the selected ball from the contents list
            drawn_balls.append(ball)  # Add the selected ball to the drawn balls list
        return drawn_balls  # Return the list of drawn balls

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    successful_experiments = 0  # Initialize a counter for successful experiments
    for _ in range(num_experiments):
        hat_copy = copy.deepcopy(hat)  # Create a deep copy of the original hat
        drawn_balls = hat_copy.draw(num_balls_drawn)  # Draw a specified number of balls from the hat
        drawn_dict = {color: drawn_balls.count(color) for color in set(drawn_balls)}  # Count the occurrence of each color in the drawn balls
        success = True  # Initialize a variable to track if the experiment is successful
        # Check if the drawn balls contain the expected number of each color
        for color, count in expected_balls.items():
            if color not in drawn_dict or drawn_dict[color] < count:
                success = False  # If any expected color is not found or the count is less than expected, the experiment fails
                break
        if success:
            successful_experiments += 1  # Increment the counter for successful experiments
    return successful_experiments / num_experiments  # Return the probability of successful experiments
