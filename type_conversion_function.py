# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
def get_age_from_year(birth_year):
    age = 2023 - int(birth_year)
    return age


def weight_kg_conversion_from_lbs(weight_lbs):
    weight_kg = int(weight_lbs) * 0.45
    return weight_kg
