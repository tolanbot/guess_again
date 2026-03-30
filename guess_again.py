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
    games_abandoned: int = 0
    high_score: int = 0


class GameResult(Enum):
    WON = auto()
    LOST = auto()
    QUIT = auto()


def choose_difficulty() -> Difficulty:
    while True:
        print(
            """\
Choose Difficulty:
    1. Easy   (1-10, 4 tries)
    2. Medium (1-50, 5 tries)
    3. Hard   (1-100, 7 tries)
    4. Mad Max (Custom Game Config)"""
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
    if difficulty == Difficulty.MEDIUM:
        return GameConfig(Difficulty.MEDIUM, DEFAULT_MIN_NUM, 50, 5)
    if difficulty == Difficulty.HARD:
        return GameConfig(Difficulty.HARD, DEFAULT_MIN_NUM, 100, 7)
    if difficulty == Difficulty.MAD_MAX:
        return get_custom_game_config()

    raise ValueError(f"Unsupported difficulty: {difficulty}")


def get_custom_game_config() -> GameConfig:
    while True:
        max_num = parse_int_from_input("Choose max num: ")
        max_tries = parse_int_from_input("Choose max number of tries: ")
        if max_tries > max_num:
            print("Max num should be greater than max tries... please choose again.")
            continue
        break
    return GameConfig(Difficulty.MAD_MAX, DEFAULT_MIN_NUM, max_num, max_tries)


def parse_int_from_input(prompt: str) -> int:
    while True:
        response = input(prompt)
        try:
            parsed_int = int(response)
            if is_positive(parsed_int):
                return parsed_int
            print("Number must be greater than zero...")
            continue
        except ValueError:
            print("Could not parse int value...")
            continue


def is_positive(num: int) -> bool:
    return num > 0


def get_stats(stats: GameStats):
    print(
        f"""\
***** Current Game Stats *****
Games Played: {stats.games_played}
Games Won: {stats.games_won}
Current High Score: {stats.high_score}
Games Lost: {stats.games_lost}
Games Abandoned: {stats.games_abandoned}"""
    )


def play_game(config: GameConfig, stats: GameStats) -> GameResult:
    rand_num: int = randint(config.min_num, config.max_num)
    num_guesses: int = 0
    guesses: set[int] = set()
    display_game_config(config)

    while num_guesses < config.max_tries:
        prompt = "Guess again... "
        entry = input(prompt).strip().lower()

        if entry == "quit":
            print("Ending this round...")
            return GameResult.QUIT

        if entry == "stats":
            get_stats(stats)
            continue

        guess = validate_guess(entry, config, guesses)
        if guess == None:
            continue

        num_guesses += 1
        remaining_guesses = config.max_tries - num_guesses
        guesses.add(guess)

        if guess == rand_num:
            score = calculate_score(config, remaining_guesses)
            print("You guessed the random number!")
            print(f"Score: {score}")
            if score > stats.high_score:
                stats.high_score = score
                print("You got a new high score!!!")
            return GameResult.WON

        greater_or_lower = "Too low..." if guess < rand_num else "Too high..."
        print(greater_or_lower)
        guess_or_guesses = "guess" if remaining_guesses == 1 else "guesses"
        print(f"You have {remaining_guesses} {guess_or_guesses} remaining...")

    print("Sorry too many guesses! The number was", rand_num)
    return GameResult.LOST


def validate_guess(entry: str, config: GameConfig, guesses: set[int]) -> int | None:
    try:
        guess = int(entry)
    except ValueError:
        print("Type entered cannot be converted to int... Guess again!")
        return None

    if guess < config.min_num or guess > config.max_num:
        print(f"Guess must be between {config.min_num} and {config.max_num} (inclusive)... Guess again!")
        return None

    if guess in guesses:
        print(f"You have already guessed {guess}... Guess again!")
        return None
    return guess


def calculate_score(config: GameConfig, remaining_guesses: int) -> int:
    range_size = config.max_num - config.min_num + 1
    return int((range_size / config.max_tries) * (remaining_guesses + 1) * 10)

def player_continue() -> bool:
    while True:
        answer = input("Do you want to play again?(y/n) ").strip().lower()
        if answer == "y":
            return True
        if answer == "n":
            return False
        print("Please only enter 'y' or 'n'...")


def display_main_menu(config: GameConfig, stats: GameStats) -> None:
    print("***** GUESS AGAIN: THE GAME *****")
    while True:
        print(
            f"""\
Main Menu:
    1. Start
    2. Choose Difficulty (Current Difficulty: {display_difficulty(config.difficulty)})
    3. Current Stats
    4. Quit"""
        )

        choice = input("Enter 1, 2, 3 or 4: ").strip()

        if choice == "1" or choice.lower() == "start":
            while True:
                game_result = play_game(config, stats)
                add_result_to_stats(game_result, stats)
                if game_result == GameResult.QUIT:
                    break
                if not player_continue():
                    print("Back to main menu...")
                    break
            continue
        if choice == "2" or choice.lower() == "diff":
            difficulty = choose_difficulty()
            print(f"{display_difficulty(difficulty)} difficulty selected.")
            config = map_difficulty_to_config(difficulty)
            continue
        if choice == "3" or choice.lower() == "stats":
            get_stats(stats)
            continue
        if choice == "4" or choice.lower() == "quit":
            print("Goodbye for now!")
            break
        print("Invalid Choice. Please enter 1, 2, 3 or 4...")


def add_result_to_stats(game_result: GameResult, stats: GameStats) -> None:
    stats.games_played += 1
    if game_result == GameResult.QUIT:
        stats.games_abandoned += 1
    if game_result == GameResult.WON:
        stats.games_won += 1
    if game_result == GameResult.LOST:
        stats.games_lost += 1


def display_difficulty(difficulty: Difficulty) -> str:
    return difficulty.name.replace("_", " ").title()


def display_game_config(config: GameConfig) -> None:
    prompt = f"""\
Guess a number between {config.min_num} and {config.max_num}...
You have {config.max_tries} tries.
(or type 'stats' or 'quit'): """
    print(prompt)


def main() -> None:
    stats = GameStats()
    display_main_menu(map_difficulty_to_config(Difficulty.EASY), stats)


if __name__ == "__main__":
    main()
