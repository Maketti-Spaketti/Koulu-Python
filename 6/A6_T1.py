from pathlib import Path

# Read/Write on .py folder,not cwd
ROOT_FOLDER = Path(__file__).parent


def askfileName() -> Path:
    return ROOT_FOLDER / input("Insert filename: ")


def printFile(filepath: Path) -> None:
    print(f'#### START "{filepath.name}" ####')
    print(filepath.read_text())
    print(f'#### END "{filepath.name}" ####')
    return None


def main() -> None:
    print("Program starting.")
    print("This program can read a file.")
    filename = askfileName()
    printFile(filename)
    print("Program ending.")
    return None


if __name__ == "__main__":
    main()
