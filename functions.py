FILEPATH="todos.txt"


def get_todos(filepath=FILEPATH):
    """
    Read a text file and return the list of to-do list items
    :param filepath:
    :return: todos_local
    """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg,filepath=FILEPATH):
    """
    Write the to-do items list in the text file
    :param todos_arg:
    :param filepath:
    :return: None
    """
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)



if __name__=="__main__":
    print("Hello")
    print(get_todos())