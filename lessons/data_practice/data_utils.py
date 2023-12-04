"""Docstring moment."""
from csv import DictReader


def read_scv_rows(filename: str) -> list[dict[str, str]]:
    """Reading csv file."""
    result: list[dict[str, str]] = []
    file_handle = open(filename, "r", encoding="utf8")
    csv_reader = DictReader(file_handle)
    for row in csv_reader:
        result.append(row)
    file_handle.close()
    return result


def column_vals(table: list[dict[str, str]], header: str ) -> list[str]:
    """Docstring docstring docstring."""
    result: list[str] = []
    for elem in table:
        result.append(elem[header])
    return result