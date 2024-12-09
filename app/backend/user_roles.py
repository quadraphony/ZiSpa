# backend/user_roles.py
from app.backend import data_management

def check_role(username, role):
    """Checks if the user has the specified role."""
    users = data_management.load_json("app/data/user_data.json")
    for user in users:
        if user["username"] == username:
            return user["role"] == role
    return False

def grant_role(username, role):
    """Grants a specific role to a user."""
    users = data_management.load_json("app/data/user_data.json")
    for user in users:
        if user["username"] == username:
            user["role"] = role
            data_management.save_json("app/data/user_data.json", users)
            print(f"{role} role granted to {username}.")
            return True
    print(f"User {username} not found.")
    return False

def get_user_role(username):
    """Gets the role of a user."""
    users = data_management.load_json("app/data/user_data.json")
    for user in users:
        if user["username"] == username:
            return user["role"]
    return None
