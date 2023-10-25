
def get_formatted_profesion(profesion):
    result = (profesion.replace("[", "(").replace("]", ")"))
    result = (result.replace("[Smith]", "(Smith)"))
    return result


print(get_formatted_profesion("John [Smith] is a coder"))
