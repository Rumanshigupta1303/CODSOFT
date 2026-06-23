import random
import string
print("=== Password Generator ===")
length = int(input("Enter password length: "))
use_letters = input("Include letters? (yes/no): ")
use_numbers = input("Include numbers? (yes/no): ")
use_symbols = input("Include symbols? (yes/no): ")
characters = ""
if use_letters.lower() == "yes":
    characters += string.ascii_letters
if use_numbers.lower() == "yes":
    characters += string.digits
if use_symbols.lower() == "yes":
    characters += string.punctuation
if characters == "":
    print("Please select at least one option!")
else:
    password = ""
    for i in range(length):
        password += random.choice(characters)
    print("Generated Password:", password)
