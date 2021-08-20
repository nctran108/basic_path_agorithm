import queue
ROWS, COLS = 10, 10

def createmaze():
    MAZE = []
    MAZE.append(['@', 'O', '@', '@', '@', '@', '@', '@', '@', '@'])
    MAZE.append(['@', ' ', ' ', ' ', ' ', '@', '@', ' ', '@', '@'])
    MAZE.append(['@', ' ', '@', '@', '@', ' ', '@', ' ', '@', '@'])
    MAZE.append(['@', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '@'])
    MAZE.append(['@', '@', ' ', '@', '@', '@', '@', ' ', '@', '@'])
    MAZE.append(['@', ' ', ' ', ' ', '@', '@', '@', ' ', '@', '@'])
    MAZE.append(['@', ' ', '@', ' ', ' ', ' ', ' ', ' ', '@', '@'])
    MAZE.append(['@', ' ', '@', '@', ' ', '@', '@', ' ', '@', '@'])
    MAZE.append(['@', ' ', '@', '@', ' ', '@', '@', ' ', '@', '@'])
    MAZE.append(['@', '@', '@', '@', '@', '@', '@', 'X', '@', '@'])

    return MAZE

def printmaze(MAZE):
    print(MAZE)


def main(ROWS, COLS):
    maze = createmaze()
    printmaze(maze)