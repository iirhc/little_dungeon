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
        self.descriptions = []
        self.descriptions += scripts.hello()
        self.show_map()
    # visualize
    def view(self):
        #self.print_data()
        for d in self.descriptions:
            print(d)
        self.descriptions = []
    # do action
    def get_moves(self):
        self.monster_alert()
        self.show_moves()
        return ['w', 'a', 's', 'd', 'pass', 'p', 'g']
    def action(self, act):
        if act in ['g']:
            return 0
        elif act in ['pass', 'p']:
            pass
        elif act in ['w', 'a', 's', 'd']:
            self.walk(self.character, act)
        self.show_map()
        self.monster_action()
        return self.decision()

# private method
    #initialize
    def init_pos(self):
        while True:
            pos = [random.randint(0, self.size-1), random.randint(0, self.size-1)]
            if self.meet(pos) == 'nothing':
                break
        return pos
    def add_player(self):
        self.character = c_list.Player(self.init_pos())
    def add_monster(self):
        mon = c_list.Monster(self.init_pos())
        self.monsters.append(mon)
    # react
    def decision(self):
        meet = self.meet(self.character.pos)
        if meet == 'exit':
            self.descriptions += scripts.escape()
            return 0
        elif meet == 'monster':
            self.descriptions += scripts.meet_monster()
            return 0
        self.descriptions += ['nothing happens']
        return 'nothing happens'
    # func
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
                self.descriptions += scripts.there_is_wall()
            else:
                role.pos[1] -= 1
        elif act == 'a':
            if role.pos[0] == 0:
                self.descriptions += scripts.there_is_wall()
            else:
                role.pos[0] -= 1
        elif act == 's':
            if role.pos[1] == self.size-1:
                self.descriptions += scripts.there_is_wall()
            else:
                role.pos[1] += 1
        elif act == 'd':
            if role.pos[0] == self.size-1:
                self.descriptions += scripts.there_is_wall()
            else:
                role.pos[0] += 1
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
    def print_data(self):
        print('/////////////////')
        print("size:", self.size)
        print("exit:", self.exit_pos)
        print("your position:", self.character.pos)
        for mon in self.monsters:
            print("mon's position:", mon.pos)
        print('/////////////////')
    def show_map(self):
        string = '=================\n'
        for y in range(self.size):
            for x in range(self.size):
                if [x, y] == self.character.pos:
                    string += '[★]'
                else:
                    string += '[  ]'
            string += '\n'
        string += '================='
        self.descriptions += [string]
    def show_moves(self):
        string = '=================\n'
        string += '\t↑\n'
        string += '\tw\n'
        string += '←a\t\td→\n'
        string += '\ts\n'
        string += '\t↓\t\tor pass\n'
        string += '================='
        self.descriptions += [string]
    def monster_alert(self):
        x = self.character.pos[0]
        y = self.character.pos[1]
        around = [[x+1, y], [x-1, y], [x, y+1], [x, y-1]]
        for mon in self.monsters:
            if mon.pos in around:
                self.descriptions += scripts.monster_alert()
