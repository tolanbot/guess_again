# Guess Again

A command-line number guessing game written in Python.

Players can choose a difficulty level, guess a randomly generated number, view stats during the game, and quit a round at any time.

## Features

- Main menu
- Three difficulty levels
- Input validation
- Duplicate guess detection
- In-game commands:
  - `stats`
  - `quit`
- Game statistics tracking:
  - games played
  - games won
  - games lost
  - games abandoned

## Difficulty Levels

- Easy: 1-10, 5 tries
- Medium: 1-20, 5 tries
- Hard: 1-50, 7 tries

## Requirements

- Python 3.10 or newer

## How to Run

Clone the repository:

```bash
git clone https://github.com/tolanbot/guess_again.git
cd guess_again
```

Run the program:

```bash
python3 main.py
```

Replace `main.py` with your actual Python filename if it is different.

## How to Play

1. Start the program
2. Choose one of the menu options:
   - Start
   - Choose Difficulty
   - Current Stats
   - Quit
3. Enter a guess within the allowed range
4. Keep guessing until you:
   - guess the number
   - run out of tries
   - type `quit`

## In-Game Commands

- `stats` — show current game statistics
- `quit` — abandon the current round

## Example

```text
***** GUESS AGAIN: THE GAME *****

1. Start
2. Choose Difficulty
3. Current Stats
4. Quit
```

## What This Project Practices

This project was built to practice:

- functions
- loops
- conditionals
- input validation
- sets
- dataclasses
- enums
- basic program organization

## Future Improvements

- Save stats between sessions
- Add a high score system
- Add a hint system
- Add unit tests
- Improve menu formatting

## Author

Chris Tolan
