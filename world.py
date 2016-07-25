import random
import character as c_list
import scripts

class Dungeon:
# Interface
    # initialize
    def __init__(self, size=3):
        self.size = size
        self.monsters = []
        self.character = c_list.Player([-1, -1])
        self.exit_pos = [-1, -1]
        self.exit_pos = self.init_pos()
        for i in range(size-2):
            self.add_monster()
        self.add_player()
    def add_player(self):
        self.character = c_list.Player(self.init_pos())
    def add_monster(self):
        mon = c_list.Monster(self.init_pos())
        self.monsters.append(mon)
    # visualize
    def view(self):
        self.show_map()
    # do action
    def get_moves(self):
        self.show_moves()
        return ['w', 'a', 's', 'd', 'pass', 'p']
    def action(self, act):
        if act in ['pass', 'p']:
            pass
        elif act in ['w', 'a', 's', 'd']:
            self.walk(self.character, act)
        self.show_map()
        self.monster_action()
        self.monster_alert()
        return self.decision()


# private method
    def init_pos(self):
        while True:
            pos = [random.randint(0, self.size-1), random.randint(0, self.size-1)]
            if self.meet(pos) == 'nothing':
                break
        return pos
    # reaction
    def decision(self):
        meet = self.meet(self.character.pos)
        if meet == 'exit':
            scripts.escape()
            return 0
        elif meet == 'monster':
            scripts.meet_monster()
            return 0
        return 'nothing happens'
    def meet(self, pos):
        if pos == self.exit_pos:
            return 'exit'
        else:
            for mon in self.monsters:
                if pos == mon.pos:
                    return 'monster'
            else:
                if pos == self.character.pos:
                    return 'player'
        return 'nothing'
    def walk(self, role, act):
        if act == 'w':
            if role.pos[1] == 0:
                scripts.there_is_wall()
            else:
                role.pos[1] -= 1
        elif act == 'a':
            if role.pos[0] == 0:
                scripts.there_is_wall()
            else:
                role.pos[0] -= 1
        elif act == 's':
            if role.pos[1] == self.size-1:
                scripts.there_is_wall()
            else:
                role.pos[1] += 1
        elif act == 'd':
            if role.pos[0] == self.size-1:
                scripts.there_is_wall()
            else:
                role.pos[0] += 1
    def monster_alert(self):
        x = self.character.pos[0]
        y = self.character.pos[1]
        around = [[x+1, y], [x-1, y], [x, y+1], [x, y-1]]
        for mon in self.monsters:
            if mon.pos in around:
                scripts.monster_alert()
                print('===============')
    # monster move
    def monster_action(self):
        for mon in self.monsters:
            self.monster_walk(mon)
    def monster_walk(self, mon):
        moves = ['p']
        x = mon.pos[0]
        y = mon.pos[1]
        if x != 0:
            if [x-1, y] != self.exit_pos:
                moves.append('a')
        if x != self.size-1:
            if [x+1, y] != self.exit_pos:
                moves.append('d')
        if y != 0:
            if [x, y-1] != self.exit_pos:
                moves.append('w')
        if y != self.size-1:
            if [x, y+1] != self.exit_pos:
                moves.append('s')
        self.walk(mon, moves[random.randint(0, len(moves)-1)])
    # show
    def show_map(self):
        for y in range(self.size):
            for x in range(self.size):
                if [x, y] == self.character.pos:
                    print('[★]', end="")
                else:
                    print('[  ]', end="")
            print('')
        print('===============')
    def show_moves(self):
        print('\t↑')
        print('\tw')
        print('←a\t\td→')
        print('\ts')
        print('\t↓\t\tor pass')
