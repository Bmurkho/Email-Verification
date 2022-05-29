# a-z
# 0-9
# @ 1 time
# . 2nd or 3rd position

import re

email_condition= "^[a-z]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$"

user_email= input("Write an email: ")

if re.search(email_condition, user_email):
    print("Valid email")
else:
    print("Invalid email address")