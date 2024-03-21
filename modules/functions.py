FILEPATH = "./files/todos.txt"


def get_todos(file_path=FILEPATH):
    """Gets the list of to-do's from the file todo.txt"""
    with open(file_path, 'r') as file_reader :
        todos_local = file_reader.readlines()
    return todos_local


def write_todos(todos_arg, file_path=FILEPATH):
    """writes the added to-do item to the list of to-do's file i.e doto.txt in this case"""
    with open(file_path, 'w') as file_writer:
        file_writer.writelines(todos_arg)


# testing the functions above
if __name__ == "__main__":
    print("works fine")
    print(get_todos())