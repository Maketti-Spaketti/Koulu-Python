########################################################
# Input library
# Developer Markus Kivinen
# Date 2024-11-08
########################################################


def getIntInput(prompt: str) -> int:
    """
    Returns an integer value from user input.
    If the input is not an integer, returns -1.

    Returns:
        int: The user's input.
    """
    value = input(prompt)
    try:
        return int(value)
    except ValueError:
        return -1


def getConfirmation(prompt: str) -> bool:
    """
    Returns a boolean value from user input.
    If the input is not 'y' or 'n', returns False.

    Returns:
        bool: The user's input.
    """
    value = input(prompt)
    return value.lower() == "y"


def getFloatInput(prompt: str) -> float:
    """
    Returns an integer value from user input.
    If the input is not an float, returns -1.

    Returns:
        float: The user's input.
    """
    value = input(prompt)
    try:
        return float(value)
    except ValueError:
        return -1


def getStrInput(prompt: str) -> str:
    """
    Returns an string from user input.

    Returns:
        str: The user's input.
    """
    value = input(prompt)
    return value


def getUserChoice(self) -> int:
    """Returns the user's choice.
    If the input is not an integer, returns -1.

    Returns:
        int: The user's choice.
    """
    return self.getIntInput("Enter your choice: ")


def showOptions(header: str, options: dict[int, str]) -> None:
    """Shows the options to the user.
    Args:
        options (dict[int, str]): The options to show.
    """
    print(header)
    for i in options:
        print(f"{i} - {options[i]}")
