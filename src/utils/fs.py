import os
import json

DIRNAME = os.path.dirname(__file__)

def read_txt_file(filepath: str):
    __filepath = os.path.join(DIRNAME, "..", "..", filepath)
    with open(__filepath, "r", encoding="utf8") as f:
        return f.read()


def read_json_file(dirpath: str, filename: str):
    filepath = os.path.join(DIRNAME, "..", "..", dirpath, filename)
    with open(filepath, "r", encoding="utf8") as f:
        return json.load(f)


def save_json_to_file(dirpath: str, filename: str, jsonb):
    """Saves the json into the file
    Args:
        dirpath (str): The relative path from the src/utils folder.
        filename (str): The name of the file.
        jsonb (dict[]): The array of dictionaries containing the model ID and score.
    Returns:
        None

    """
    dir_path = os.path.join(DIRNAME, "..", "..", dirpath)
    os.makedirs(dir_path, exist_ok=True)
    with open(os.path.join(dir_path, filename), "w", encoding="utf8") as f:
        json.dump(jsonb, f, ensure_ascii=False)
