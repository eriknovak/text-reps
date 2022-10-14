import re

def preprocess_text(texts, split: str = "(?<=[.!?])\s+"):
    """Preprocesses the text

    Args:
        texts (str | str[]): The texts to be preprocessed.
        split (str): The regex used to split the text into multiple parts.
    Returns:
        split_content (str[]): The preprocessed texts.

    """
    content = texts
    if isinstance(content, str):
        content = [content]

    split_content = []
    for element in content:
        split_content += re.split(split, element)

    return split_content