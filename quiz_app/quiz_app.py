import json

with open("questions.json", 'r') as file_reader:
    content = file_reader.read()

data = json.loads(content)
score = 0
for index, question in enumerate(data):
    print(index + 1, question["question_text"])
    for i, alternative in enumerate(question["alternatives"]):
        print(i + 1, ".", alternative)
    user_choice = int(input("Select answer by entering number of your choice : "))
    question["user_choice"] = user_choice

    if question["correct_answer"] == question["user_choice"]:
        score = score + 1
        result = "Good Job!"
        message = f"{result} You answered question {index + 1} correctly"
    else:
        result = "Wrong!"
        message = f"{result} You selected '{question['user_choice']} instead of {question['correct_answer']}"
    print(message)

"""score = 0

for index, question in enumerate(data):
    if question["correct_answer"] == question["user_choice"]:
        score = score + 1
        message = f"you answered question {index + 1} correctly"
    else:
        message = f"for question {index + 1} you selected '{question['user_choice']} instead of {question['correct_answer']}"
    print(message)"""
if score == len(data):
    print("excellent! You answered all ", len(data), "correctly")
else:
    print("Your final score is :", score, "/", len(data))
