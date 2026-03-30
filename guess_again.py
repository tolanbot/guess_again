# number guessing game
from random import randint
from dataclasses import dataclass
from enum import Enum, auto


DEFAULT_MIN_NUM = 1
DEFAULT_MAX_NUM = 10
DEFAULT_MAX_TRIES = 4


class Difficulty(Enum):
    EASY = auto()
    MEDIUM = auto()
    HARD = auto()
    MAD_MAX = auto()


@dataclass(frozen=True)
class GameConfig:
    difficulty: Difficulty
    min_num: int
    max_num: int
    max_tries: int


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
            """\
Choose Difficulty:
    1. Easy   (1-10, 4 tries)
    2. Medium (1-50, 5 tries)
    3. Hard   (1-100, 7 tries)
    4. MadMax (Custom Game Config)"""
        )

        choice = input("Enter 1, 2, 3 or 4: ").strip()

        if choice == "1":
            return Difficulty.EASY
        if choice == "2":
            return Difficulty.MEDIUM
        if choice == "3":
            return Difficulty.HARD
        if choice == "4":
            return Difficulty.MAD_MAX
        print("Invalid Choice. Please enter 1, 2, 3, or 4...")


def map_difficulty_to_config(difficulty: Difficulty) -> GameConfig:
    if difficulty == Difficulty.EASY:
        return GameConfig(Difficulty.EASY, DEFAULT_MIN_NUM, DEFAULT_MAX_NUM, DEFAULT_MAX_TRIES)
    elif difficulty == Difficulty.MEDIUM:
        return GameConfig(Difficulty.MEDIUM, 1, 50, 5)
    elif difficulty == Difficulty.HARD:
        return GameConfig(Difficulty.HARD, 1, 100, 7)
    else:
        return get_custom_game_config()


def get_custom_game_config() -> GameConfig:
    while True:
        max_num = input("Choose max num: ")
        try:
            max_num = int(max_num)
            break
        except ValueError:
            print("Could not parse value.")
            continue

    while True:
        max_tries = input("Choose max number of tries: ")
        try:
            max_tries = int(max_tries)
            break
        except ValueError:
            print("Could not parse value")
            continue

    return GameConfig(Difficulty.MAD_MAX, DEFAULT_MIN_NUM, max_num, max_tries)


def get_stats(stats: GameStats):
    print(
        f"""\
***** Current Game Stats *****
Games Played: {stats.games_played}
Games Won: {stats.games_won}
Current High Score: {stats.high_score}
Games Lost: {stats.games_lost}
Games Abandoned: {stats.games_abandonded}"""
    )


def play_game(config: GameConfig, stats: GameStats):
    rand_num: int = randint(config.min_num, config.max_num)
    num_guesses: int = 0
    guesses: set[int] = set()
    if config.difficulty != Difficulty.MAD_MAX:
        print(f"Current difficulty: {config.difficulty.name.title()}")
    else:
        print(
            f"Current difficulty: {config.difficulty.name.replace("_", " ").title()} (Max Num: {config.max_num}, Max Tries: {config.max_tries})"
        )

    while num_guesses < config.max_tries:
        entry = get_guess_or_command(config)

        if entry == "quit":
            stats.games_abandonded += 1
            stats.games_played += 1
            print("Ending this round...")
            return True

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
        remaining_guesses = config.max_tries - num_guesses
        guesses.add(guess)

        if guess == rand_num:
            stats.games_won += 1
            stats.games_played += 1
            score = calculate_score(config, remaining_guesses)
            print("You guessed the random number!")
            print(f"Score: {score}")
            if score > stats.high_score:
                stats.high_score = score
                print("You got a new high score!!!")
            return False

        greater_or_lower = "Too low..." if guess < rand_num else "Too high..."
        print(greater_or_lower)
        guess_or_guesses = "guess" if remaining_guesses == 1 else "guesses"
        print(f"You have {remaining_guesses} {guess_or_guesses} remaining...")

    stats.games_lost += 1
    stats.games_played += 1
    print("Sorry too many guesses! The number was", rand_num)


def calculate_score(config: GameConfig, remaining_guesses: int) -> int:
    range_size = config.max_num - config.min_num + 1
    return int((range_size / config.max_tries) * (remaining_guesses + 1) * 10)


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
            """\
Main Menu:
    1. Start
    2. Choose Difficulty
    3. Current Stats
    4. Quit"""
        )

        choice = input("Enter 1, 2, 3 or 4: ").strip()

        if choice == "1":
            while True:
                player_quit_mid_game = play_game(config, stats)
                if player_quit_mid_game:
                    break
                if not get_continue():
                    print("Back to main menu...")
                    break
            continue
        if choice == "2":
            difficulty = choose_difficulty()
            print(f"{difficulty.name.replace("_", " ").title()} difficulty selected.")
            config = map_difficulty_to_config(difficulty)
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
    display_main_menu(map_difficulty_to_config(Difficulty.EASY), stats)


if __name__ == "__main__":
    main()
