from player import Player


class Game:
    def __init__(self):
        self.grid_coords = {
            1: '1', 2: '2', 3: '3',
            4: '4', 5: '5', 6: '6',
            7: '7', 8: '8', 9: '9'
        }
        self.winning_combos = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
        self.turn_counter = 9

    def check_for_winner(self):
        if self.turn_counter == 0:
            print('The game is tied. Better luck next time!')
            exit(0)

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

    def place_piece(self, player: Player):
        self.draw_board()
        # This is ugly. What is a better selection method?
        try:
            location = int(input(f"Hi, {player.name}. Where would you like to place your piece?\n"
                                 f"Enter a space number that is not yet taken: \n"))
        except ValueError:
            print('\nPlease enter a valid integer.')
            self.place_piece(player)
        else:
            if location in self.grid_coords.keys():
                if self.grid_coords[location] != 'X' and self.grid_coords[location] != 'Y':
                    self.grid_coords[location] = f'{player.piece}'
                    self.turn_counter -= 1
                    self.check_for_winner()
                    print(f'{self.turn_counter} turns left!')
                else:
                    print('\nThat space is already taken. Try again.')
                    self.place_piece(player)
            else:
                print('\nSorry, that coordinate was not found. Please try again.')
                self.place_piece(player)
