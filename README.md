# Battleships

Welcome to Battleships, a classic naval strategy game brought to life in Python! This console-based game allows you to engage in a thrilling battle against the computer.  It is a turn-based guessing game where you play against the computer and try to sink your enemies battleships before your own fleet is destroyed.


By developing the game on Code Institutes Python Template, it can be run in a web browser, as opposed to only being able to run on a CLI or Command Line Interface.

![responsive image](documentation/amIresponsive.png)

# Table of Contents

## How to play
Battleships is a board game based on the classic pen-and-paper version. The objective is to sink all your opponent's ships before your own ships are destroyed. In this version of the game, players start by entering their names, and two boards are randomly generated. The user can see their own ships marked by an '@' sign but cannot see the computer's ships. Guesses that aren't hits are marked with a '-' sign, while hits are marked with an 'X'. The user and the computer take turns making guesses and attempting to sink each other's battleships. The winner is the first to successfully sink the opponent's battleships.

## Features

In this section I will provide an overview of the features included in Battleships. The game is built on the Code Institute Python Template, which provides the HTML and CSS code necessary to play the game in a browser. As that code is not written by the developer, its features will not be mentioned.

### Welcome message

- The welcome message presented as ASCII art and a small welcome message.
- The user is then prompted to enter a name, which is validated to be at least one character . If left blank, an error message will print, asking for a valid input.

![welcome message image](documentation/welcomeMessage.png)