import string
import random

def generate_password(length):
    """Generate a random password of specified length."""
    # Define the characters that can be used in the password
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Generate the password by randomly selecting characters
    password = ''.join(random.choice(characters) for i in range(length))
    
    return password

# Prompt the user for input
password_length = int(input("Enter the desired length of the password: "))

# Generate the password and print it out
password = generate_password(password_length)
print("Generated password:",password)
