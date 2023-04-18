"""Logical Operators
"""
HAS_HIGHT_INCOME = True
HAS_GOOD_CREDIT = False

if HAS_GOOD_CREDIT and HAS_HIGHT_INCOME:
    print("Eligible for loan")
if HAS_GOOD_CREDIT or HAS_HIGHT_INCOME:
    print("Eligible for loan")
HAS_GOOD_CREDIT = True
HAS_CRIMINAL_RECORD = True
if HAS_GOOD_CREDIT and not HAS_CRIMINAL_RECORD:
    print("Eligible for loan. Not criminal")
