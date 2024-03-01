file_contents = ["Local is not fake",
                "Boys are not smiling",
                "The good, the bad and the ugly"]

file_names = ["dayne.txt",
              "terry.txt",
              "movie.txt"]

for file_content, file_name in zip(file_contents, file_names) : 
    file = open(f"files/{file_name}", "w")
    file.write(file_content)