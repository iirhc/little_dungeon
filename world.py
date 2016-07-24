import random
import character as c_list

class Dungeon:
# Interface
    # initialize
    def __init__(self, size=3):
        self.size = size
        self.obj_in = []
        self.characters = []
        self.monsters = []
        self.exit_pos = [-1, -1]
        self.exit_pos = self.init_pos()
    def add_player(self):
        role = c_list.Player(self.init_pos())
        self.characters.append(role)
        return len(self.characters)-1
    def add_monster(self):
        mon = c_list.Monster(self.init_pos())
        self.monsters.append(mon)
    # get player infomation
    def get_playermoves(self, pno):
        return self.characters[pno].moves
    # do action
    def action(self, actions):
        for role in self.characters:
            role.move(actions.pop(0))
        return self.decision()
    # visualize
    def view(self):
        print("size:", self.size)
        print("exit:", self.exit_pos)
        for role in self.characters:
            print("your position:", role.pos)
        for mon in self.monsters:
            print("mon's position:", mon.pos)
        print('===============')
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

# private method
    def init_pos(self):
        while True:
            pos = [random.randint(0, self.size-1), random.randint(0, self.size-1)]
            if pos not in self.obj_in:
                self.obj_in.append(pos)
                break
        return pos
    def decision(self):
        for role in self.characters:
            if role.pos == self.exit_pos:
                return 'escape'
            for mon in self.monsters:
                if mon.pos == role.pos:
                    return 'die'
        return 'nothing happens'
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
