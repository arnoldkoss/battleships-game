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
welcome_message()    

def input_name():
    """
    Ask the user for a name and stores it
    in a global variable to be used in the game.
    """
    global user_name
    user_name = input("Please enter your name: \n")
input_name()        