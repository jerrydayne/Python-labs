from modules import functions

import FreeSimpleGUI as fsg
import time

fsg.theme("DarkGrey6")
clock = fsg.Text('', key="clock")
label = fsg.Text("type in a Todo here")
input_box = fsg.InputText(tooltip="Enter a Todo", key='todo')
add_button = fsg.Button("Add")
list_box = fsg.Listbox(values=functions.get_todos(), key='todos',
                       enable_events=True, size=[35, 10])
edit_button = fsg.Button("Edit")
complete_btn = fsg.Button("Complete")
exit_btn = fsg.Button("Exit")


window = fsg.Window('Dayne Todo App',
                    layout=[[clock],
                            [label],
                            [input_box, add_button],
                            [list_box, edit_button, complete_btn],
                            [exit_btn]],
                    font=('helvetica', 20))


while True:
    event, values = window.read(timeout=100)
    window["clock"].update(value=time.strftime("%b %D, %Y %H:%M:%S"))
    print(1, 'event = ', event)
    print(2, 'values = ', values)
    print(3, 'selected todo', values['todos'])
    match event:
        case 'Add':
            todos = functions.get_todos()
            new_todo = values['todo'] + '\n'
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos'].update(values=todos)

        case 'Edit':
            try:
                todo_to_edit = values['todos'][0]
                new_todo = values['todo']
                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                functions.write_todos(todos)
                window['todos'].update(values=todos)
            except IndexError:
                fsg.Popup("Kindly select an item you'd want to edit", font=("helvetica", 16))

        case 'Complete':
            try:
                todo_to_complete = values['todos'][0]
                todos = functions.get_todos()
                todos.remove(todo_to_complete)
                functions.write_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value="")
            except IndexError:
                fsg.Popup("First select an item, them proceed to complete", font=("helvetica", 16))

        case 'Exit':
            break

        case 'todos':
            window['todo'].update(value=values['todos'][0])
        case fsg.WIN_CLOSED:
            break



window.close()
