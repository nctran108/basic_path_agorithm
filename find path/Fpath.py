import queue
PATH = list()


def create_maze():
    maze = list()
    maze.append(["-", "O", "-", "-", "-", "-", "-", "-", "-", "-"])
    maze.append(["-", " ", " ", " ", " ", " ", "-", " ", "-", "-"])
    maze.append(["-", "-", "-", "-", "-", " ", "-", " ", "-", "-"])
    maze.append(["-", " ", " ", " ", " ", " ", " ", " ", " ", "-"])
    maze.append(["-", "-", " ", "-", "-", "-", "-", " ", "-", "-"])
    maze.append(["-", " ", " ", " ", "-", "-", "-", " ", "-", "-"])
    maze.append(["-", " ", "-", " ", " ", " ", " ", " ", "-", "-"])
    maze.append(["-", " ", "-", "-", " ", "-", "-", " ", "-", "-"])
    maze.append(["-", " ", "-", "-", " ", "-", "-", " ", "-", "-"])
    maze.append(["-", "-", "-", "-", "-", "-", "-", "X", "-", "-"])

    return maze


def print_maze(maze, path=""):
    i = find_start(maze)[0]
    j = find_start(maze)[1]
    pos = set()

    for move in path:
        if move == "U":
            i -= 1
        elif move == "D":
            i += 1
        elif move == "R":
            j += 1
        elif move == "L":
            j -= 1
        pos.add((i, j))

    for i, row in enumerate(maze):
        for j, elem in enumerate(row):
            if (i, j) in pos:
                print("*", end=" ")
            else:
                print(elem, end=" ")
        print()


def find_start(maze):
    start = [0, 0]
    count = 0
    for row in maze:
        for index in range(len(row)):
            if maze[count][index] == "O":
                start = [count, index]
                break
        count += 1
    return start


def find_moves(start, move):
    if move == "U":
        start[0] -= 1
    elif move == "D":
        start[0] += 1
    elif move == "R":
        start[1] += 1
    elif move == "L":
        start[1] -= 1
    return start


def find_end(maze, path):
    start = find_start(maze)

    for move in path:
        start = find_moves(start, move)

    i = start[0]
    j = start[1]
    if maze[i][j] == "X":
        print_maze(maze, path)
        print(f"Found end at: ({i}, {j})")
        return True

    return False


def valid_moves(maze, path):
    start = find_start(maze)

    for move in path:
        start = find_moves(start, move)

        i = start[0]
        j = start[1]
        if not(0 <= i <= len(maze) and 0 <= j <= len(maze[0])):
            return False
        elif maze[i][j] == "-":
            return False

    return True


def main():
    maze = create_maze()
    q = queue.Queue()
    q.put("")
    moves = list()

    while not find_end(maze, moves):
        moves = q.get()
        for direction in ["L", "R", "U", "D"]:
            path = moves + direction
            if valid_moves(maze, moves):
                q.put(path)


main()
