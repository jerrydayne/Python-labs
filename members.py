"""
Please code this exercise in your computer IDE. For this exercise, download the members.txt file attached to the resources. Then, create a program that:

1. prompts the user to enter a new member.

2. adds that member to members.txt at the end of the existing members. For example, the user here has entered the member Solomon Right.


In the above example, Solomon Right will be added to members.txt updating the content of the file to:

John Smith

Sen Lakmi

Sono Octonot

Solomon Right
"""

while True :
    user_action = input("Enter 'VIEW' to view members or 'NEW'to add a new member : ")
    user_action = user_action.strip()

    match user_action :
        case 'view' :
            file_reader = open('files/members.txt', 'r')
            members = file_reader.readlines()
            file_reader.close()

            for index, item in enumerate(members) :
                item = item.title()
                item_row = f"{index + 1}.{item}"
                print(item_row)

        case 'new' :
            new_member = input("Enter new member : ") + "\n"

            file_reader = open('files/members.txt', 'r')
            members = file_reader.readlines()
            file_reader.close()

            members.append(new_member)
            file_writer = open('files/members.txt', 'w')
            file_writer.writelines(members)
            file_writer.close()
            

