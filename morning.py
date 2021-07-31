#!/usr/bin/env python3

import subprocess, pyautogui, time, GetMediumArticles

"""
This script is intended for me to run first thing in the morning to automate all 
the apps and things I have to do after waking up
"""


def open_obsidian_daily_note():
    article_outputer = GetMediumArticles.GetMediumArticles()
    print("\nWaiting for obsidian to open to open daily note\n")
    time.sleep(7)
    pyautogui.hotkey("shift", "option", "D")

    pyautogui.hotkey("command", "shift", "I")

    pyautogui.press(["d", "a", "i", "l", "y"])
    pyautogui.press(["enter"])

    # Fetches medium articles and add their links to the bottom of the daily note
    time.sleep(1)
    print("Fetching Medium Articles")
    article_outputer.run()


def main():
    print("☀️ Good Morning Jack!!\n")

    apps = ["Day One", "Todoist", "Spark", "Obsidian"]

    for app in apps:
        print(f"Opening {app}!")
        subprocess.Popen(["open", f"/Applications/{app}.app"])

        if app == "Obsidian":
            open_obsidian_daily_note()
        elif app == "Day One":
            # allow app to open
            time.sleep(2)

    print("\n⚡️All Done, Have a Productive Morning⚡️")


if __name__ == "__main__":
    main()
