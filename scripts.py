def hello():
    a = []
    a.append(' ')
    a.append('...where is it?')
    a.append('It seems that I am in a dungeon, and I can feel something moving in the dark.')
    a.append('I should get out of here quickly.')
    a.append('...')
    a.append('I find a magic map around me, which can show me where I am.')
    return a

def there_is_wall():
    a = []
    a.append('There is wall, cannot pass through.')
    return a

def escape():
    a = []
    a.append('It\'s an exit, and I survive from the dungeon!')
    return a

def meet_monster():
    a = []
    a.append('A monster appear and catch me, and......')
    a.append(' ')
    a.append('- Game Over -')
    a.append(' ')
    return a

def monster_alert():
    a = []
    a.append('I can feel that there is monster around me...')
    return a
