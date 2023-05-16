"""Exceptions
"""
try:
    AGE = int(input("Age: "))
    INCOME = 20000
    risk = INCOME / AGE
    print(AGE)
except ZeroDivisionError:
    print("Age cannot be 0.")
except ValueError:
    print("Invalid value")
