from modules import functions

import FreeSimpleGUI as fsg

label = fsg.Text("type in a Todo here")
input_box = fsg.InputText(tooltip="Enter a Todo", key='todo')
add_button = fsg.Button("Add")

window = fsg.Window('Dayne Todo App',
                    layout=[[label], [input_box, add_button]],
                    font=('helvetica', 20))


while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case 'Add' :
            todos = functions.get_todos()
            new_todo = values['todo'] + '\n'
            todos.append(new_todo)
            functions.write_todos(todos)
        case fsg.WIN_CLOSED :
            break



window.close()
