# Basic text-based Tic Tac Toe game

grid_coords = {
    (0, 0): ' ', (0, 1): ' ', (0, 2): ' ',
    (1, 0): ' ', (1, 1): ' ', (1, 2): ' ',
    (2, 0): ' ', (2, 1): ' ', (2, 2): ' '
}


def draw_board():
    for i, coordinate in enumerate(grid_coords):
        i += 1  # Less opaque math on iterable for separating the board
        print(f' {grid_coords.get(coordinate)}', end='')
        if i % 3 == 0:
            print('\n-----------')
        else:
            print(' |', end='')


if __name__ == '__main__':
    draw_board()
