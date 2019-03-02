"""
General utility functions.
"""

import json
from pathlib import Path
from typing import Callable
import numpy as np
import time

def todayDateStr():
    return  time.strftime("%Y-%m-%d",time.localtime())

def get_path(temp_name: str):
    """
       Get path where trader is running in.
    """
    cwd = Path.cwd()
    temp_path = cwd.joinpath(temp_name)

    # If .vigar folder exists in current working directory,
    # then use it as trader running path.
    if temp_path.exists():
        return cwd, temp_path

    # Otherwise use home path of system.
    home_path = Path.home()
    temp_path = home_path.joinpath(temp_name)

    # Create .vigar folder under home path if not exist.
    if not temp_path.exists():
        temp_path.mkdir()

    return home_path, temp_path

TRADER_PATH, TEMP_PATH = get_path(".vigar")

def get_file_path(filename: str):
    """
    Get path for temp file with filename.
    """
    return TEMP_PATH.joinpath(filename)

def get_folder_path(folder_name: str):
    """
    Get path for temp folder with folder name.
    """
    folder_path = TEMP_PATH.joinpath(folder_name)
    if not folder_path.exists():
        folder_path.mkdir()
    return folder_path

def get_icon_path(filepath: str, ico_name: str):
    """
    Get path for icon file with ico name.
    """
    ui_path = Path(filepath).parent
    icon_path = ui_path.joinpath("ico", ico_name)
    return str(icon_path)

def load_json(filename: str):
    """
    Load data from json file in temp path.
    """
    filepath = get_file_path(filename)
    print(filepath)
    if filepath.exists():
        with open(filepath, mode='r') as f:
            data = json.load(f)
        return data
    else:
        save_json(filename, {})
        return {}

def save_json(filename: str, data: dict):
    """
    Save data into json file in temp path.
    """
    filepath = get_file_path(filename)
    with open(filepath, mode='w+') as f:
        json.dump(data, f, indent=4)

if __name__ == '__main__':
    a=load_json("mail.json")
    print(a)