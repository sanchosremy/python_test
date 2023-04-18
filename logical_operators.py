"""Logical Operators
"""
HAS_HIGHT_INCOME = True
HAS_GOOD_CREDIT = False

if HAS_GOOD_CREDIT and HAS_HIGHT_INCOME:
    print("Eligible for loan")
if HAS_GOOD_CREDIT or HAS_HIGHT_INCOME:
    print("Eligible for loan")
HAS_GOOD_CREDIT = True
HAS_CRIMINAL_RECORD = False
