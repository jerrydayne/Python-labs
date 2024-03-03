while True :
    user_action = input("do you want to add, display, edit, complete or exit (add/display/exit): ")
    user_action = user_action.strip()

    match user_action :
        case 'add' :
            todo = input("Add what you want todo : ") + "\n"

            file_reader = open('files/todos.txt', 'r')
            todos = file_reader.readlines()
            file_reader.close()

            todos.append(todo)
            file_writer = open('files/todos.txt', 'w')
            file_writer.writelines(todos)
            file_writer.close()

        case 'display' | 'show':
            file_reader = open('files/todos.txt', 'r')
            todos = file_reader.readlines()
            file_reader.close()

            """
            new_todos = []
            for item in todos:
                new_item = item.strip('\n')
                new_todos.append(new_item)
            """
            ###new_todos = [item.strip('\n') for item in todos]

            for index, item in enumerate(todos) :
                item = item.strip('\n')
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
            print("Bye")
            break
        case something_else :
            print("this is an unknown selection, pleas check and try again")

print("Thanks for coming!")