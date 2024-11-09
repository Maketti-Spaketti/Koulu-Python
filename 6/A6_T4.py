from pathlib import Path

# Read/Write on .py folder,not cwd
ROOT_FOLDER: Path = Path(__file__).parent


def askAnalysisTarget() -> str:
    return input("Insert filename to read: ")


def analyzeFile(filename) -> None:
    file_path: Path = ROOT_FOLDER / filename
    print(f'Reading names from "{filename}".')
    print("Analysing names...")
    print("Analysis complete!")
    print("#### REPORT BEGIN ####")

    # names = file_path.read_text().splitlines()
    # names = [x for x in names if x]
    # count = len(names)
    # shortest = min(names, key=len)
    # longest = max(names, key=len)
    # summed = sum(len(x) for x in names)

    count = 0
    shortest = 9999
    longest = 0
    summed = 0
    for name in file_path.read_text().splitlines():
        if not name:
            continue
        length = len(name)
        count += 1
        if length < shortest:
            shortest = length
        if length > longest:
            longest = length
        summed += length

    print(f"Name count - {count}")
    print(f"Shortest name - {shortest} chars")
    print(f"Longest name - {longest} chars")
    print(f"Average name -{summed / count: .2f} chars")
    print("#### REPORT END ####")
    return None


def main() -> None:
    print("Program starting.")
    print("This program analyses a list of names from a file.")
    filename = askAnalysisTarget()
    analyzeFile(filename)
    print("Program ending.")
    return None


if __name__ == "__main__":
    main()
