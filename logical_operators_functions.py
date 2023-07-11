def get_credit_rating(has_good_credit, has_hight_income):
    if has_good_credit and has_hight_income:
        print("Eligible for loan")
    if has_good_credit or has_hight_income:
        print("Eligible for loan")
