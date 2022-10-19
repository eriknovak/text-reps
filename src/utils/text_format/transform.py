import re

from typing import List

# -----------------------------------------------
# Transformation Methods
# -----------------------------------------------


def t_generic(text: str, pattern: str, replacement: str) -> str:
    """A generic method for transforming text
    Args:
        text: The text to be changed.
        pattern: The pattern we wish to change.
        replacement: The blueprint how we want to change the found pattern.
    Returns: The transformed text.
    """
    return re.sub(pattern, replacement, text)


def t_camelcase(text: str) -> str:
    """Transforms text by splitting camelcase word into two or more words
       Example: "camelCase" -> "camel Case"
    Args:
        text: The text to be changed.
    Returns: The transformed text.
    """
    return t_generic(text, r"([a-z])([A-Z])", r"\g<1> \g<2>")


def t_capitalize(text: str) -> str:
    """Transforms text my capitalizing every word
       Example: "I am a happy monkey" -> "I Am A Happy Monkey"
    Args:
        text: The text to be changed.
    Returns: The transformed text.
    """

    def _uppercase_first_char(t):
        return t.group(0).upper() if t else None

    return t_generic(text, r"(\b[a-z](?!\s))", _uppercase_first_char)


def t_lowercase(text: str) -> str:
    """Transforms text by making the text lowercase
       Example: "This is Mount Everest" -> "this is mount everest"
    Args:
        text: The text to be changed.
    Returns: The transformed text.
    """
    return text.lower()


def t_uppercase(text: str) -> str:
    """Transforms text by making the text uppercase
       Example: "I am not shouting" -> "I AM NOT SHOUTING"
    Args:
        text: The text to be changed.
    Returns: The transformed text.
    """
    return text.upper()


def t_underscore(text: str) -> str:
    """Transforms text by splitting underscored words into two or more words
       Example: "text_underscore" -> "text underscore"
    Args:
        text: The text to be changed.
    Returns: The transformed text.
    """
    return t_generic(text, r"(_+)", " ")


def t_monospace(text: str) -> str:
    """Transforms text by merging multiple whitespaces into one
       Example: "this is    a text" -> "this is a text"
    Args:
        text: The text to be changed.
    Returns: The transformed text.
    """
    return t_generic(text, r"\s+", " ")


# -----------------------------------------------
# Transformation Mapping
# -----------------------------------------------

key_transform_map = {
    # CamelCase transform
    "CC": t_camelcase,
    # CaPitalize transform
    "CP": t_capitalize,
    # LowerCase transform
    "LC": t_lowercase,
    # UpperCase transform
    "UC": t_uppercase,
    # UnderScore transform
    "US": t_underscore,
    # MonoSpace transform
    "MS": t_monospace,
}

# -----------------------------------------------
# Transformation String Function
# -----------------------------------------------


def transform_string(text: str, commands: List[str]) -> str:
    """Transforms the provided text based on the given commands
    Args:
        text: The text to be transformed.
        commands: The list of commands. Possible options:
            CC - Transforms text by splitting camelcase word into two or more words
            CP - Transforms text my capitalizing every word
            LC - Transforms text by making the text lowercase
            UC - Transforms text by making the text uppercase
            US - Transforms text by splitting underscored words into two or more words
            MS - Transforms text by merging multiple whitespaces into one
    Returns: The transformed text.

    """
    current_text = text
    for command in commands:
        transform = key_transform_map.get(command)
        if transform:
            current_text = transform(current_text)
    return current_text
