#! python3
# bulletPointAdder.py - Adds user given symbol to the start of each line of text on the clipboard.

import pyperclip

text = pyperclip.paste()
symbol = input("What symbol you would like to add to each line of copied text? (or press Enter to add '*' symbol ")
if symbol == '':
    symbol = '*'
# Separates lines and adds stars.
lines = text.split('\n')
for i in range(len(lines)):     # loops through all indexes in the "lines" list
    lines[i] = symbol + ' ' + lines[i] # adds star to each string in "lines" list
text = '\n'.join(lines)
pyperclip.copy(text)
