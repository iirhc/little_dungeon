import world
import character
import scripts

if __name__ == '__main__':
    dungeon = world.Dungeon()
    player_num = 1
    player_no = []
    for p in range(player_num):
        player_no.append(dungeon.add_player())
    action = {}

    scripts.hello()
    dungeon.view()
    while True:
        for pno in player_no:
            #dungeon.view()
            moves = dungeon.get_moves()
            while True:
                input_action = input('How? ')
                if input_action in moves:
                    break
            action['player'] = pno
            action['act'] = input_action
        feedback = dungeon.action(action)
        if feedback == 0:
            break
        print(feedback)
        print('===============')
