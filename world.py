import random
import character as c_list
import scripts

class Dungeon:
# Interface
    # initialize
    def __init__(self, size=3):
        self.size = size
        self.characters = []
        self.monsters = []
        self.exit_pos = [-1, -1]
        self.exit_pos = self.init_pos()
        self.add_monster()
    def add_player(self):
        role = c_list.Player(self.init_pos())
        self.characters.append(role)
        return len(self.characters)
    def add_monster(self):
        mon = c_list.Monster(self.init_pos())
        self.monsters.append(mon)
    # visualize
    def view(self):
        print("size:", self.size)
        print("exit:", self.exit_pos)
        for role in self.characters:
            print("your position:", role.pos)
        for mon in self.monsters:
            print("mon's position:", mon.pos)
        print('===============')
        self.show_map()
    # do action
    def get_moves(self):
        self.show_moves()
        return ['w', 'a', 's', 'd', 'pass', 'p']
    def action(self, action):
        pno = action['player']-1
        act = action['act']
        if act in ['pass', 'p']:
            pass
        elif act in ['w', 'a', 's', 'd']:
            self.walk(self.characters[pno], act)
            self.show_map()
        return self.decision(self.characters[pno])

    # reaction
    def decision(self, role):
        meet = self.meet(role.pos)
        if meet == 'exit':
            scripts.escape()
            return 0
        elif meet == 'monster':
            scripts.meet_monster()
            return 0
        return 'nothing happens'

# private method
    def init_pos(self):
        while True:
            pos = [random.randint(0, self.size-1), random.randint(0, self.size-1)]
            if self.meet(pos) == 'nothing':
                break
        return pos
    def meet(self, pos):
        if pos == self.exit_pos:
            return 'exit'
        else:
            for mon in self.monsters:
                if pos == mon.pos:
                    return 'monster'
            else:
                for chara in self.characters:
                    if pos == chara.pos:
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
    def show_map(self):
        ptr = [0, 0]
        print('┌─', end="")
        for x in range(self.size-1):
            print('┬─', end="")
        print('┐')
        self.show_chara_in_block(ptr)
        for y in range(self.size-1):
            print('├─', end="")
            for x in range(self.size-1):
                print('┼─', end="")
            print('┤')
            ptr[0] = 0
            ptr[1] += 1
            self.show_chara_in_block(ptr)
        print('└─', end="")
        for x in range(self.size-1):
            print('┴─', end="")
        print('┘')
        print('===============')
    def show_chara_in_block(self, ptr):
        chara_in = []
        for role in self.characters:
            chara_in.append(role.pos)
        for x in range(self.size):
            if ptr in chara_in:
                print('│★', end="")
            else:
                print('│　', end="")
            ptr[0] += 1
        print('│')
    def show_moves(self):
        print('　　↑　　')
        print('　　ｗ　　')
        print('←ａ　ｄ→')
        print('　　ｓ　　')
        print('　　↓　　　or pass')
    # useless setting now
    def get_playermoves(self, pno):
        return self.characters[pno-1].moves
