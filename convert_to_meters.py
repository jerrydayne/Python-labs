
### this program gets feets and inchesfrom the user, converts it to meters and check if the user's hieght meets the standard requirement

feet_and_inches = input("Enter feet and inches (e.g 4 12) : ")

def parse(feet_and_inches):
    spliter = feet_and_inches.split(" ")
    feet = float(spliter[0])
    inches = float(spliter[1])
    return {"feet": feet, "inches":inches}

def convert(feet, inches):
    meter = feet * 0.3048 + inches * 0.0254
    return meter


parsed = parse(feet_and_inches)
result = convert(parsed['feet'], parsed['inches'])

print(f"{parsed['feet']} feet and {parsed['inches']} inches is equal to {result} meters")

if result < 4.75:
    print("heigt is below standard")

else: print("height is within required standard")

