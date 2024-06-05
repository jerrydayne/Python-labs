import FreeSimpleGUI as fsg
from extractor_function import extract_archive

fsg.theme("Black")

select_label = fsg.Text("Select Archive")
select_input = fsg.Input()
select_btn = fsg.FileBrowse("Choose Archive", key="archive")

dir_label = fsg.Text("Select where to save extracted archive")
dir_input = fsg.Input()
exit_btn = fsg.Button("Exit")
dir_btn = fsg.FolderBrowse("Choose Location", key="destination")

extract_tbn = fsg.Button("Extract")
status_label = fsg.Text(key="status", text_color="white")

window = fsg.Window("Dayne Archive Extractor",
                    layout=[[select_label, select_input, select_btn],
                            [dir_label, dir_input, dir_btn],
                            [extract_tbn, exit_btn],
                            [status_label]])

while True:
    event, values = window.read()
    print(event, values)

    match event:
        case "Exit":
            break
        case fsg.WIN_CLOSED:
            break

    archive_path = values["archive"]
    dest_folder = values["destination"]
    extract_archive(archive_path, dest_folder)
    window["status"].update(value="Extraction Completed Successfully!")


window.close()