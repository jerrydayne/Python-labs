from modules import functions

import FreeSimpleGUI as fsg

label = fsg.Text("type in a Todo here")
input_box = fsg.InputText(tooltip="Enter a Todo")
add_button = fsg.Button("Add")

window = fsg.Window('Dayne Todo App', layout=[[label], [input_box, add_button]])
window.read()
window.close()