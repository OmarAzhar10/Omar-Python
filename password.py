import random
import string

# Function to generate a random password
def generate_password(length):
    # All possible characters: letters, digits, and punctuation
    characters = string.ascii_letters + string.digits + string.punctuation
    # Randomly pick 'length' characters
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Example usage
password_length = int(input("Enter password length: "))
generated_password = generate_password(password_length)
print(f"Your random password is: {generated_password}")
