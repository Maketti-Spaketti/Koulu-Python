from pathlib import Path

# Read/Write on .py folder,not cwd
ROOT_FOLDER = Path(__file__).parent


def askAnalysisTarget() -> str:
    return input("Insert filename: ")


def parseData(data: list[str]) -> tuple[int, int, int, float]:
    """Parses given lit of string numbers
    and returns count, sum, greatest and average

    Args:
        data (list[str]): List of string type numbers

    Returns:
        tuple[int, int, int, float]: count, sum, greatest, average
    """
    int_data = list(map(int, data))
    count = len(int_data)
    summed = sum(int_data)
    greatest = max(int_data)
    average = summed / count
    return (count, summed, greatest, average)


def analyzeFile(filename: str) -> None:
    file_path = ROOT_FOLDER / filename
    print("#### Number analysis - START ####")
    raw_data = file_path.read_text().splitlines()
    count, summed, greatest, average = parseData(raw_data)
    # Flake8 bugeja
    print(f'File "{filename}" results:')  # noqa
    print("Count;Sum;Greatest;Average")  # noqa
    print(f"{count};{summed};{greatest};{average:.2f}")  # noqa
    print("")
    print("#### Number analysis - END ####")
    return None


def main() -> None:
    print("Program starting.")
    filename = askAnalysisTarget()
    analyzeFile(filename)
    print("Program ending.")
    return None


if __name__ == "__main__":
    main()
