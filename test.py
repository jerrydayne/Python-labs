'''ranking = ['John', 'Sen', 'Lisa']

user_input = input("enter a name to reveal position : ")
user_input = user_input.strip()
rank = ranking.index(user_input)
print(rank + 1)'''




"""ips = ['100.122.133.105', '100.122.133.111']

for item in ips :
    number = int(input("select the number of IP's to display : "))
    ip = ips[number]
    response = "you chose"
    print(f"{response.capitalize()} {ip}")"""
    

"""
    Take a look at the essay.txt file tab. That file contains some text.

You should create a program that reads the essay.txt file, converts the first letter of each word to uppercase and prints out the converted text.
    """
"""
user_input = 'snail'
file_writer = open('file.txt', 'w')
file_writer.writelines(user_input)
file_writer.close()
"""

"""names = ["john smith", "jay santi", "eva kuki"]
names = [name.title() for name in names]
print(names)"""

"""usernames = ["john 1990", "alberta1970", "magnola2000"]
size = [len(username) for username in usernames]
print(size)"""

"""letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(letters[1:4])"""

"""
try:
    total_value = float(input("Enter total value: "))
    if total_value == 0 :
        exit("Your total value cannot be zero")
    value = float(input("Enter value: "))
    
    percentage = float((value/total_value) * 100) 
    print(f"That is {percentage}%")
    
except ValueError:
    print("You need to enter a number. Run the program again.")
"""

"""
colors = [11, 34, 98, 43, 45, 54, 54]

for number in colors :
    if number > 50 :
        print(number)
"""

def get_max():
    grades = [9.6, 9.2, 9.7]
    Max = max(grades)

    Min = min(grades)

    result = f"Max: {Max}, Min: {Min}"

    return result

print(get_max())

