#! python3
# bulletPointAdder.pyw - Adds bullet points to the start of each line of text from the clipboard

import sys, pyperclip


def bulleted():
    # get clipboard
    text = pyperclip.paste()

    text_list = text.split("\n")

    for i in range(len(text_list)):
        text_list[i] = "- " + text_list[i]

    text = "\n".join(text_list)

    # send clipboard
    pyperclip.copy(text)


def numbered():
    # get clipboard
    text = pyperclip.paste()

    text_list = text.split("\n")

    for i in range(len(text_list)):
        text_list[i] = f"{i+1}. " + text_list[i]

    text = "\n".join(text_list)

    # send clipboard
    pyperclip.copy(text)


if len(sys.argv) > 1:
    if sys.argv[1].lower() == "numbered":
        numbered()
else:
    bulleted()
