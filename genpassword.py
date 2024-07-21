import string
import random
def generate_password(length):
    if length < 4:
        raise ValueError("Password length should be at least 4 or more to include all character types.")

    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    special_chars = string.punctuation 

    password = [
        random.choice(lowercase_letters),
        random.choice(uppercase_letters),
        random.choice(digits),
        random.choice(special_chars)
    ]

    all_characters = lowercase_letters + uppercase_letters + digits + special_chars
    password += [random.choice(all_characters) for _ in range(length - 4)]

    random.shuffle(password)
    return ''.join(password)

def main():
    try:
        length = int(input("Enter the desired length of the password:"))

        password = generate_password(length)
        print("Generated Password:", password)
    except ValueError as e:
        print(e)
if __name__ == "__main__":
    main()