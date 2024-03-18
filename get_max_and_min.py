def get_max():
    with open("files/temperature.txt", 'r') as file_reader:
        grades = file_reader.readlines()
   
    Max = max(grades[1:])

    Min = min(grades)

    result = f"Max: {Max}, Min: {Min}"
    y = result.strip('\n')

    return y

print(get_max())