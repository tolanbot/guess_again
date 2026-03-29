# number guessing game
from random import randint
from dataclasses import dataclass
from enum import Enum, auto


DEFAULT_MIN_NUM = 1
DEFAULT_MAX_NUM = 10
DEFAULT_MAX_TRIES = 5


@dataclass(frozen=True)
class GameConfig:
    difficulty: str
    min_num: int
    max_num: int
    max_tries: int


class Difficulty(Enum):
    EASY = GameConfig("Easy", DEFAULT_MIN_NUM, DEFAULT_MAX_NUM, DEFAULT_MAX_TRIES)
    MEDIUM = GameConfig("Medium", 1, 20, 5)
    HARD = GameConfig("Hard", 1, 50, 7)


@dataclass
class GameStats:
    games_played: int = 0
    games_won: int = 0
    games_lost: int = 0
    games_abandonded: int = 0
    high_score: int = 0


def choose_difficulty() -> Difficulty:
    while True:
        print(
            """
Choose Difficulty:
    1. Easy   (1-10, 5 tries)
    2. Medium (1-20, 5 tries)
    3. Hard   (1-50, 7 tries)
    """
        )
        choice = input("Enter 1, 2, or 3: ").strip()

        if choice == "1":
            print(f"{Difficulty.EASY.value.difficulty} difficulty selected.")
            return Difficulty.EASY
        if choice == "2":
            print(f"{Difficulty.MEDIUM.value.difficulty} difficulty selected.")
            return Difficulty.MEDIUM
        if choice == "3":
            print(f"{Difficulty.HARD.value.difficulty} difficulty selected.")
            return Difficulty.HARD
        print("Invalid Choice. Please enter 1, 2, or 3...")


def get_stats(stats: GameStats):
    print(
        f"""
***** Current Game Stats *****
Games Played: {stats.games_played}
Games Won: {stats.games_won}
Games Lost: {stats.games_lost}
Games Abandoned: {stats.games_abandonded}
"""
    )


def play_game(config: GameConfig, stats: GameStats):
    rand_num: int = randint(config.min_num, config.max_num)
    num_guesses: int = 0
    guesses: set[int] = set()

    print(f"\nCurrent difficulty: {config.difficulty}")

    while num_guesses < config.max_tries:
        entry = get_guess_or_command(config)

        if entry == "quit":
            stats.games_abandonded += 1
            stats.games_played += 1
            print("Ending This Round.")
            return

        if entry == "stats":
            get_stats(stats)
            continue

        try:
            guess = int(entry)
        except ValueError:
            print("Type entered cannot be converted to int... Guess again!")
            continue

        if guess < config.min_num or guess > config.max_num:
            print(f"Guess must be between {config.min_num} and {config.max_num} (inclusive)... Guess again!")
            continue

        if guess in guesses:
            print(f"You have already guessed {guess}... Guess again!")
            continue

        num_guesses += 1
        guesses.add(guess)

        if guess == rand_num:
            stats.games_won += 1
            stats.games_played += 1
            print("You guessed the random number!")
            return

        greater_or_lower = "lower" if guess < rand_num else "higher"
        print(f"Your guess is {greater_or_lower} than the random number.")
        print(f"You have {config.max_tries - num_guesses} remaining...")

    stats.games_lost += 1
    stats.games_played += 1
    print("Sorry too many guesses! The number was", rand_num)


def get_guess_or_command(config: GameConfig) -> str:
    prompt = f"Guess a number between {config.min_num} and {config.max_num} " f"(or type 'stats' or 'quit'): "
    return input(prompt).strip().lower()


def get_continue():
    while True:
        answer = input("Do you want to play again?(y/n) ").strip().lower()
        if answer == "y":
            return True
        if answer == "n":
            return False
        print("Please only enter 'y' or 'n'...")


def display_main_menu(config: GameConfig, stats: GameStats):
    print("***** GUESS AGAIN: THE GAME *****")
    while True:
        print(
            """
    1. Start
    2. Choose Difficulty
    3. Current Stats
    4. Quit
    """
        )
        choice = input("Enter 1, 2, 3 or 4: ").strip()

        if choice == "1":
            while True:
                play_game(config, stats)
                if not get_continue():
                    print("Back to main menu...")
                    break
            continue
        if choice == "2":
            difficulty = choose_difficulty()
            config = difficulty.value
            continue
        if choice == "3":
            get_stats(stats)
            continue
        if choice == "4":
            print("Goodbye for now!")
            break
        print("Invalid Choice. Please enter 1, 2, 3 or 4...")


def main() -> None:
    stats = GameStats()
    config = Difficulty.EASY.value
    display_main_menu(config, stats)


if __name__ == "__main__":
    main()
