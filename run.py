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

    def print_board(self, other_board=None):
        """
        Prints the boards with rows and columns.
        """
        player_name = f"{self.name}'s" if self.type == "user" else "Computer"
        print(f"{player_name} gameboard{' ' * (2 * self.size - len(player_name) - len(' gameboard'))}", end="")
    
        if other_board is not None:
            print(f"   {other_board.name}'s gameboard")
            col_str = " ".join(map(str, range(self.size)))
            header = f"  {col_str}{' ' * (2 * self.size - len(col_str))}      {col_str}"
            print(header)

            for row, (user_row, comp_row) in enumerate(zip(self.board, other_board.board)):
                print(f"{row}|{'|'.join(user_row)}{' ' * (2 * self.size - len(user_row))}|  "
                    f"{row}|{'|'.join(comp_row)}")
        else:
            print("")
            col_numbers = " ".join(map(str, range(self.size)))
            print(f"  {col_numbers}")
            for row_number, row in enumerate(self.board):
                print(f"{row_number}|{'|'.join(row)}")

    def guess(self, x, y):
        """
        Checks whether the guess is a hit or miss and
        saves all guesses in guesses variable.
        Prints 'X' for hit and '-' for miss.
        """
        if not (0 <= x < self.size and 0 <= y < self.size):
            print("Invalid guess. Please enter valid row and column values.")
            return "Invalid Guess"

        if (x, y) in self.guesses:
            print("You've already guessed that!")
            return "Already Guessed"

        self.guesses.append((x, y))

        if (x, y) in self.ships:
            self.board[x][y] = "X"
            return "Hit"
        else:
            self.board[x][y] = "-"
            return "Miss"        
        
    

    def place_ship(self, x, y, type="computer"):
        """
        Places ships on the board with the help
        of randomized coordinates passed in from
        populate_board.
        """
        if len(self.ships) >= self.num_ships:
            pass
        else:
            self.ships.append((x, y))
            if self.type == "user":
                self.board[x][y] = "@"

    
    def populate_board(self):
        """
        Randomly place ships on the board.
        """
        for _ in range(self.num_ships):
            while True:
                row = randint(0, self.size - 1)
                col = randint(0, self.size - 1)
                if (row, col) not in self.ships:
                    self.place_ship(row, col)
                    break         

test_user_board = Board(6, 4, "Test User", "user")
test_user_board.populate_board()
test_user_board.print_board()

test_comp_board = Board(6, 4, "Test Computer", "computer")
test_comp_board.populate_board()
test_comp_board.print_board()         