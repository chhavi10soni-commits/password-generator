import random
import string

# function to generate password
def generate_password(length=12, use_uppercase=True, use_lowercase=True,
                      use_digits=True, use_symbols=True):

    characters = ""

    if use_uppercase:
        characters += string.ascii_uppercase
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += "!@#$%^&*"

    if characters == "":
        print("Select at least one option!")
        return ""

    password = ""
    for i in range(length):
        password += random.choice(characters)

    return password


# function to check strength
def check_strength(password):
    length = len(password)

    if length < 8:
        return "Weak"
    elif length < 12:
        return "Moderate"
    else:
        if any(c.isdigit() for c in password) and any(c.isalpha() for c in password):
            return "Strong"
        else:
            return "Moderate"


# main program
print("---- Password Generator ----")

length = int(input("Enter password length: "))
count = int(input("How many passwords: "))

choice = input("Include symbols? (y/n): ")
use_symbols = True if choice.lower() == 'y' else False

for i in range(count):
    pwd = generate_password(length, use_symbols=use_symbols)
    strength = check_strength(pwd)
    print(f"{i+1}. {pwd}  ->  {strength}")