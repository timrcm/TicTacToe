# Basic text-based Tic Tac Toe game

from game import Game
from player import Player

game = Game()


def select_players():
    name_1 = input("What is the first player's name?\n")
    name_2 = input("What is the second player's name?\n")
    player_1 = Player(name_1, 'X')
    player_2 = Player(name_2, 'Y')
    return player_1, player_2


def check_for_winner():
    pass


def place_piece(player):
    game.draw_board()
    # This is ugly. What is a better selection method?
    try:
        location = int(input(f"Hi, {player.name}. Where would you like to place your piece?\n"
                             f"Enter a space number that is not yet taken: \n"))
    except ValueError:
        print('\nPlease enter a valid integer.')
        place_piece(player)
    else:
        if location in game.grid_coords.keys():
            if game.grid_coords[location] != 'X' and game.grid_coords[location] != 'Y':
                game.grid_coords[location] = f'{player.piece}'
            else:
                print('\nThat space is already taken. Try again.')
                place_piece(player)
        else:
            print('\nSorry, that coordinate was not found. Please try again.')
            place_piece(player)


if __name__ == '__main__':
    players = select_players()
    active_player = players[0]
    while True:
        # Keep swapping turns and playing until the game ends
        place_piece(active_player)
        if active_player == players[0]:
            active_player = players[1]
        else:
            active_player = players[0]
