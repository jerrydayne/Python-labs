todos = []

while True :
    user_action = input("do you want to add, display or exit (add/display/exit): ")
    user_action = user_action.strip()

    match user_action :
        case 'add' :
            todo = input("Add what you want todo : ")
            todos.append(todo)
        case 'display' | 'show':
            for item in todos :
                item = item.title()
                print(item)
        case 'exit' :
            break
#        case something_else :
#            print("this is an unknown selection, check again")

print("Thanks for coming!")