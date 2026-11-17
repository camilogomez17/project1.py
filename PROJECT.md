# Project 1: Rock, Paper, Scissors CLI

Build a command-line Rock, Paper, Scissors game in Python using the fundamentals from Mod 1. The application runs in the terminal, accepts typed input, plays rounds against a computer opponent, tracks results, and keeps returning to the main menu until the user exits.

This project-specific brief replaces the generic task-manager/list-of-dictionaries example in the starter template. Follow the Rock, Paper, Scissors requirements below for this project.

Assignment reference: [Marcy Labs — Project: CLI Application](https://marcylabschool.gitbook.io/swe/computational-thinking-and-responsible-use-of-ai/mod-1-python-fundamentals/project)

## What You Are Building

A terminal game with three menu options:

1. **Play Round** — The user enters rock, paper, or scissors. Input must be case-insensitive. The computer randomly chooses one of the three moves. The program displays both choices and announces whether the round is a win, loss, or tie.
2. **View Stats** — Display the player's wins, losses, ties, total games, and win rate. The win rate should be rounded to a readable number of decimal places.
3. **Exit** — End the application and display the final statistics.

The menu should continue to appear until the user chooses Exit. During a round, the user should also be able to enter `quit` to return to the main menu.

## Requirements

### Game behavior

- [ ] Display a menu with **Play Round**, **View Stats**, and **Exit**.
- [ ] Accept `rock`, `paper`, or `scissors` as user input.
- [ ] Accept input regardless of capitalization and ignore accidental surrounding whitespace.
- [ ] Randomly select one of all three moves for the computer.
- [ ] Determine the outcome using the standard Rock, Paper, Scissors rules.
- [ ] Display the player's move, the computer's move, and the round result.
- [ ] Allow the player to leave a round and return to the menu.
- [ ] Keep the application running until the player selects Exit.
- [ ] Handle invalid menu choices and invalid moves without crashing.

### Statistics

Store game statistics in a dictionary with these keys:

- `wins`
- `losses`
- `ties`

Update the appropriate value after every completed round. The statistics screen must display:

- Wins
- Losses
- Ties
- Total games played
- Win rate, rounded to a readable precision

When the player exits, display the final statistics.

### Code organization and Python fundamentals

- [ ] Use several functions, with each function responsible for one clear job.
- [ ] Use conditionals to handle menu choices and round outcomes.
- [ ] Use a `while` loop to keep the application running.
- [ ] Use string methods to normalize and validate input.
- [ ] Use a dictionary to represent game data and/or map move names to numeric values.
- [ ] Split the application across at least **three modules** and use imports.
- [ ] Include an `if __name__ == "__main__":` guard in the entry-point module.
- [ ] Keep the code in `src/`.
- [ ] Add at least four tests for the data layer.
- [ ] Include a `requirements.txt` file if the project uses external dependencies.
- [ ] Ensure `.venv` is included in `.gitignore`.

### Documentation and submission

- [ ] Replace the starter `README.md` with a description of this game, instructions for running it, and a usage example.
- [ ] Complete `REFLECTIONS.md`, explaining what was learned, what was difficult, and how the implementation works.
- [ ] Push the completed work to GitHub and submit it as instructed by the course.

## Current Project Structure

The project is being developed in the `development` branch.

```text
src/
├── main.py       # Application entry point
├── menu.py       # Main menu and navigation
├── game_data.py  # Statistics dictionary and statistics display
└── logic.py      # Rock, Paper, Scissors round logic
```

The intended responsibilities are:

- **`main.py`** starts the application and calls the menu.
- **`menu.py`** displays the three options, reads the menu choice, and routes the user to the correct action.
- **`game_data.py`** stores and displays the statistics.
- **`logic.py`** handles a round: reading the player's move, choosing the computer's move, determining the outcome, and updating the statistics.

## Learning Roadmap

Work through the project in small steps. Understand each concept before moving to the next one.

1. **Represent the moves.** Understand how a dictionary maps the strings `"rock"`, `"paper"`, and `"scissors"` to numeric values.
2. **Translate input into data.** The user types a string. The program validates that string and looks up its numeric representation before doing arithmetic.
3. **Determine the outcome.** Understand how the expression `(player - computer + 3) % 3` maps the two numeric moves to a result. With rock = 0, paper = 1, and scissors = 2, the results are 0 = tie, 1 = player wins, and 2 = computer wins.
4. **Manage state.** Understand how the statistics dictionary changes after each completed round and remains available while the application runs.
5. **Separate responsibilities.** Understand why the entry point, menu, game logic, and statistics are separated into modules and how imports connect them.
6. **Test the data layer.** Test the statistics behavior independently from terminal input and random computer choices.
7. **Polish the application.** Improve output, input validation, documentation, and the final user experience.

## Current Progress and Known Issues

The project already has an entry point, a menu loop, a statistics dictionary, and the beginning of the game logic.

The current implementation has two issues to resolve in `logic.py`:

- The computer choice currently uses `random.randint(1, 2)`. This can only select 1 or 2, so it never selects rock (0). The computer must be able to choose from all three move values.
- The outcome calculation refers to `user_digit`, but that variable has not been defined. The input is currently stored as `user_string`. The program needs to translate the validated string into its numeric value before applying the modulo expression.

The statistics dictionary exists, but completed rounds do not yet update it. The statistics screen currently prints the raw dictionary rather than calculating and displaying the total games and win rate.

The README and reflections still need to be completed.

## Tutor Mode

Use AI as a tutor while learning and implementing this project. The tutor should explain concepts, ask guiding questions, quiz understanding, and critique code. The student writes and understands the implementation.

Do not ask the tutor to provide the complete solution. Instead, ask focused questions such as:

- How does a dictionary lookup translate a move name into a number?
- Why must the input be converted before the modulo calculation?
- How can the three possible outcomes be tested?
- How should the game logic update the statistics dictionary?
- How can the round logic be tested without relying on random output?

The goal is to understand the reasoning behind the code, be able to explain each function and module, and build the application independently.

## Stretch Features

Only attempt these after the required game and statistics features work:

- Best-of-three or best-of-five matches
- ASCII art for the moves
- Win/loss streak tracking
- Saving and loading statistics with JSON
