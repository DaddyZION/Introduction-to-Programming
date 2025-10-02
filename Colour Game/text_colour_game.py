# Import the random module - this gives us tools to generate random numbers
import random

# A dictionary stores pairs of keys and values
# Here we map color names to special codes that make text appear colored
colors = {
    'red': '\033[91m',      # Code to make text red
    'green': '\033[92m',    # Code to make text green
    'blue': '\033[94m',     # Code to make text blue
    'yellow': '\033[93m',   # Code to make text yellow
    'purple': '\033[95m'    # Code to make text purple
}
# This code resets text back to normal color
normal = '\033[0m'

# A list contains multiple items in order
# These are the 5 words we'll always show to the player
words = ['RED', 'BLUE', 'GREEN', 'YELLOW', 'PURPLE']

# Print instructions to the screen
print("Color Game! Find the RED word. Type 'quit' to exit.")
print()  # Print a blank line for spacing

# A while loop repeats code forever (until we tell it to stop)
while True:
    # Pick a random number from 0 to 4 to decide which word will be red
    # random.randint(0, 4) gives us 0, 1, 2, 3, or 4
    red_word = random.randint(0, 4)
    
    # A for loop repeats code a specific number of times
    # range(5) creates numbers 0, 1, 2, 3, 4
    # So this loop runs 5 times, once for each word
    for i in range(5):
        # Check if this is the word that should be red
        if i == red_word:
            # f-strings let us insert variables into text using {}
            # This prints the word in red color
            print(f"{colors['red']}{words[i]}{normal}", end="  ")
        else:
            # This word should be a different color
            # Create a list of colors (excluding red)
            other_colors = ['green', 'blue', 'yellow', 'purple']
            # random.choice() picks one random item from a list
            color = random.choice(other_colors)
            # Print the word in the randomly chosen color
            print(f"{colors[color]}{words[i]}{normal}", end="  ")
    
    # Move to a new line after showing all words
    print()
    # Ask the user for their answer and store it in a variable
    answer = input("Which word is red? ")
    
    # Check if the user wants to quit the game
    # .lower() converts text to lowercase so 'QUIT' becomes 'quit'
    if answer.lower() == 'quit':
        break  # Exit the while loop and end the program
        
    # Check if the user's answer is correct
    # .upper() converts text to uppercase so 'red' becomes 'RED'
    # words[red_word] gets the word at position red_word from our list
    if answer.upper() == words[red_word]:
        print("Correct! 🎉")
    else:
        # If wrong, tell them the correct answer
        print(f"Wrong! It was {words[red_word]}")
    
    # Print a blank line before the next round
    print()