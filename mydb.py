#!/usr/bin/env python3

import shelve, pyperclip, sys


class App:
    def __init__(self, shelve):
        self.shelve = shelve
        self.options = {
            "LIST": self.list,
            "GET": self.get,
            "SAVE": self.save,
            "DELETE": self.delete,
            "SHOW": self.show,
        }

    def run(self):
        """
        Entry point to app
        """
        self.options[sys.argv[1].upper()]()

    def list(self):
        """
        Displays all keys in db
        >>> mydb.py show
        """
        print("Keys Stored In Vault:")
        for key in self.shelve.keys():
            print("-", key)

    def get(self):
        """
        Copies value from given key
        >>> mydb.py get key
        """
        pyperclip.copy(self.shelve[sys.argv[2]])

    def save(self):
        """
        Creates a new key value pair of the given key and what is on the users clipboard
        >>> mydb.py save key
        """
        self.shelve[sys.argv[2]] = pyperclip.paste()

    def delete(self):
        """
        Deletes key value pair of given key
        >>> mydb.py delete key
        """
        self.shelve.pop(sys.argv[2])

    def show(self):
        """
        Displays value stored at given key
        >>> mydb.py show key
        """
        print(self.shelve[sys.argv[2]])


def main():
    with shelve.open("mydb") as mydb_shelf:
        try:
            app = App(mydb_shelf)
            app.run()
        except:
            print("Key Not Found")


if __name__ == "__main__":
    main()
