import sys


def get_user_input(message):
    # Support Python 2
    if sys.version_info >= (3, 0):
        return input(message)
    else:
        return raw_input(message)


def wants_to_replace():
    choice = get_user_input(
        "There is already a project with that name.\n"
        "Do you want to replace it? (Y/N) "
    ).lower()
    while choice not in ["y", "n"]:
        choice = get_user_input(
            "Invalid input. Please try again.\n"
            "Do you want to replace it? (Y/N) "
        ).lower()
    return choice == "y"
