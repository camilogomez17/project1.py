# Rock, Paper, Scissors CLI

A terminal-based Rock, Paper, Scissors game written in Python. Play rounds
against the computer, review your game history, correct or delete a saved
record, and view statistics calculated from the history.

## Requirements

- Python 3
- No third-party packages are required.

## Run the app

From the repository root, run:

```bash
python3 src/main.py
```

## Menu

1. **Play a game** — choose rock, paper, or scissors and play against a
   computer choice.
2. **View game history** — see each recorded round, its timestamp, both
   choices, and the result.
3. **Edit or delete a game** — correct the choices in a saved record (the
   result is recalculated) or delete the record after confirmation.
4. **View statistics** — see wins, losses, ties, and total games.
5. **Quit** — exit the application.

## Example session

```text
=== Rock, Paper, Scissors ===
1. Play a game
2. View game history
3. Edit or delete a game
4. View statistics
5. Quit
Select an option: 1
Choose rock, paper, or scissors: rock
You chose: rock
Computer chose: scissors
You win!
Game saved to your history.
```

Game records are stored in memory while the program is running. They are
cleared when you quit; this project does not write data to a file or database.
