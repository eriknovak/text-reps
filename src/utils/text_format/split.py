import re

from typing import List

def s_generic(text: str, pattern: str) -> List[str]:
    """A generic method for splitting text
    Args:
        text: The text to be split.
        pattern: The pattern used to split the text.
    Returns: The list of text parts.
    """
    return re.split(pattern, text)


def s_delimiter(text: str, delimiter: str = ","):
    """Split text based on provided delimiter
    Args:
        text: The text to be split.
        delimiter: The delimiter used to split the text.
    Returns: The list of text parts.
    """
    return s_generic(text, delimiter)


def s_space_after_punctuation(text: str):
    """Split text based on spaces after the punctuation
    Args:
        text: The text to be split.
    Returns: The list of text parts.
    """
    return s_generic(text, r"(?<=[.!?])\s+")