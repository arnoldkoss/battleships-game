# Battleships

Welcome to Battleships, a classic naval strategy game brought to life in Python! This console-based game allows you to engage in a thrilling battle against the computer.  It is a turn-based guessing game where you play against the computer and try to sink your enemies battleships before your own fleet is destroyed.


By developing the game on Code Institutes Python Template, it can be run in a web browser, as opposed to only being able to run on a CLI or Command Line Interface.

![responsive image](documentation/amIresponsive.png)

# Table of Contents

## How to play
Battleships is a board game based on the classic pen-and-paper version. The objective is to sink all your opponent's ships before your own ships are destroyed. In this version of the game, players start by entering their names, and two boards are randomly generated. The user can see their own ships marked by an '@' sign but cannot see the computer's ships. Guesses that aren't hits are marked with a '-' sign, while hits are marked with an 'X'. The user and the computer take turns making guesses and attempting to sink each other's battleships. The winner is the first to successfully sink the opponent's battleships.

## Features

In this section I will provide an overview of the features included in Battleships. The game is built on the Code Institute Python Template, which provides the HTML and CSS code necessary to play the game in a browser. As that code is not written by the developer, its features will not be mentioned.

### Welcome Message

- The welcome message presented as ASCII art and a small welcome message.
- The user is then prompted to enter a name, which is validated to be at least one character . If left blank, an error message will print, asking for a valid input.

![welcome message image](documentation/welcomeMessage.png)

- Invalid input (if the user inserts non-alphabetic characters)

![invalid input image](documentation/invalidInput.png)

- Invalid input (if the user left the input blank)

![invalid input image 2](documentation/invalidInput2.png)


### Game Boards

- Random board generation.
  - Ships are randomly generated on the users board as well for the computer.
  - The user can not see the placement of the computer's ships.
  - When the name imput  is set, the game boards are printed out and populated with a number of 4 ships on each board.
  - Numbers are printed along the rows and columns to help the user easier find the coordinates.

  ![the boards image](documentation/theBoards.png)

- Play against the computer.
- Accepts user input.

![playing the game image](documentation/userInput.png)

- Input validation and error-checking
  - Using same coordinates
  ![same coordinates input image](documentation/sameCoordinates.png)
  - Entering coordinates outside the size of the grid or using non-numerical coordinates.
  ![invalid coordinates image](documentation/invalidCoordinates.png)

 - Data maintained in class instances.

 ### Future Futures

 - Allow the user to select the board size and the number of ships.
 - Allow the user to place the ships by himself.
 - Add different sizes for the ships.
 - Add a score feature.

 ## Data model

 - My game utilizes a Board class to create both boards, in which the input parameters, such as size and number of ships are stored. It also takes in all guesses made on each board, the location of the deployed ships, the name and type of player the board belongs to (user or computer).
 - The class then builds the boards with the correct parameters and prints them out. After each turn the boards are updated with the stored guesses and printed out.
 - Aside from the Board class there are helper functions that are called as the game progresses, such as asking for and validating the coordinates guessed and generating random integers to use when adding the ships.


 ## Testing

 - The python code is free of errors and written correctly, validation through the PEP8 online validator was performed with no errors or warnings raised.

 - Tested in my local terminal and the Code Institute Heroku terminal.
 