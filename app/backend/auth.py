# backend/auth.py
from app.backend import data_management
from app.frontend import prompts

def login():
    """Handles user login"""
    print("Login:")
    username = prompts.get_username()
    password = prompts.get_password()

    # Check if the credentials are valid
    if data_management.validate_user(username, password):
        print(f"Welcome back, {username}!")

        # Get the user profile data to check for role
        profile = data_management.get_user_profile(username)
        if profile:
            role = profile.get("role", "user")  # Default to 'user' if no role is found
            
            if role == "admin":
                # Admin-specific actions
                print("You are logged in as an admin.")
                admin_menu(username)  # Call the admin-specific menu
            else:
                print("You are logged in as a regular user.")
                # Normal user flow
                user_menu(username)
        else:
            print("No profile found. Please complete your profile.")
            capture_profile_info(username)

    else:
        print("Invalid credentials, please try again.")
        retry = input("Would you like to try again? (y/n): ")
        if retry.lower() == 'y':
            login()  # Retry login
        else:
            print("Exiting login process...")

def admin_menu(username):
    """Displays the admin menu options."""
    print("\nAdmin Menu:")
    print("1. Manage Users")
    print("2. View Reports")
    print("3. Log Out")
    choice = input("Select an option: ")
    
    if choice == "1":
        manage_users()  # Add a function to manage users
    elif choice == "2":
        view_reports()  # Function to view reports or other admin-specific tasks
    elif choice == "3":
        print("Logging out...")
        # You can add logic to log out or return to the main menu
    else:
        print("Invalid choice. Returning to main menu...")

def user_menu(username):
    """Displays the user menu options."""
    print("\nUser Menu:")
    print("1. View Profile")
    print("2. Update Profile")
    print("3. Log Out")
    choice = input("Select an option: ")
    
    if choice == "1":
        view_user_profile(username)  # View user profile
    elif choice == "2":
        update_profile(username)  # Update user profile
    elif choice == "3":
        print("Logging out...")
        # Add logic to log out or return to main menu
    else:
        print("Invalid choice. Returning to main menu...")

def manage_users():
    """Function to manage users (only accessible by admin)."""
    print("Managing users...")
    # Implement user management tasks here (add, remove, or edit users)

def view_reports():
    """Function to view reports (only accessible by admin)."""
    print("Viewing reports...")
    # Implement functionality to view reports or other admin tasks

def update_profile(username):
    """Function to update the profile"""
    print(f"Updating profile for {username}")
    # Capture new profile data (gender, province, district, etc.)
    gender = prompts.get_gender()
    province = prompts.get_province()
    district = prompts.get_district()

    # Save the updated profile data
    profile_data = {
        "gender": gender,
        "province": province,
        "district": district
    }

    data_management.save_user_profile(username, profile_data)
    print("Profile updated successfully.")

def capture_profile_info(username):
    """Capture profile information from the user if they don't have one."""
    print(f"Capturing profile information for {username}")
    gender = prompts.get_gender()
    province = prompts.get_province()
    district = prompts.get_district()

    # Save the new profile data
    profile_data = {
        "gender": gender,
        "province": province,
        "district": district
    }

    data_management.save_user_profile(username, profile_data)
    print("Profile created successfully.")
