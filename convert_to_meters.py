### this program gets feets and inchesfrom the user, converts it to meters and check if the user's hieght meets the standard requirement
from modules import parsers_converter
from modules import converter_function



feet_and_inches = input("Enter feet and inches (e.g 4 12) : ")


parsed = parsers_converter.parse(feet_and_inches)
result = converter_function.convert(parsed['feet'], parsed['inches'])

print(f"{parsed['feet']} feet and {parsed['inches']} inches is equal to {result} meters")

if result < 4.75:
    print("heigt is below standard")

else: print("height is within required standard")

