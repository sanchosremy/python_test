"""Lists
"""
numbers = [13, 4, 67, 43, 2]
MAX_NUMBER = numbers[0]
for number in numbers:
    if number > MAX_NUMBER:
        MAX_NUMBER = number
print(MAX_NUMBER)
