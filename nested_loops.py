"""
Nested Loops
"""


# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
def nested_loops(xxx, yyy):
    for row in range(xxx):
        for item in range(yyy):
            print(f"({row}, {item})")


nested_loops(4, 3)
