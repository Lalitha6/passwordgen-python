import string
import random

def password_generator(length=8, upper_case=True, lower_case=True, numbers=True, special_chars=True):
    """
    Generates a random password of specified length.
    """
    password_characters = ""

    if upper_case:
        password_characters += string.ascii_uppercase
    if lower_case:
        password_characters += string.ascii_lowercase
    if numbers:
        password_characters += string.digits
    if special_chars:
        password_characters += string.punctuation

    if len(password_characters) == 0:
        raise ValueError("At least one character type must be selected.")

    password = "".join(random.choice(password_characters) for i in range(length))

    return password

# Example usage
print(password_generator(length=12, upper_case=True, lower_case=True, numbers=True, special_chars=True))
