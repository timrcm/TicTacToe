class Player:
    def __init__(self, name, piece):
        if name == 'AI':
            self.ai = True
        else:
            self.ai = False
        self.name = name
        self.piece = piece
        self.owned_spaces = []
