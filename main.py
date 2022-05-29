email= input("Enter your email: ")
error= False
if len(email)>5:
    if email[0].isalpha():
        if ("@" in email) and (email.count("@")==1):
            if (email[-4]==".")^(email[-3]=="."):
                for digit in email:
                    if digit== digit.isspace():
                        error= True
                    elif digit.isalpha():
                        if digit==digit.upper():
                            error= True
                    elif digit.isdigit():
                        continue
                    elif digit=="." or digit=="@" or digit== "_":
                        continue
                    else:
                        error= True

                if error:
                    print("This is not a valid email")
                else:
                    print("Valid Email")

        else:
            print("This is not a valid email 3")
    else:
        print("This is not a valid email 2")
else:
    print("This is not a valid email 1")
