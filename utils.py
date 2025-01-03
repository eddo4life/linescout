from colorama import Fore, Style

def print_error(message):
    """
    Prints the given message in red to indicate an error.

    Args:
        message (str): The error message to be printed.
    """
    print(Fore.RED + str(message) + Style.RESET_ALL)

def print_success(message):
    """
    Prints the given message in green to indicate a success message.
    
    Args:
        message (str); The success message to be printed.
    """
    print(Fore.GREEN + str(message) + Style.RESET_ALL)