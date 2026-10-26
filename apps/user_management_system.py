"""Interactive user management system with in-memory storage."""

import os

# In-memory records used to store user data.
hashed_passwords = {}
user_id_counter = 1
users = {}


def clear_terminal():
    """Clear the terminal screen based on the operating system."""
    os.system("cls" if os.name == "nt" else "clear")


class User:
    """Represents a user record in the system."""

    def __init__(self, first_name, last_name, email, password, user_id, status="inactive"):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.status = status
        self.user_id = user_id

    def display_info(self):
        """Print the user's stored information in a readable format."""
        print(f"First Name: {self.first_name}")
        print(f"Last Name: {self.last_name}")
        print(f"Email: {self.email}")
        print(f"Password: {hashed_passwords[self.user_id]}")
        print(f"User ID: {self.user_id}")
        print(f"Status: {self.status}")
        print("=" * 30)


def hash_password(password):
    """Return a masked version of the password for display purposes."""
    return "*" * len(password)


def create_user():
    """Prompt for a new user's details and create the record."""
    global user_id_counter

    while True:
        clear_terminal()
        first_name = input("Enter first name: ").strip().capitalize()
        last_name = input("Enter last name: ").strip().capitalize()
        email = input("Enter email: ").strip()
        password = input("Enter password: ").strip()

        if not password:
            input("Error: Password cannot be empty. Please enter a valid password.")
            continue

        status = input("Enter status [active/inactive] (default = \"inactive\"): ").strip().lower()
        if status not in ["active", "inactive", ""]:
            print("Error: Invalid input. Please type \"active\" or \"inactive\" (or press 'Enter' for default = \"inactive\").")
            input("Press 'Enter' to continue...")
            continue

        status = status if status else "inactive"
        user_id = user_id_counter
        user_id_counter += 1
        hashed_passwords[user_id] = hash_password(password)
        print("\nUser created successfully!")
        break

    return User(first_name, last_name, email, password, user_id, status)


def display_all_users():
    """Display every user currently stored in the system."""
    if users:
        print("\n============== All Users ==============\n")
        for user in users.values():
            user.display_info()
    else:
        print("\n============== No users found ==============\n")


def search_user_by_id(user_id):
    """Display a user whose ID matches the given value."""
    user = users.get(user_id)
    if user:
        print("User found:\n")
        user.display_info()
    else:
        print("Error: User not found.")


def search_user_by_first_name(first_name):
    """Display all users whose first name matches the input."""
    found = False
    for user in users.values():
        if user.first_name.lower() == first_name.lower():
            user.display_info()
            found = True

    if not found:
        print("Error: No users found with that first name.")


def search_user_by_status(status):
    """Display all users whose status matches the input."""
    found = False
    for user in users.values():
        if user.status.lower() == status.lower():
            user.display_info()
            found = True

    if not found:
        print("Error: No users found with that status.")


def search_user_by_email(email):
    """Display the user whose email matches the input."""
    found = False
    for user in users.values():
        if user.email.lower() == email.lower():
            user.display_info()
            found = True

    if not found:
        print("Error: No users found with that email.")


def main():
    """Display the main menu and handle the user's actions."""
    while True:
        clear_terminal()
        print("=========== Welcome To User Management ===========\n")
        try:
            action = int(input("\nChoose an Action:\n1. Add new user\n2. Display all users\n3. Search for a user\n4. Exit the program\n"))
        except ValueError:
            print("Error: Please enter a valid action number.")
            input("Press 'Enter' to continue...")
            continue

        clear_terminal()

        if action == 1:
            user = create_user()
            users[user.user_id] = user
            input("\nUser added successfully! Press 'Enter' to continue...")

        elif action == 2:
            display_all_users()
            input("Press 'Enter' to continue...")

        elif action == 3:
            while True:
                clear_terminal()
                try:
                    search_action = int(input(
                        "Search by:\n\n1. User ID\n2. First Name\n3. Status\n4. Email\n5. Go back\n6. Exit the program\n\nEnter the action number: "))
                    if search_action <= 0 or search_action > 6:
                        input("Error: Please enter a valid action number.")
                        continue
                except ValueError:
                    input("Error: Please enter a valid number.")
                    continue

                if search_action == 1:
                    try:
                        user_id_to_search = int(input("Enter the user's ID: "))
                        search_user_by_id(user_id_to_search)
                    except ValueError:
                        input("Error: Please enter a valid number.")
                    input("Press 'Enter' to continue...")

                elif search_action == 2:
                    first_name_to_search = input("Enter the user's first name: ").strip()
                    search_user_by_first_name(first_name_to_search)
                    input("Press 'Enter' to continue...")

                elif search_action == 3:
                    status_to_search = input("Enter the user's status (active/inactive): ").strip().lower()
                    if status_to_search not in ["active", "inactive"]:
                        input("Error: Invalid status. Please enter either 'active' or 'inactive'.")
                        continue
                    search_user_by_status(status_to_search)
                    input("Press 'Enter' to continue...")

                elif search_action == 4:
                    email_to_search = input("Enter the user's email: ").strip()
                    search_user_by_email(email_to_search)
                    input("Press 'Enter' to continue...")

                elif search_action == 5:
                    break

                elif search_action == 6:
                    print("\nExiting the program...")
                    exit()

        elif action == 4:
            print("\nExiting the program...")
            exit()

        else:
            input("Error: Please enter a valid action number.\nPress 'Enter' to continue...")


if __name__ == "__main__":
    main()
