import csv

with open("files/csv_example.csv", 'r') as file_reader:
    data = list(csv.reader(file_reader))

#get user input
city = input("enter city")

for row in data[1:]:
    if row[0] == city:
        print(row[0], "=", row[1])