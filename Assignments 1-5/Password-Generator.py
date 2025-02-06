"""
Script that will randomly generate password based on the criteria input
"""

import secrets
import string



# function to get criteria for password
def get_criteria():

    characters = ''

    uppercase_letters = input("would you like to use uppercase letters? y/n ").strip().lower()
    if uppercase_letters == "y":
        characters += string.ascii_uppercase
    else:
        print("ok no uppercase")

    lowercase_letters = input("would you like to use lowercase letters? y/n ").strip().lower()
    if lowercase_letters == "y":
        characters += string.ascii_lowercase
    else:
        print("ok no lowercase")

    numbers_included = input("would you like to include numbers? y/n ").strip().lower()
    if numbers_included == "y":
        characters += string.digits
    else:
        print("ok no numbers")

    special_characters = input("would you like to use special characters? y/n ").strip().lower()
    if special_characters == "y":
        characters += string.punctuation
    else:
        print("ok no special characters")

    while True:
        password_length = int(input("how long would you like the password to be? "))
        if password_length >= 8:
            break
        elif password_length < 8:
            print("I'm sorry that password is too short")
    return characters, password_length


# function that will generate the password
def generate_password(characters, password_length):

    return ''.join(secrets.choice(characters) for _ in range(password_length))

# main function to run
def main():
    while True:
        characters, password_length = get_criteria()
        password = generate_password(characters, password_length)
        print(f"\n Generated password: {password}\n")

        retry = input("Generate another password? y/n ").strip().lower()
        if retry != "y":
            print("goodbye")
            break

main()
