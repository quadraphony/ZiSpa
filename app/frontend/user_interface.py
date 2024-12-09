# frontend/user_interface.py
from app.backend import auth, user_roles
from app.frontend import prompts

def display_main_menu():
    """Display the main menu and prompt the user for an action."""
    print("\n=== Welcome to ZiSpa ===")
    print("1. Login")
    print("2. Sign up")
    print("3. Exit")
    choice = input("Choose an option (1-3): ")

    if choice == "1":
        auth.login()  # Call the login function
    elif choice == "2":
        auth.signup()  # Call the signup function
    elif choice == "3":
        print("Exiting ZiSpa. Goodbye!")
        exit()
    else:
        print("Invalid option. Please choose again.")
        display_main_menu()  # Recurse to the menu if input is invalid

def get_user_choice():
    """Prompt the user to choose between login or sign up."""
    choice = input("Please select an option:\n1. Login\n2. Sign up\nChoice: ")
    if choice == "1":
        return "1"  # Login
    elif choice == "2":
        return "2"  # Sign up
    else:
        print("Invalid choice. Please select a valid option.")
        return get_user_choice()  # Recursively ask until valid input
