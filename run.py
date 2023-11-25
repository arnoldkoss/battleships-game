"""
Import random to generate random integers in game.
"""
from random import randint



def welcome_message():
    """
    Displays a greeting.
    Ascii art source:
    https://patorjk.com/software/taag/#p=display&f=Doom&t=Battleship
    """
    print("""
 _    _      _                          _ 
| |  | |    | |                        | |
| |  | | ___| | ___ ___  _ __ ___   ___| |
| |/\| |/ _ \ |/ __/ _ \| '_ ` _ \ / _ \ |
\  /\  /  __/ | (_| (_) | | | | | |  __/_|
 \/  \/ \___|_|\___\___/|_| |_| |_|\___(_)
    """)
    print("=" * 42 + "\n")
    print("Welcome to Battleship! \n")
    print("Board size: 6. Number of ships: 4 \n")
    print("Top left corner is row: 0, col: 0  \n")

welcome_message()

def validate_name_input(name):
    """Validate the user's name input."""
    if not name:
        print("Please enter a name.")
        return False
    elif not name.isalpha():
        print("Name can only contain alphabetic characters.")
        return False
    else:
        return True

def input_name():
    """
    Get the user's name and store it
    in a global variable to be used in the game.
    """
    global user_name
    while True:
        user_name = input("Please enter your name: \n")
        if validate_name_input(user_name):
            break
input_name() 
print(f"Welcome, {user_name}!") 