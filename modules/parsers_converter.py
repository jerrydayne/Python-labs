def parse(feet_and_inches):
    spliter = feet_and_inches.split(" ")
    feet = float(spliter[0])
    inches = float(spliter[1])
    return {"feet": feet, "inches":inches}