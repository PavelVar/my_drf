from random import choice, randint
from string import digits


def generate_account_number() -> str:
    """
    Generates a random account number
    """
    random_number_1 = "".join(choice(digits) for _ in range(2))
    random_number_2 = "".join(choice(digits) for _ in range(6))
    random_symbols_1 = "".join(chr(randint(65, 91)).upper() for _ in range(2))
    random_symbols_2 = "".join(chr(randint(65, 91)).upper() for _ in range(2))
    account_number = random_symbols_1 + random_number_1 + "RPGN" + "3014" + random_symbols_2 + random_number_2

    return account_number
