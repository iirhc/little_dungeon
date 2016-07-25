import world
import character

if __name__ == '__main__':
    dungeon = world.Dungeon(size=3)
    dungeon.view()
    while True:
        moves = dungeon.get_moves()
        dungeon.view()
        while True:
            input_action = input('How? ')
            if input_action in moves:
                break
        feedback = dungeon.action(input_action)
        dungeon.view()
        if feedback == 0:
            break
    print('===============')
    print('Thank you for playing!')
