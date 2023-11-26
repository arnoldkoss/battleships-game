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


class Board:
    """
    Main class to create game boards. Sets board size,
    number of ships, username and type of board(user
    or computer). Stores guesses made and the location
    of the randomized ships.
    """
    def __init__(self, size, num_ships, name, board_type):
        self.size = size
        self.num_ships = num_ships
        self.name = name
        self.type = board_type  
        self.guesses = []
        self.ships = []
        self.board = [["." for x in range(size)] for y in range(size)]

    def print_board(self):
        """
        Prints the boards with rows and columns 
        """
        for row in self.board:
            print(" ".join(row))

    def guess(self, x, y):

        self.guesses.append((x, y))

        if (row, col) in self.ships:
            self.board[x][y] = "X"
            return "Hit"
        else:
            self.board[x][y] = "-"
            return "Miss"        
        
    

 