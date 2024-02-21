'''ranking = ['John', 'Sen', 'Lisa']

user_input = input("enter a name to reveal position : ")
user_input = user_input.strip()
rank = ranking.index(user_input)
print(rank + 1)'''




ips = ['100.122.133.105', '100.122.133.111']

for item in ips :
    number = int(input("select the number of IP's to display : "))
    ip = ips[number]
    response = "you chose"
    print(f"{response.capitalize()} {ip}")
    