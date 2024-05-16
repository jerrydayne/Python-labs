import FreeSimpleGUI as fsg

label1 = fsg.Text("select the file(s) you'd want to compress : ")
input1 = fsg.Input()
choose_btn1 = fsg.FilesBrowse("choose")

label2 = fsg.Text("select the file(s) you'd want to compress : ")
input2 = fsg.Input()
choose_btn2 = fsg.FilesBrowse("choose")


window = fsg.Window("File Compressorby Dyne.io",
                    layout = [[label1, input1, choose_btn1],
                              [label2, input2, choose_btn2]])

window.read()
window.close()