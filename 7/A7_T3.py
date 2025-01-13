from pathlib import Path

ROOT_FOLDER = Path(__file__).parent
WEEKDAYS = (
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturnday",
    "Sunday",
)


def askFilename() -> str:
    return input("Insert filename: ")


def processFile(filename: str) -> list[str]:
    file_path = ROOT_FOLDER / filename
    if not file_path.exists():
        # print(f"File {filename} not found")
        return []
    print(f'Reading file "{filename}".')
    content = file_path.read_text(encoding="utf-8")
    rows = content.splitlines()[1:]
    return rows


def analyseTimestamps(rows: list[str]) -> dict[str, int]:
    print("Analysing timestamps.")
    results = {i: 0 for i in WEEKDAYS}
    for row in rows:
        if not row:
            continue
        # Weekday;Hour;Consumption(kWh);Price(€/kWh)
        weekday, _, _, _ = row.split(";")
        if weekday in results:
            results[weekday] += 1
    return results


def displayResults(results: dict[str, int]) -> None:
    print("Displaying results.")
    print("### Timestamp analysis ###")
    for i in results:
        print(f" - {i} {results[i]} stamps")
    print("### Timestamp analysis ###")
    return None


def main() -> None:
    print("Program starting.")
    filename = askFilename()
    rows = processFile(filename)
    results = analyseTimestamps(rows)
    displayResults(results)
    print("Program ending.")
    return None


if __name__ == "__main__":
    main()
