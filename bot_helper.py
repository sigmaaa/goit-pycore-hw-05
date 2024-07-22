"""
This module provides a simple command-line assistant bot to manage a contacts list.
The bot supports the following commands:
- add <name> <phone>: Adds a new contact with the given name and phone number.
- phone <name>: Retrieves the phone number for the given contact name.
- change <name> <new_phone>: Changes the phone number for the given contact name.
- all: Displays all contacts in the contacts list.
- hello: Greets the user.
- close/exit: Exits the assistant bot.
"""

def parse_input(user_input):
    """
    Parse user input into command and arguments.

    Parameters:
    user_input (str): The input string from the user.

    Returns:
    tuple: A tuple containing the command and a list of arguments.
    """
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def input_error(func):
    """
    Decorator for handling input error
    """
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Error: Command requires exactly 2 arguments (name and phone)."
        except KeyError:
            return "Error: No contact with this name was found in the dictation"
        except IndexError:
            return "Error: Command requires 1 argument (name)"
    return inner

@input_error
def add_contact(args, contacts):
    """
    Add a new contact to the contacts dictionary.

    Parameters:
    args (list): A list of arguments containing the name and phone number.
    contacts (dict): The contacts dictionary.

    Returns:
    str: A message indicating the result of the operation.
    """
    name, phone = args
    contacts[name] = phone
    return "Contact added."

@input_error
def get_number(args, contacts):
    """
    Returns a contact's phone from the dictionary.

    Parameters:
    args (list): A list of arguments containing the name.
    contacts (dict): The contacts dictionary.

    Returns:
    str: A message indicating the result of the operation.
    """
    name = args[0]
    return contacts[name]

@input_error
def change_contact(args, contacts):
    """
    Change the phone number for an existing contact.

    Parameters:
    args (list): A list of arguments containing the name and new phone number.
    contacts (dict): The contacts dictionary.

    Returns:
    str: A message indicating the result of the operation.
    """
    name, new_phone = args
    old_phone = contacts[name] # force failure handled by input_error if no such name is found
    if old_phone:
        contacts[name] = new_phone
    return "Contact updated"

@input_error
def show_all(contacts):
    """
    Show all contacts in the contacts dictionary.

    Parameters:
    contacts (dict): The contacts dictionary.

    Returns:
    str: A formatted string of all contacts.
    """
    if not contacts:
        return "No contacts found."
    result = "\n" + "-" * 30 + "\n"
    result += f"{'Name':<15} {'Phone Number':<15}\n"
    result += "\n" + "-" * 30 + "\n"
    for name, phone in contacts.items():
        result += f"{name:<15} {phone:<15}\n"
        result += "\n"
    return result

def main():
    """
    Main function to run the assistant bot.
    """
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break

        if command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "phone":
            print(get_number(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
