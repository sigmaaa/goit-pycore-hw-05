"""
This module provides functionality to parse, filter, and analyze log entries.

It includes the following features:
- Parsing log lines into structured log entries.
- Loading log lines from a file.
- Filtering log entries by log level.
- Counting log entries by log level.
- Displaying log counts in a formatted table.
- Converting log entries to a space-separated string for easy printing.

Usage:
    python log_parser.py <log_file_path> [<log_level>]

    <log_file_path>: Path to the log file containing log entries.
    <log_level>: Optional filter to display log entries of a specific level.

Example:
    python log_parser.py logs.txt INFO
    This will read log entries from 'logs.txt', count the number of log entries by level,
    and print details for logs with the level 'INFO'.
"""

import sys
from pathlib import Path
from collections import defaultdict, namedtuple

# Define the named tuple for log entries
LogEntry = namedtuple('LogEntry', ['date', 'time', 'level', 'message'])


def parse_log_line(line: str) -> LogEntry:
    """
    Parse a single log line into a named tuple.

    Args:
        line (str): A single log line in the format "date time level message".

    Returns:
        LogEntry: A named tuple with fields "date", "time", "level", and "message".
    """
    try:
        date, time, level, message = line.split(' ', 3)
    except ValueError as exc:
        raise ValueError(f"Log line '{line}' is not in the expected format.") from exc
    return LogEntry(date, time, level, message)


def load_logs(file_path: str) -> list:
    """
    Load log lines from a file.

    Args:
        file_path (str): The path to the log file.

    Returns:
        list: A list of log lines.

    Raises:
        FileNotFoundError: If the file does not exist.
    """
    path = Path(file_path)
    if not path.is_file():
        raise FileNotFoundError(f"The file {file_path} does not exist.")
    with path.open(mode="r", encoding="UTF-8") as file:
        return file.readlines()


def filter_logs_by_level(logs: list, level: str) -> list:
    """
    Filter logs by the specified level.

    Args:
        logs (list): A list of LogEntry named tuples.
        level (str): The log level to filter by.

    Returns:
        list: A list of filtered LogEntry named tuples.
    """
    return [log for log in logs if log.level == level]


def count_logs_by_level(logs: list) -> dict:
    """
    Count logs by their level.

    Args:
        logs (list): A list of LogEntry named tuples.

    Returns:
        dict: A dictionary with log levels as keys and counts as values.
    """
    count_lvl_log_dict = defaultdict(int)
    for log in logs:
        count_lvl_log_dict[log.level] += 1
    return count_lvl_log_dict


def display_log_counts(counts: dict):
    """
    Display log counts in a table format.

    Args:
        counts (dict): A dictionary with log levels as keys and counts as values.
    """
    headers = ["Рівень логування", "Кількість"]
    separator = "-" * 17 + "|" + "-" * 10

    max_level_len = max(len(headers[0]), max(
        len(level) for level in counts.keys()))
    max_count_len = max(len(headers[1]), max(
        len(str(count)) for count in counts.values()))

    header_row = f"{headers[0]:<{max_level_len}} | {
        headers[1]:<{max_count_len}}"

    print(header_row)
    print(separator)
    for level, count in counts.items():
        print(f"{level:<{max_level_len}} | {count:<{max_count_len}}")


def display_selected_level(selected_level: str, filtered_logs: list):
    """
    Display filtered logs by selected level

    Args: selected_level (str): choosen level, filtered_logs (list): filtered log list
    """
    print(f"Деталі логів для рівня '{selected_level}':")
    for log in filtered_logs:
        print(' '.join(log))


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python log_parser.py <log_file_path> [<log_level>]")
        sys.exit(1)
    file_path = sys.argv[1]
    lines = load_logs(file_path)
    try:
        lines = load_logs(file_path)
        logs = [parse_log_line(line) for line in lines]
    except (FileNotFoundError, ValueError) as e:
        print(f"Error: {e}")
        sys.exit(1)

    log_counts = count_logs_by_level(logs)
    display_log_counts(log_counts)

    if len(sys.argv) > 2:
        selected_level = sys.argv[2].upper()
        filtered_logs = filter_logs_by_level(logs, selected_level)
        display_selected_level(selected_level, filtered_logs)
