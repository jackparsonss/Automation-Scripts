#!/usr/bin/env python3
# User passes in the length of desired password and an autogenerated password is copied to users clipboard
import string, pyperclip, random, sys

try:
    # Retrieve length of desired password
    if len(sys.argv) > 1:
        try:
            length = int(sys.argv[1])
        except:
            print("Please enter a length or leave blank for default length")
    else:
        length = 16

    # Generate password
    letters = string.ascii_letters
    numbers = string.digits
    symbols = string.punctuation
    options = letters + numbers + symbols

    if length > len(options):
        raise ValueError("Please give a shorter length")

    password_chars = random.sample(options, length)
    password = "".join(password_chars)

    # Copy password to clipboard
    pyperclip.copy(password)
    print("New Password Copied To Clipboard!")

except Exception as e:
    print(e)
