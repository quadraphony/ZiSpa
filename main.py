from app.backend import auth, data_management
from app.frontend import user_interface
from app.config import settings

def main():
    print("Welcome to ZiSpa!")
    user_choice = user_interface.get_user_choice()

    if user_choice == "1":
        auth.login()
        # After login, check if the user has a profile
        username = input("Enter your username to check profile: ")
        if data_management.user_exists(username):
            # Ask if they want to update their profile
            if user_interface.ask_update_profile():
                # Capture and update the profile info
                # Assuming you've added a function to update the profile
                update_profile(username)
            else:
                print("Profile remains unchanged.")
        else:
            print("No profile found. Please complete your profile.")
            capture_profile_info(username)
            
    elif user_choice == "2":
        auth.signup()
    else:
        print("Invalid choice! Exiting...")

def capture_profile_info(username):
    """Collect additional profile information if no profile exists."""
    gender = user_interface.get_gender()
    # Assuming we have the function to capture province and district
    provinces = load_provinces_data()  # This should be your logic to load provinces
    province = user_interface.get_province(provinces)
    district = user_interface.get_district(province, load_districts_data())  # Similarly, districts
    # Save the profile to the user data
    data_management.add_user_profile(username, gender, province, district)
    print(f"Profile for {username} has been created.")

def update_profile(username):
    """Update the user's profile information."""
    # This function can capture any necessary updates (e.g., gender, province, district)
    gender = user_interface.get_gender()
    provinces = load_provinces_data()
    province = user_interface.get_province(provinces)
    district = user_interface.get_district(province, load_districts_data())
    # Assuming you have logic for updating user profiles
    data_management.update_user_profile(username, gender, province, district)
    print(f"Profile for {username} has been updated.")

if __name__ == "__main__":
    main()
