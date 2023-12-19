# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-module-docstring
def calculate_division(first_number, second_number):
    result = first_number / second_number
    return result


TOTAL = calculate_division(10, 3)
print(TOTAL)


def calculate_floor_division(first_number, second_number):
    result = first_number // second_number
    return result


TOTAL = calculate_floor_division(10, 3)
print(TOTAL)


def calculate_modulus(first_number, second_number):
    result = first_number % second_number
    return result


TOTAL = calculate_modulus(10, 3)
print(TOTAL)


def calculate_exponentiation(first_number, second_number):
    result = first_number**second_number
    return result


TOTAL = calculate_exponentiation(10, 3)
