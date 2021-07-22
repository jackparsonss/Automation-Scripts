#!/usr/bin/env python3

"""
Please enter the filename as a command line argument

This command will take in a .docx file and copy the text into the users clipboard
"""

import docx, sys, pyperclip

try:
    if len(sys.argv) < 2:
        raise Exception("Please give the file as an argument")

    filename = sys.argv[1]

    doc = docx.Document(filename)
    text = []

    for paragraph in doc.paragraphs:
        text.append(" " + paragraph.text)

    pyperclip.copy("\n".join(text))


except Exception as e:
    print(e)
