# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
"""Dictionaries

"""
phone = input("Phone :")
translate_number = {"1": "One ", "2": "Two ", "3": "Three ", "4": "Four "}
OUTPUT = ""
for item in phone:
    OUTPUT += str(translate_number.get(item))
print(OUTPUT)
