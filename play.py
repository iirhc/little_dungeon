import world
import character
import scripts

if __name__ == '__main__':
    dungeon = world.Dungeon(size=3)

    scripts.hello()
    dungeon.view()
    while True:
        moves = dungeon.get_moves()
        while True:
            input_action = input('How? ')
            if input_action in moves:
                break
        feedback = dungeon.action(input_action)
        if feedback == 0:
            print('===============')
            break
        print(feedback)
        print('===============')
    print('Thank you for playing!')
