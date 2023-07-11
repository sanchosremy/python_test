def get_temperature_desc(hot_temperatue):
    if hot_temperatue > 30:
        print("It's a hot day")
    else:
        print("It's not a hot day")


def check_name_length(username):
    if len(username) < 3:
        print("Name must be at least 3 charahters.")
    elif len(username) > 50:
        print("Name must be a maximum of 50 characters")
    else:
        print("Name looks good!")
