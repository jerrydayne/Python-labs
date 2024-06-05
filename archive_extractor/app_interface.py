import FreeSimpleGUI as fsg

fsg.theme("Black")

select_label = fsg.Text("Select Archive")
select_input = fsg.Input()
select_btn = fsg.FileBrowse("Choose Archive", key="archive")

dir_label = fsg.Text("Select where to save extracted archive")
dir_input = fsg.Input()
dir_btn = fsg.FolderBrowse("Choose Location", key="destination")

extract_tbn = fsg.Button("Extract")
status_label = fsg.Text(key="ststus", text_color="white")

window = fsg.Window("Dayne Archive Extractor",
                    layout=[[select_label, select_input, select_btn],
                            [dir_label, dir_input, dir_btn],
                            [extract_tbn, status_label]])

window.read()
window.close()