class Character:
    def __init__(self, pos):
        self.pos = pos
        self.state = 'walk'
        self.moves = []
        self.set()
    def set(self):
        pass
    def move(self, act):
        pass

class Player(Character):
    def set(self):
        self.moves = ['c8763']
    def move(self, act):
        if act == 'c8763':
            return {'atk': 8763}

class Monster(Character):
    pass
