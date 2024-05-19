import FreeSimpleGUI as fsg
from zip_creator import create_zip



label1 = fsg.Text("select the file(s) you'd want to compress : ")
input1 = fsg.Input()
choose_btn1 = fsg.FilesBrowse("choose", key="files")

label2 = fsg.Text("select the destination folder : ")
input2 = fsg.Input()
choose_btn2 = fsg.FolderBrowse("choose", key="folder")

compress_btn = fsg.Button("compress")
status_label = fsg.Text(" ", key="status")



window = fsg.Window("File Compressor by Dayne.ng",
                    layout=[[label1, input1, choose_btn1],
                            [label2, input2, choose_btn2],
                            [compress_btn, status_label]])
while True:
    event, values = window.read()
    print(event, values)
    file_paths = values['files'].split(";")
    dest_folder = values['folder']
    create_zip(file_paths, dest_folder)
    window["status"].update(value="compressed successfully by Dayne.ng")



window.close()