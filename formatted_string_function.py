# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring


def greet_user(first_name, last_name):
    result = first_name + " [" + last_name + "] is a coder"
    return result


message = greet_user("John", "Smith")
print(message)
