#!/usr/bin/env python3
# refer to Automate The Boring Stuff With Python Chapter 9 For Usage

import shelve, pyperclip, sys


def check_word(word):
    return sys.argv[1].lower() == word


def show_list(shelve):
    if check_word("list"):
        pyperclip.copy(str(list(shelve.keys())))
        print("Keys Stored In Vault:")
        for key in shelve.keys():
            print("-", key)


def run_options(shelve):
    if check_word("get"):
        pyperclip.copy(shelve[sys.argv[2]])

    elif check_word("save"):
        shelve[sys.argv[2]] = pyperclip.paste()

    elif check_word("delete"):
        shelve.pop(sys.argv[2])

    elif check_word("show"):
        print(shelve[sys.argv[2]])


def app(shelve):
    if len(sys.argv) == 3:
        run_options(shelve)
    elif len(sys.argv) == 2:
        show_list(shelve)


def main():
    with shelve.open("mydb") as mydb_shelf:
        try:
            app(mydb_shelf)
        except:
            print("Key Not Found")


if __name__ == "__main__":
    main()
