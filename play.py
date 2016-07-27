import world
import character
import numbers

if __name__ == '__main__':
    while True:
        input_size = input('choose dungeon level: ')
        try:
            size = int(input_size)+2
            if size>=3:
                break
            else:
                print('Input should be > 0')
        except ValueError:
            print('Input is not integer.')
    dungeon = world.Dungeon(size=size)
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
    print('=================')
    print('Thank you for playing!')
