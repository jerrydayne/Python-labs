password = input("Enter password : ")

result = {}

#check if password length is greater or equal to 8
if len(password) >= 8 :
    result["length"] = True
else :
    result["length"] = False

#checkig if password contains a digit
digit = False
for character in password :
    if character.isdigit() :
        digit = True
result["digit"] = digit

#checking if password contains an uppercase
uppercase = False
for character in password :
    if character.isupper() :
        uppercase = True
result["uppercase"] = uppercase

"""
print(result)
print(result.values())
"""

#checking if all conditions are true/password is strong or weak
if all(result.values()) :
    print("Password is strong")
else :
    print("Password is weak")