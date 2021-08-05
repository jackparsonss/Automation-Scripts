#!/usr/bin/env python3

import shutil, os

"""
This program will take any files in my downloads folder and move
it into my trash
"""


def main():
    source_path = "/Users/jackparsons/Downloads/"
    destination_path = "/Users/jackparsons/.Trash"

    files = os.listdir(source_path)

    for file in files:
        print(f"Moving {file} into trash")
        shutil.move(source_path + file, destination_path + file)


if __name__ == "__main__":
    main()
