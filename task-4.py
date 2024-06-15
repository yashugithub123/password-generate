import random
import string


def generate_password(length):
    """

    Generate a random password of specified length.


    Args:

    - length (int): Length of the password to generate


    Returns:

    - str: Generated password
    """

    if length < 12:

        raise ValueError("Password length should be at least 12 for better security")


    uppercase_letters = string.ascii_uppercase

    lowercase_letters = string.ascii_lowercase

    digits = string.digits

    special_characters = string.punctuation


    # Ensure at least one character from each category

    password_chars = [

        random.choice(uppercase_letters),

        random.choice(lowercase_letters),

        random.choice(digits),

        random.choice(special_characters)

    ]


    # Fill the rest of the password with random characters

    password_chars += random.choices(uppercase_letters + lowercase_letters + digits + special_characters, k=length - 4)
    

    # Shuffle the characters to mix them up

    random.shuffle(password_chars)
    

    # Convert list to string

    password = ''.join(password_chars)
    
    return password


def main():
    """

    Main function to interact with the user for generating passwords.
    """

    print("Welcome to the Strong Password Generator!")

    try:

        num_passwords = int(input("Enter the number of passwords to generate: "))

        password_length = int(input("Enter the length of each password (minimum 12): "))
        

        if num_passwords <= 0 or password_length < 12:

            raise ValueError("Number of passwords should be positive and password length should be at least 12.")

        jls_extract_var = print
        jls_extract_var("\nGenerated Passwords:")

        for _ in range(num_passwords):
            print(generate_password(password_length))


    except ValueError as ve:

        print(f"Error: {ve}")

    except Exception as e:

        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()