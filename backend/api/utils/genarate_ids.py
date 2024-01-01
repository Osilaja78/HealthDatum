# This module contains logic to generating unique ids.
import secrets
import string


def generate_short_id(length=6):
    """
    Generates short unique identifiers.

    Parameters:
        lenght: lenght of the id (optional)
    
    Return: random_id (generated random id)
    """

    # Define the characters to use in the ID (alphanumeric)
    characters = string.ascii_letters + string.digits
    
    # Generate a random ID of the specified length
    random_id = ''.join(secrets.choice(characters) for _ in range(length))
    
    return random_id
