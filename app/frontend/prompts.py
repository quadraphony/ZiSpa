def get_username():
    """Prompt the user to enter their username."""
    username = input("Enter your username: ")
    return username

def get_password():
    """Prompt the user to enter their password."""
    password = input("Enter your password: ")
    return password

def get_role():
    """Prompt the user to select a role during signup (optional)."""
    print("Select your role:")
    roles = ['admin', 'spa_owner', 'user']
    for i, role in enumerate(roles, 1):
        print(f"{i}. {role}")
    choice = int(input("Enter the number of your role: ")) - 1
    return roles[choice]

def get_gender():
    """Prompt the user to enter their gender."""
    print("Select your gender:")
    genders = ['male', 'female', 'other']
    for i, gender in enumerate(genders, 1):
        print(f"{i}. {gender}")
    choice = int(input("Enter the number of your gender: ")) - 1
    return genders[choice]

def get_province(provinces):
    """Prompt the user to select their province."""
    print("Select your province:")
    for i, province in enumerate(provinces, 1):
        print(f"{i}. {province['ProvinceName']}")
    choice = int(input("Enter the number of your province: ")) - 1
    selected_province = provinces[choice]
    return selected_province

def get_district(province, districts):
    """Prompt the user to select their district from a specific province."""
    print(f"Select your district in {province['ProvinceName']}:")
    available_districts = [district for district in districts if district['ProvincePCode'] == province['ProvincePCode']]
    for i, district in enumerate(available_districts, 1):
        print(f"{i}. {district['DistrictName']}")
    choice = int(input("Enter the number of your district: ")) - 1
    selected_district = available_districts[choice]
    return selected_district

def ask_update_profile():
    """Ask the user if they want to update their profile after login."""
    update = input("Would you like to update your profile? (y/n): ").lower()
    if update == 'y':
        return True
    return False
