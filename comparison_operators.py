"""Comparison Operators
"""
TEMPERATURES = 30
if TEMPERATURES > 30:
    print("It's a hot day")
else:
    print("It's not a hot day")
NAME = "J"
if len(NAME) < 3:
    print("Name must be at least 3 charchters.")
elif len(NAME) > 50:
    print("Name must be a maximum of 50 characters.")
else:
    print("Name looks good!")
