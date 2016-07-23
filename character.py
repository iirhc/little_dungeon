class Character:
    def __init__(self, pos):
        self.pos = pos
        self.moves = []
        self.set()
    def set(self):
        pass
    def move(self, act):
        pass

class Player(Character):
    def set(self):
        self.moves = ['w', 'a', 's', 'd']
    def move(self, act):
        if act == 'w':
            self.pos[1] -= 1
        elif act == 'a':
            self.pos[0] -= 1
        elif act == 's':
            self.pos[1] += 1
        elif act == 'd':
            self.pos[0] += 1

class Monster(Character):
    pass
