todos = []

while True :
    user_action = input("do you want to add, display, edit, complete or exit (add/display/exit): ")
    user_action = user_action.strip()

    match user_action :
        case 'add' :
            todo = input("Add what you want todo : ") + "\n"
            todos.append(todo)
            file = open('todos.txt', 'w')
            file.writeline(todos)
        case 'display' | 'show':
            for index, item in enumerate(todos) :
                item = item.title()
                item_row = f"{index + 1}.{item}"
                print(item_row)
        case 'edit' :
            todo_serial_number = int(input("enter the serial number of the item to edit : "))
            todo_serial_number = todo_serial_number - 1
            new_todo = input("Enter new task")
            todos[todo_serial_number] = new_todo
            print(todos[todo_serial_number], "is replaced with ", new_todo)
        case 'complete' :
             todo_serial_number = int(input("enter the serial number of the item to complete : "))
             todos.pop(todo_serial_number -1)
        case 'exit' :
            break
        case something_else :
            print("this is an unknown selection, check again")

print("Thanks for coming!")