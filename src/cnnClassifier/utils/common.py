import os  # Import the os module for interacting with the operating system
from box.exceptions import BoxValueError  # Import BoxValueError exception from the box library
import yaml  # Import the yaml module for working with YAML files
from cnnClassifier import logger  # Import the logger from the cnnClassifier module
import json  # Import the json module for working with JSON data
import joblib  # Import the joblib module for serialization
from ensure import ensure_annotations  # Import the ensure_annotations decorator for type checking
from box import ConfigBox  # Import ConfigBox from the box library for better dictionary handling
from pathlib import Path  # Import Path from the pathlib module for path manipulations
from typing import Any  # Import Any type for type annotations
import base64  # Import base64 module for encoding and decoding

@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """
    Reads a YAML file and returns its content as a ConfigBox.

    Args:
        path_to_yaml (Path): Path to the YAML file.

    Raises:
        ValueError: If the YAML file is empty.
        e: For any other exception that occurs.

    Returns:
        ConfigBox: Content of the YAML file as a ConfigBox.
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"YAML file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("YAML file is empty")
    except Exception as e:
        raise e

@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """
    Create a list of directories.

    Args:
        path_to_directories (list): List of directory paths to create.
        verbose (bool, optional): Log the creation of directories. Defaults to True.
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"Created directory at: {path}")

@ensure_annotations
def save_json(path: Path, data: dict):
    """
    Save data to a JSON file.

    Args:
        path (Path): Path to the JSON file.
        data (dict): Data to be saved in the JSON file.
    """
    with open(path, "w") as f:
        json.dump(data, f, indent=4)
    logger.info(f"JSON file saved at: {path}")

@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    """
    Load data from a JSON file.

    Args:
        path (Path): Path to the JSON file.

    Returns:
        ConfigBox: Data loaded from the JSON file as a ConfigBox.
    """
    with open(path) as f:
        content = json.load(f)
    logger.info(f"JSON file loaded successfully from: {path}")
    return ConfigBox(content)

@ensure_annotations
def save_bin(data: Any, path: Path):
    """
    Save data to a binary file.

    Args:
        data (Any): Data to be saved as binary.
        path (Path): Path to the binary file.
    """
    joblib.dump(value=data, filename=path)
    logger.info(f"Binary file saved at: {path}")

@ensure_annotations
def load_bin(path: Path) -> Any:
    """
    Load data from a binary file.

    Args:
        path (Path): Path to the binary file.

    Returns:
        Any: Object stored in the file.
    """
    data = joblib.load(path)
    logger.info(f"Binary file loaded from: {path}")
    return data

@ensure_annotations
def get_size(path: Path) -> str:
    """
    Get the size of a file in KB.

    Args:
        path (Path): Path of the file.

    Returns:
        str: Size in KB.
    """
    size_in_kb = round(os.path.getsize(path) / 1024)
    return f"~ {size_in_kb} KB"

def decodeImage(imgstring: str, fileName: str):
    """
    Decode a base64-encoded image and save it to a file.

    Args:
        imgstring (str): Base64-encoded image string.
        fileName (str): Name of the file to save the decoded image.
    """
    imgdata = base64.b64decode(imgstring)
    with open(fileName, 'wb') as f:
        f.write(imgdata)

def encodeImageIntoBase64(croppedImagePath: str) -> str:
    """
    Encode an image file into a base64 string.

    Args:
        croppedImagePath (str): Path to the image file.

    Returns:
        str: Base64-encoded string of the image.
    """
    with open(croppedImagePath, "rb") as f:
        return base64.b64encode(f.read()).decode('utf-8')
