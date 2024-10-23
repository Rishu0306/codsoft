import random
import string

def generate_password(length=12):
    if length < 4:
        raise ValueError("Password length should be at least 4 characters.")

    # Define the character sets to choose from
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    special_characters = string.punctuation

    # Ensure the password contains at least one of each character type
    password = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(digits),
        random.choice(special_characters),
    ]

    # Fill the rest of the password length with random choices
    all_characters = lowercase + uppercase + digits + special_characters
    password += random.choices(all_characters, k=length - 4)

    # Shuffle the created password list to ensure randomness
    random.shuffle(password)

    # Join the list into a string and return
    return ''.join(password)

# Example usage
if __name__ == "__main__":
    password_length = 12  # You can change the length here
    print("Generated password:", generate_password(password_length))
