from pathlib import Path

# Read/Write on .py folder,not cwd
ROOT_FOLDER = Path(__file__).parent


def askFileDetails() -> tuple[str, str, str]:
    return (
        input("Insert first name: "),
        input("Insert last name: "),
        input("Insert filename: "),
    )


def writeFile(first: str, last: str, file: str) -> None:
    file_path = ROOT_FOLDER / file
    with file_path.open("w"):
        file_path.write_text(f"{first}\n{last}\n")
    return None


def main() -> None:
    print("Program starting.")
    first, last, file = askFileDetails()
    writeFile(first, last, file)
    print("Program ending.")
    return None


if __name__ == "__main__":
    main()
