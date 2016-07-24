import world
import character

if __name__ == '__main__':
    dungeon = world.Dungeon()
    player_num = 1
    player_no = []
    for p in range(player_num):
        player_no.append(dungeon.add_player())
    action = {}

    feedback = 1
    while feedback:
        for pno in player_no:
            dungeon.view()
            moves = dungeon.get_moves()
            while True:
                input_action = input('How? ')
                if input_action in moves:
                    break
            action['player'] = pno
            action['act'] = input_action
            feedback = dungeon.action(action)
            print(feedback)
            print('===============')
