# Rock, Paper, Scissors CLI

## Features

This project has a navigable menu, a playable rock, paper, scissors game, and game stats that can be checked. The technologies used are purely python, modular arithmetic, and basic algebra.

To install this program clone the repository.

Run with `python3 src/main.py`

# Example gameplay and statistics output:

`Welcome to the game!

Menu: 
1. Play rock, paper, scissors!
2. View Statistics.
3. Exit.
Please choose an option!

>1

Choose a move (rock, paper, or scissors).
'quit' to exit.

>rock

You chose rock
Computer chose paper
Computer wins!

Choose a move (rock, paper, or scissors).
'quit' to exit.

>quit

Menu: 
1. Play rock, paper, scissors!
2. View Statistics.
3. Exit.
Please choose an option!

>2

Total games:1

Wins:0
Ties:0
Losses:1
Win rate:0.0%`

# Project Structure

`main.py` welcomes the user and runs the project.

`menu.py` displays the menu, takes user input, and runs `logic.py` or `game_data.py`, as well as allowing the user to quit.

`logic.py` contains the rock, paper, scissors game. This is done via variables, lists, modular arithmetic, and printing to the terminal.

`game_data.py` creates the structure for the game data, and runs operations on it to display to the user their total games, wins, losses, ties, and win rate.