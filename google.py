#!/usr/bin/env python3

import webbrowser, sys

query = " ".join(sys.argv[1:])

print("Searching " + query)
webbrowser.open("https://google.com/search?q=" + query)
