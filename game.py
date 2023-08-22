from player import Player
import random


class Game:
    def __init__(self):
        self.grid_coords = {
            1: '1', 2: '2', 3: '3',
            4: '4', 5: '5', 6: '6',
            7: '7', 8: '8', 9: '9'
        }
        self.remaining_options = [space for space in self.grid_coords.keys()]
        self.winning_combos = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
        self.turn_counter = 9
        self.draw_board()

    def check_for_winner(self, player):
        self.draw_board()
        consecutive_spaces = 0
        for combo in self.winning_combos:
            for num in combo:
                if num in player.owned_spaces:
                    consecutive_spaces += 1
            if consecutive_spaces == 3:
                print(f'{player.name} wins!!')
                exit(0)
            else:
                consecutive_spaces = 0
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
        # This is ugly. What is a better selection method?
        try:
            if player.ai:
                location = random.choice(self.remaining_options)
                print(f'AI chose space {location}')
            else:
                location = int(input(f"Hi, {player.name}. Where would you like to place your piece?\n"
                                     f"Enter a space number that is not yet taken: \n"))
        except ValueError:
            print('\nPlease enter a valid integer.')
            self.place_piece(player)
        else:
            if location in self.grid_coords.keys():
                if location in self.remaining_options:
                    self.grid_coords[location] = f'{player.piece}'
                    player.owned_spaces.append(location)
                    self.remaining_options.remove(location)
                    self.turn_counter -= 1
                    self.check_for_winner(player)
                else:
                    print('\nThat space is already taken. Try again.')
                    self.place_piece(player)
            else:
                print('\nSorry, that coordinate was not found. Please try again.')
                self.place_piece(player)
