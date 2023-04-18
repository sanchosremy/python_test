"""Strings method
"""
FIRST_NAME = "John"
LAST_NAME = "Smith"
PROFESION = FIRST_NAME + " [" + LAST_NAME + "] is a coder"
print(PROFESION)
PROFESION = f"{FIRST_NAME}  [{LAST_NAME}]  is a coder"
print(PROFESION)
print(len(PROFESION))
print(PROFESION.upper())
print(PROFESION.lower())
print(PROFESION.find("c"))
print(PROFESION.replace("[", "(").replace("]", ")"))
print(PROFESION.replace("[Smith]", "(Smith)"))
