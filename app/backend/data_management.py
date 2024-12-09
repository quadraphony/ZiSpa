# backend/data_management.py
import json
import os
from app.config import settings

def load_json(file_path):
    """Helper function to load a JSON file. Creates the file if it doesn't exist."""
    if not os.path.exists(file_path):
        print(f"File {file_path} not found, creating a new one.")
        with open(file_path, "w") as file:
            json.dump([], file, indent=4)  # Create an empty list if the file doesn't exist
        return []  # Return an empty list if the file was created
    else:
        with open(file_path, "r") as file:
            return json.load(file)

def save_json(file_path, data):
    """Helper function to save data to a JSON file."""
    with open(file_path, "w") as file:
        json.dump(data, file, indent=4)

def validate_user(username, password):
    """Checks if the user credentials are valid."""
    users = load_json(settings.USER_DATA_FILE_PATH)
    for user in users:
        if user["username"] == username and user["password"] == password:
            return True
    return False

def user_exists(username):
    """Checks if a user already exists."""
    users = load_json(settings.USER_DATA_FILE_PATH)
    for user in users:
        if user["username"] == username:
            return True
    return False

def add_user(username, password, role="user"):
    """Adds a new user to the user data file with a default role."""
    users = load_json(settings.USER_DATA_FILE_PATH)
    users.append({"username": username, "password": password, "role": role})
    save_json(settings.USER_DATA_FILE_PATH, users)
