class Game:
    def __init__(self):
        self.grid_coords = {
            1: '1', 2: '2', 3: '3',
            4: '4', 5: '5', 6: '6',
            7: '7', 8: '8', 9: '9'
        }

    def draw_board(self):
        print('\n')
        for i, val in self.grid_coords.items():
            print(f' {val}', end='')
            if i == 9:
                print('\n\n')
            elif i % 3 == 0:
                print('\n-----------')
            else:
                print(' |', end='')
