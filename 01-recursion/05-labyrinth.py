WALL = '*'
EMPTY = '-'
EXIT = 'e'
VISITED = 'v'


def is_inbound(labyrinth, row, col):
    return 0 <= row < len(labyrinth) and 0 <= col < len(labyrinth[0])


def is_visitable(cell):
    return cell != WALL and cell != VISITED


def is_solution(cell):
    return cell == EXIT


def find_paths(labyrinth, row=0, col=0, path=''):
    if not is_inbound(labyrinth, row, col):
        return

    cell = labyrinth[row][col]
    if is_solution(cell):
        print(path)
    elif is_visitable(cell):
        labyrinth[row][col] = VISITED
        find_paths(labyrinth, row, col + 1, path + 'R')
        find_paths(labyrinth, row, col - 1, path + 'L')
        find_paths(labyrinth, row - 1, col, path + 'U')
        find_paths(labyrinth, row + 1, col, path + 'D')
        labyrinth[row][col] = EMPTY


# labyrinth = [
#     ['-', '-', '-', ],
#     ['-', '*', '-', ],
#     ['-', '-', 'e', ],
# ]

def read_labyrinth():
    n_rows = int(input())
    n_cols = int(input())

    labyrinth = []
    for _ in range(n_rows):
        row = list(input())
        labyrinth.append(row)

    return labyrinth

labyrinth = read_labyrinth()
find_paths(labyrinth)
