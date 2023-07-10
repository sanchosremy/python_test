def your_bio(name, favorite_color, birth_year, age):
    print(name + "likes" + favorite_color, age)
    age = 2023 - int(birth_year)
    print(age)


def weight_conversion(weight_lbs):
    weight_kg = int(weight_lbs) * 0.45
    print(weight_kg)
