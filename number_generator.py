"""
This module provides utility functions for processing text and calculating
the sum of numeric values found within the text using Decimal for precision.
"""

from typing import Callable, Generator
from decimal import Decimal, InvalidOperation
import re

# Compile the regular expression once to check if word is decimal
_DECIMAL_PATTERN = re.compile(r'\d+(\.\d+)?')


def generator_numbers(text: str) -> Generator[Decimal, None, None]:
    """
    Generator function that yields Decimal numbers from a given text.
    Non-numeric words and special values like 'Infinity' and 'NaN' are ignored.

    Args:
        text (str): The input text containing potential numbers.

    Yields:
        Decimal: The numbers found in the text.
    """
    for match in _DECIMAL_PATTERN.finditer(text):
        try:
            yield Decimal(match.group(0))
        except InvalidOperation:
            continue  # Skip invalid values


def sum_profit(text: str, func: Callable[[str], Generator[Decimal, None, None]]) -> Decimal:
    """
    Sums the numbers generated from the given text using the specified function.

    Args:
        text (str): The input text containing numbers.
        func (Callable[[str], Generator[Decimal, None, None]]): The function used to generate 
        numbers from the text.

    Returns:
        Decimal: The total sum of the numbers.
    """
    return sum(func(text), Decimal(0))
