def get_todos():
    with open("todo.txt") as f:
        lines = f.readlines()
    return lines

def write_todos(lines):
    with open("todo.txt", "w") as f:
        for line in lines:
            f.write(line)