# number guessing game
from random import randint
from dataclasses import dataclass, field
from enum import Enum, auto


DEFAULT_MIN_NUM = 1
DEFAULT_MAX_NUM = 10
DEFAULT_MAX_TRIES = 4


class GameResult(Enum):
    WON = auto()
    LOST = auto()
    QUIT = auto()


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
    high_scores: dict[Difficulty, int] = field(
        default_factory=lambda: {
            Difficulty.EASY: 0,
            Difficulty.MEDIUM: 0,
            Difficulty.HARD: 0,
            Difficulty.MAD_MAX: 0,
        }
    )


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

        choice = input("Enter 1, 2, 3 or 4: ").strip().lower()

        if choice == "1" or choice == "easy" or choice == "e":
            return Difficulty.EASY
        if choice == "2" or choice == "medium" or choice == "md":
            return Difficulty.MEDIUM
        if choice == "3" or choice == "hard" or choice == "h":
            return Difficulty.HARD
        if choice == "4" or choice == "mad max" or choice == "madmax" or choice == "mm":
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


def get_stats(stats: GameStats, config: GameConfig) -> None:
    print(
        f"""\
***** Current Game Stats *****
Games Played: {stats.games_played}
Games Won: {stats.games_won}
Games Lost: {stats.games_lost}
Games Abandoned: {stats.games_abandoned}
High Scores:
    {display_difficulty(Difficulty.EASY)}:\t{stats.high_scores[Difficulty.EASY]}
    {display_difficulty(Difficulty.MEDIUM)}:\t{stats.high_scores[Difficulty.MEDIUM]}
    {display_difficulty(Difficulty.HARD)}:\t{stats.high_scores[Difficulty.HARD]}
    {display_difficulty(Difficulty.MAD_MAX)}:\t{stats.high_scores[Difficulty.MAD_MAX]}"""
    )


def handle_command_entry(entry: str, config: GameConfig, stats: GameStats) -> tuple[bool, GameResult | None]:
    if entry in ("quit", "q"):
        print("Ending this round...")
        return True, GameResult.QUIT

    if entry in ("stats", "st"):
        get_stats(stats, config)
        return True, None

    return False, None


def process_valid_guess(
    guesses: set[int], guess: int, num_guesses: int, config: GameConfig, rand_num: int, stats: GameStats
) -> GameResult | None:
    guesses.add(guess)
    remaining_guesses = config.max_tries - num_guesses

    if guess_is_match(guess, rand_num, config, stats, remaining_guesses):
        return GameResult.WON

    greater_or_lower = "Too low..." if guess < rand_num else "Too high..."
    print(greater_or_lower)
    guess_or_guesses = "guess" if remaining_guesses == 1 else "guesses"
    print(f"You have {remaining_guesses} {guess_or_guesses} remaining...")
    return None


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


def guess_is_match(guess: int, rand_num: int, config: GameConfig, stats: GameStats, remaining_guesses: int) -> bool:
    if guess == rand_num:
        score = calculate_score(config, remaining_guesses)
        print("You guessed the random number!")
        print(f"Score: {score}")
        if score > stats.high_scores[config.difficulty]:
            stats.high_scores[config.difficulty] = score
            print("You got a new high score!!!")
        return True
    return False


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


def play_game(config: GameConfig, stats: GameStats) -> GameResult:
    rand_num: int = randint(config.min_num, config.max_num)
    num_guesses: int = 0
    guesses: set[int] = set()
    display_game_config(config)

    while num_guesses < config.max_tries:
        prompt = "Guess again... "
        entry = input(prompt).strip().lower()

        command_received, result = handle_command_entry(entry, config, stats)
        if command_received:
            if result is not None:
                return result
            continue

        guess = validate_guess(entry, config, guesses)
        if guess == None:
            continue

        num_guesses += 1
        result = process_valid_guess(guesses, guess, num_guesses, config, rand_num, stats)
        if result is not None:
            return result

    print("Sorry too many guesses! The number was", rand_num)
    return GameResult.LOST


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

        choice = input("Enter 1, 2, 3 or 4: ").strip().lower()

        if choice == "1" or choice == "start" or choice == "s":
            while True:
                game_result = play_game(config, stats)
                add_result_to_stats(game_result, stats)
                if game_result == GameResult.QUIT:
                    break
                if not player_continue():
                    print("Back to main menu...")
                    break
            continue
        if choice == "2" or choice == "diff" or choice == "d":
            difficulty = choose_difficulty()
            print(f"{display_difficulty(difficulty)} difficulty selected.")
            config = map_difficulty_to_config(difficulty)
            continue
        if choice == "3" or choice == "stats" or choice == "st":
            get_stats(stats, config)
            continue
        if choice == "4" or choice == "quit" or choice == "q":
            print("Goodbye for now!")
            break
        print("Invalid Choice. Please enter 1, 2, 3 or 4...")


def main() -> None:
    stats = GameStats()
    display_main_menu(map_difficulty_to_config(Difficulty.EASY), stats)


if __name__ == "__main__":
    main()
