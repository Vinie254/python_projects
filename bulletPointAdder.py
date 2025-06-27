#! python3
#This code adds numbering to a list that doesnt have any.Copy the list first, run the script and then paste into where its needed.😃
import sys

import pyperclip
def numbering():
    text = pyperclip.paste()
    lines = text.split('\n')
    for i in range(len(lines)):
        lines[i] = f"{i + 1}. {lines[i]}"

    text = '\n'.join(lines)
    pyperclip.copy(text)
def asterisk():
    text = pyperclip.paste()
    lines = text.split('\n')
    for i in range(len(lines)):
        lines[i] = f"{'*'}{lines[i]}"

    text = '\n'.join(lines)
    pyperclip.copy(text)

user_choice = input("Choose which order method to use( * or 1 for numbering): ")
if user_choice == "*":
    asterisk()
elif user_choice == "1":
    numbering()
else:
    print("Invalid input")
    sys.exit()
