########################################################
# Timestamp library
# Developer Markus Kivinen
# Date 2024-11-08
########################################################
from datetime import datetime


def readTimestampsFromFile(filename: str, format: str) -> list[datetime]:
    """Reads timestamps from a file and returns them as a list.
    Args:
        filename (str): The name of the file.
    Returns:
        list[datetime]: The timestamps.
    """
    try:
        with open(filename, "r") as file:
            return [
                datetime.strptime(value, format)
                for value in file.read().splitlines()
                if value
            ]
    except FileNotFoundError:
        return []


def filterByYear(timestamps: list[datetime], year: int) -> list[datetime]:
    """Filters timestamps by year.
    Args:
        timestamps (list[datetime]): The timestamps to filter.
        year (int): The year to filter by.

    Returns:
        list[datetime]: The filtered timestamps.
    """
    return [stamp for stamp in timestamps if stamp.year == year]


def filterByMonth(timestamps: list[datetime], month: str) -> list[datetime]:
    """Filters timestamps by month.
    Args:
        timestamps (list[datetime]): The timestamps to filter.
        month (str): The month to filter by.

    Returns:
        list[datetime]: The filtered timestamps.
    """
    return [
        stamp
        for stamp in timestamps
        if stamp.strftime("%B").lower() == month.lower()
    ]


def filterByWeekday(
    timestamps: list[datetime], weekday: str
) -> list[datetime]:
    """Filters timestamps by weekday.
    Args:
        timestamps (list[datetime]): The timestamps to filter.
        weekday (str): The weekday to filter by.

    Returns:
        list[datetime]: The filtered timestamps.
    """
    return [
        stamp
        for stamp in timestamps
        if stamp.strftime("%A").lower() == weekday.lower()
    ]
