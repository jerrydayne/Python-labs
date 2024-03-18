def get_average_temperarture() :
    with open("files/temperature.txt", 'r') as file_reader:
        data = file_reader.readlines()

    values = data[1:]
    values = [float(value) for value in values]

    average_local = sum(values) / len(values)
    return average_local


average_temperature = get_average_temperarture()
result = round(average_temperature, 2)
print(result)