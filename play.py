import world
import character
import scripts

if __name__ == '__main__':
    dungeon = world.Dungeon()
    pno = dungeon.add_player()
    dungeon.add_monster()
    dungeon.view()

    actions = []
    actions.append([])

    scripts.hello()
    moves = dungeon.get_playermoves(pno)
    """
    while True:
        print(moves, end="  ")
        enter = input("How? ")
        if enter in moves:
            break
    print(enter)
    """
