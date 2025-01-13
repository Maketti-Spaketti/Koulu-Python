# Python >= 3.12?
from pathlib import Path
from dataclasses import dataclass, field
from enum import IntEnum

ROOT_FOLDER = Path(__file__).parent


class WEEKDAY(IntEnum):
    Monday = 0
    Tuesday = 1
    Wednesday = 2
    Thursday = 3
    Friday = 4
    Saturnday = 5
    Sunday = 6


@dataclass(order=True)
class TIMESTAMP:
    weekday: WEEKDAY
    hour: str
    consumption: float
    price: float

    @property
    def cost(self) -> float:
        return self.price * self.consumption


@dataclass(order=True)
class DAY_USAGE:
    weekday: WEEKDAY
    _timestamps: list[TIMESTAMP] = field(default_factory=list)

    def add_timestamp(self, stamp: TIMESTAMP) -> None:
        self._timestamps.append(stamp)
        return None

    def sort_timestamps(self):
        self._timestamps.sort()

    def has_timestamps(self) -> bool:
        return len(self._timestamps) > 0

    @property
    def formatted_timestamps(self) -> str:
        return "\n".join(
            f" - {i.weekday.name} {i.hour}:00, "  # noqa
            f"price {i.price:.2f}, "  # noqa
            f"consumption {i.consumption:.2f} kWh, "  # noqa
            f"total {i.cost:.2f} €"  # noqa
            for i in self._timestamps
        )

    @property
    def summary(self) -> str:
        return (
            f" - {self.weekday.name} usage "
            f"{self.total_consumption:.2f} kWh, "  # noqa
            f"cost {self.total_cost:.2f} €"  # noqa
        )

    @property
    def hours(self) -> int:
        return len(self._timestamps)

    @property
    def average_consumption(self) -> float:
        if not self.has_timestamps():
            return 0
        return sum(i.consumption for i in self._timestamps) / self.hours

    @property
    def total_consumption(self) -> float:
        return sum(i.consumption for i in self._timestamps)

    @property
    def average_price(self) -> float:
        if not self.has_timestamps():
            return 0
        return sum(i.price for i in self._timestamps) / self.hours

    @property
    def total_cost(self) -> float:
        if not self.has_timestamps():
            return 0
        return sum(i.cost for i in self._timestamps)

    def __repr__(self) -> str:
        return (
            f"DAY_USAGE(\n"
            f"  {self.weekday=}\n"
            "  Entries: [\n"
            + "".join(f"    {i}\n" for i in self._timestamps)
            + "  ]\n)"
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


def analyzeRows(rows) -> list[DAY_USAGE]:
    print("Analysing timestamps.")
    results = [DAY_USAGE(i) for i in WEEKDAY]
    for row in rows:
        if not row:
            continue
        data = row.split(";")
        weekday = WEEKDAY[data[0]]
        stamp = TIMESTAMP(weekday, data[1], int(data[2]), float(data[3]))
        results[weekday.value].add_timestamp(stamp)
    # results.sort()
    # for i in results:
    #    i.sort_timestamps()
    # print(results)
    return results


def displayResults(results: list[DAY_USAGE]) -> None:
    print("Displaying results.")
    print("### Electricity consumption summary ###")
    for day in results:
        print(day.summary)
    print("### Electricity consumption summary ###")
    return None


def main() -> None:
    print("Program starting.")
    filename = askFilename()
    rows = processFile(filename)
    results = analyzeRows(rows)
    displayResults(results)
    print("Program ending.")
    return None


if __name__ == "__main__":
    main()
