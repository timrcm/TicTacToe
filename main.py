# Basic text-based Tic Tac Toe game

from game import Game
from player import Player


def select_players():
    name_1 = input("What is the first player's name?\nEnter 'AI' for an automated player.\n")
    name_2 = input("What is the second player's name?\nEnter 'AI' for an automated player.\n")
    player_1 = Player(name_1, 'X')
    player_2 = Player(name_2, 'Y')
    return player_1, player_2


if __name__ == '__main__':
    players = select_players()
    active_player = players[0]
    game = Game()
    while True:
        # Keep swapping turns and playing until the game ends
        game.place_piece(active_player)
        if active_player == players[0]:
            active_player = players[1]
        else:
            active_player = players[0]
