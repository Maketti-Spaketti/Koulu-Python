from pathlib import Path

# Read/Write on .py folder,not cwd
ROOT_FOLDER = Path(__file__).parent


def askCopyTarget() -> tuple[str, str]:
    return (
        input("Insert source filename: "),
        input("Insert destination filename: "),
    )


def copyFile(origin: str, destination: str) -> None:
    origin_path = ROOT_FOLDER / origin
    destination_path = ROOT_FOLDER / destination
    print(f"Reading file '{origin}' content.")
    origin_data = origin_path.read_bytes()
    print("File content ready in memory.")
    print(f"Writing content into file '{destination}'.")
    destination_path.write_bytes(origin_data)
    print("Copying operation complete.")
    return None


def main() -> None:
    print("Program starting.")
    print("This program can copy a file.")
    first, last = askCopyTarget()
    copyFile(first, last)
    print("Program ending.")
    return None


if __name__ == "__main__":
    main()
