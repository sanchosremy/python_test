def credit(has_good_credit, has_hight_income):
    has_good_credit = True
    has_hight_income = False
    if has_good_credit and has_hight_income:
        print("Eligible for loan")
    if has_good_credit or has_hight_income:
        print("Eligible for loan")
    has_good_credit = True
