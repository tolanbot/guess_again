Use this as your updated README.md. It matches the current code, including per-difficulty high scores, command aliases, the current scoring behavior, and the current Mad Max validation rules. 

# Guess Again

A command-line number guessing game written in Python.

Players can start a game from a main menu, choose a difficulty level, and try to guess a randomly generated number within a limited number of attempts. The game also supports a custom "Mad Max" mode where the player sets a custom maximum number and maximum number of tries.

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
* Main menu shortcuts and aliases:

  * Start: `1`, `start`, `s`
  * Choose Difficulty: `2`, `diff`, `d`
  * Current Stats: `3`, `stats`, `st`
  * Quit: `4`, `quit`, `q`
* Difficulty selection shortcuts:

  * Easy: `1`, `easy`, `e`
  * Medium: `2`, `medium`, `md`
  * Hard: `3`, `hard`, `h`
  * Mad Max: `4`, `mad max`, `madmax`, `mm`
* Tracks game statistics:

  * games played
  * games won
  * games lost
  * games abandoned
  * high scores for each difficulty
* Prevents duplicate guesses
* Validates menu choices and numeric input
* Displays remaining guesses after each valid guess
* Calculates a score when the player wins
* Updates and announces a new high score for the current difficulty when earned
* Uses explicit game results (`WON`, `LOST`, `QUIT`) to track outcomes cleanly

## Difficulty Levels

* Easy: numbers from 1 to 10, 4 tries
* Medium: numbers from 1 to 50, 5 tries
* Hard: numbers from 1 to 100, 7 tries
* Mad Max: custom maximum number and custom number of tries chosen by the user

Mad Max currently requires:

* max number must be greater than 0
* max tries must be greater than 0
* max tries cannot be greater than max number

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

If you quit during a round, the round ends immediately and is counted as an abandoned game.

## In-Game Commands

During a game, you can type:

* `stats` or `st` — display the current game statistics
* `quit` or `q` — abandon the current round

## Main Menu Example

```
***** GUESS AGAIN: THE GAME *****
Main Menu:
    1. Start
    2. Choose Difficulty (Current Difficulty: Easy)
    3. Current Stats
    4. Quit
```

## Difficulty Selection Example

```
Choose Difficulty:
    1. Easy   (1-10, 4 tries)
    2. Medium (1-50, 5 tries)
    3. Hard   (1-100, 7 tries)
    4. Mad Max (Custom Game Config)
```

## Scoring

When you win a round, the game calculates a score based on:

* the size of the number range
* the number of allowed tries
* how many guesses you had remaining

Higher difficulty settings and winning with more guesses remaining lead to higher scores.

The current score formula is based on:

* `range_size = max_num - min_num + 1`
* `(range_size / max_tries) * (remaining_guesses + 1) * 10`

The result is converted to an integer before being stored or displayed.

## Current Statistics Tracked

* Games Played
* Games Won
* Games Lost
* Games Abandoned
* High Score for Easy
* High Score for Medium
* High Score for Hard
* High Score for Mad Max

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
* helper-function decomposition
* score calculation
* per-difficulty stat tracking
* result-based state handling
* basic command-line program organization

## Future Improvements

* Save stats between program runs
* Add a reset stats option
* Add automated tests
* Add a round summary screen after each completed game
* Add total score accumulation across rounds
* Add win-rate tracking by difficulty
* Add support for a custom minimum number instead of always starting at 1
* Improve stats screen formatting and alignment
* Add a hint system or optional difficulty modifiers
* Refine the score formula further if you want a different difficulty curve

## Author

Chris Tolan
