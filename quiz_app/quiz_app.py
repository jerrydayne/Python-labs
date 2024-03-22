import json

with open("questions.json", 'r') as file_reader:
    content = file_reader.read()

data = json.loads(content)

print(data)