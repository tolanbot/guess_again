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
* Main menu shortcuts:

  * `start`
  * `diff`
  * `stats`
  * `quit`
* Tracks game statistics:

  * games played
  * games won
  * games lost
  * games abandoned
  * current high score
* Prevents duplicate guesses
* Validates menu choices and numeric input
* Displays remaining guesses after each valid guess
* Calculates a score when the player wins
* Updates and announces a new high score when earned
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

* `stats` — display the current game statistics
* `quit` — abandon the current round

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
* Current High Score 

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
* simple score calculation
* result-based state handling
* basic command-line program organization 

## Future Improvements

* Save stats between program runs
* Add a reset stats option
* Add automated tests
* Refactor `play_game()` further into smaller helper functions
* Add richer score tracking, such as per-round score history
* Add difficulty-specific statistics
* Improve Mad Max validation rules and messaging
* Add support for custom minimum number instead of always starting at 1
* Improve menu/input UX by supporting more shortcuts consistently
* Add a replay summary screen after each round 

## Author

Chris Tolan
