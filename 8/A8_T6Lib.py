########################################################
# Common utility library
# Developer Markus Kivinen
# Date 2024-11-08
########################################################
def readFloatsFromFile(filename: str) -> list[float]:
    """Reads values from a file and returns them as a list.
    Args:
        filename (str): The name of the file.
    Returns:
        list[float]: The values.
    """
    try:
        with open(filename, "r") as file:
            return [
                float(value) for value in file.read().splitlines() if value
            ]
    except FileNotFoundError:
        return []


def sleep(duration: float) -> None:
    """Pauses the program for the given duration in seconds.
    Args:
        duration (int): The duration in seconds.
    """
    import time

    time.sleep(duration)
