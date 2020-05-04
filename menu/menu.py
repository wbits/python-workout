from typing import Callable


class InvalidOption(Exception):
    pass


def menu(**options: Callable):
    choice = input('Pls choose: ')

    if choice not in options.keys():
        raise InvalidOption

    return options[choice]()
