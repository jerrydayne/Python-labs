date = input("enter today's date (YY-MM-DD) : ")
mood = input("From 1 to 10, how would you rate your mood? : ")
details = input("What really happened today ? : ")

with open(f"journals_app/journals/{date}.txt", "w") as file :
    file.write(mood + 2 * "\n")
    file.write(details)