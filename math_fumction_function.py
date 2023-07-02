import math


def get_round(number):
    result = round(number)
    return result


total = get_round(2.9)
print(total)


def get_abs(number):
    result = abs(number)
    return result


total = get_abs(2.9)
print(total)


def get_ceil(number):
    result = math.ceil(number)
    return result


total = get_ceil(2.9)
print(total)


def get_floor(number):
    result = math.floor(number)
    return result


total = get_floor(2.9)
print(total)
