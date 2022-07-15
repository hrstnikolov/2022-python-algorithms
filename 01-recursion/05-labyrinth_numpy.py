import numpy as np

FREE = 0
VISITED = 1
WALL = 5
EXIT = 9


maze = np.array([
    [0, 0, 0],
    [0, 5, 0],
    [0, 9, 0],
])

def find_paths(maze, x=0, y=0, path=''):
    maze[x]
    find_paths(maze, x + 1, y, path + 'R')
    find_paths(maze, x - 1, y, path + 'L')
    find_paths(maze, x, y + 1, path + 'D')
    find_paths(maze, x, y - 1, path + 'U')

