
### this program gets feets and inchesfrom the user, converts it to meters and check if the user's hieght meets the standard requirement

feet_and_inches = input("Enter feet and inches (e.g 4 12) : ")


def convert(feet_and_inches):
    spliter = feet_and_inches.split(" ")
    feet = float(spliter[0])
    inches = float(spliter[1])

    meter = feet * 0.3048 + inches * 0.0254
    print(f"{feet} feet and {inches} inches is equal to {meter} meters")

    return meter


result = convert(feet_and_inches)

if result < 4.5:
    print("heigt is below standard")

else: print("height is within required standard")

