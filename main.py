from modules import functions
import time

now = time.strftime("%b %D, %Y %H:%M:%S")
print("The current date and time is", now)

while True :
    user_action = input("do you want to add, display, edit, complete or exit (add/display/exit): ")
    user_action = user_action.strip()

    if user_action.startswith("add") or user_action.startswith("new") :
        todo = user_action[4:] + "\n"

        todos = functions.get_todos()

        todos.append(todo)

        functions.write_todos(todos)
        feedback = todo.strip('\n')
        print(f"'{feedback}' has been added successfully to the Todo list")
        
    elif user_action.startswith("show") :

        todos = functions.get_todos('files/todos.txt')

        """
        new_todos = []
        for item in todos:
            new_item = item.strip('\n')
            new_todos.append(new_item)
        """
        ### new_todos = [item.strip('\n') for item in todos]

        for index, item in enumerate(todos) : 
            item = item.strip('\n')
            item = item.title()
            item_row = f"{index + 1}.{item}"
            print(item_row)

    elif user_action.startswith('edit') :
        try :        
            todo_serial_number = int(user_action[5:])
            todo_index = todo_serial_number - 1
            todo_to_be_edited = todos[todo_index].strip('\n')
            todo_serial_number = todo_index

            todos = functions.get_todos('files/todos.txt')

            new_todo = input("Enter new task you would want to do : ")
            todos[todo_serial_number] = new_todo + '\n'

            functions.write_todos(todos)

            print(todo_to_be_edited, "is replaced with ", new_todo)
        except ValueError :
            print("Invalid input")
            continue

    elif user_action.startswith('complete') or user_action.startswith('done    ') :
        try :
            todo_serial_number = int(user_action[9:])
            
            todos = functions.get_todos('files/todos.txt')

            todo_index = todo_serial_number -1
            todo_to_be_removed = todos[todo_index].strip('\n')
            todos.pop(todo_index)

            functions.write_todos(todos)

            message = f"Task '{todo_to_be_removed}' is completed and removed from the list. enter 'show' to view the updated list"
            print(message)
        except IndexError :
            print("There's no item with that number")
            continue

    elif user_action.startswith('exit') :
        print("Bye")
        break
    else :
        print("this is an unknown selection, pleas check and try again")

print("Thanks for coming!")