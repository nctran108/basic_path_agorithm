import queue
PATH = list()


def create_maze():
    maze = list()
    maze.append(["@", "o", "@", "@", "@", "@", "@", "@", "@", "@"])
    maze.append(["@", " ", " ", " ", " ", "@", "@", " ", "@", "@"])
    maze.append(["@", " ", "@", "@", "@", " ", "@", " ", "@", "@"])
    maze.append(["@", " ", " ", " ", " ", " ", " ", " ", " ", "@"])
    maze.append(["@", "@", " ", "@", "@", "@", "@", " ", "@", "@"])
    maze.append(["@", " ", " ", " ", "@", "@", "@", " ", "@", "@"])
    maze.append(["@", " ", "@", " ", " ", " ", " ", " ", "@", "@"])
    maze.append(["@", " ", "@", "@", " ", "@", "@", " ", "@", "@"])
    maze.append(["@", " ", "@", "@", " ", "@", "@", " ", "@", "@"])
    maze.append(["@", "@", "@", "@", "@", "@", "@", "X", "@", "@"])

    return maze


def print_maze(maze):
    for row in maze:
        for elem in row:
            print(elem," ", end="")
        print()


def main():
    maze = create_maze()
    print_maze(maze)


main()