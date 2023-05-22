# pylint: disable=missing-function-docstring
"""
Variables
"""
print("Mosh Hamedani")
print("o----")
print("||||")
print("*" * 10)
PRICE = 10
PRICE = 20
print(PRICE)
nums = [12, 54, 34]
print(max(nums))
print(min(nums))
AUGUSTIN = False
ALEXANDRE = True
print(AUGUSTIN)
print(AUGUSTIN + ALEXANDRE)
DENIS = 9
ANASTASIA = 5
TOTAL = DENIS + ANASTASIA
print(TOTAL)
FIRST_NAME = "John"
LAST_NAME = "Smith"
FULL_NAME = FIRST_NAME + " " + LAST_NAME
print(FULL_NAME)


def get_full_name(first_name, last_name):
    full_name = first_name + last_name
    return full_name


RESULT = get_full_name("ALEXANDRE ", "REMY")
print(RESULT)
