# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
"""Emojis conventer

"""
message = input(">")
words = message.split(" ")
emojis = {":)": "😃", ":(": "😔"}
OUTPUT = ""
for item in words:
    OUTPUT += emojis.get(item, item) + " "
print(OUTPUT)
