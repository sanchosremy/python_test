"""Formatted Strings
"""
NAME = "Jennifer"
print(NAME[1:0])
FIRST_NAME = "John"
LAST_NAME = "Smith"
MESSAGE = FIRST_NAME + " [" + LAST_NAME + "] is a coder"
print(MESSAGE)
MESSAGE = f"{FIRST_NAME}  [{LAST_NAME}]  is a coder"
print(MESSAGE)
