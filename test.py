ranking = ['John', 'Sen', 'Lisa']

user_input = input("enter a name to reveal position : ")
user_input = user_input.strip()
rank = ranking.index(user_input)
print(rank + 1)