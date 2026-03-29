# Guess Again

A command-line number guessing game written in Python.

Players can start a game from a main menu, choose a difficulty level, and try to guess a randomly generated number within a limited number of attempts. The game also supports a custom "Mad Max" mode where the player sets the maximum number and maximum number of tries.

## Features

* Main menu interface
* Four difficulty options:

  * Easy
  * Medium
  * Hard
  * Mad Max (custom game configuration)
* In-game commands:

  * `stats`
  * `quit`
* Tracks game statistics:

  * games played
  * games won
  * games lost
  * games abandoned
* Prevents duplicate guesses
* Validates menu choices and numeric input
* Displays remaining guesses after each valid guess
* Handles singular/plural guess wording

## Difficulty Levels

* Easy: numbers from 1 to 10, 5 tries
* Medium: numbers from 1 to 20, 5 tries
* Hard: numbers from 1 to 50, 7 tries
* Mad Max: custom maximum number and custom number of tries chosen by the user

## Requirements

* Python 3.10 or newer

## How to Run

Clone the repository:

```
git clone https://github.com/tolanbot/guess_again.git
cd guess_again
```

Run the program:

```
python3 main.py
```

Replace `main.py` with your actual Python filename if it is different.

## How to Play

1. Run the program
2. Choose an option from the main menu:

   * Start
   * Choose Difficulty
   * Current Stats
   * Quit
3. If you choose Start, the game begins using the currently selected configuration
4. Enter guesses until you:

   * guess the number correctly
   * run out of tries
   * type `quit`

## In-Game Commands

During a game, you can type:

* `stats` — display the current game statistics
* `quit` — abandon the current round

## Main Menu Example

```
***** GUESS AGAIN: THE GAME *****
Main Menu:
    1. Start
    2. Choose Difficulty
    3. Current Stats
    4. Quit
```

## Difficulty Selection Example

```
Choose Difficulty:
    1. Easy   (1-10, 5 tries)
    2. Medium (1-20, 5 tries)
    3. Hard   (1-50, 7 tries)
    4. MadMax (Custom Game Config)
```

## What This Project Practices

This project was built to practice:

* functions
* loops
* conditionals
* input validation
* sets
* dataclasses
* enums
* mapping enum values to runtime configuration
* basic command-line program organization

## Current Statistics Tracked

* Games Played
* Games Won
* Games Lost
* Games Abandoned

## Future Improvements

* Track and display a true high score
* Save stats between program runs
* Add a reset stats option
* Add automated tests
* Improve custom configuration validation further
* Refactor parts of the menu and game flow into smaller helper functions

## Author

Chris Tolan
