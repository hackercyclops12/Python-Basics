#Ghost Game

#import functions 
from random import randint

#define variables
x = 1920
y = 1080

#game setup
print('Ghost Game')
feeling_brave = True
score = 0

#mainloop
while feeling_brave:
    ghost_door = randint(1,3)
    print('Three doors ahead . . .')
    print('A ghost behind one.')
    print('Which door do you open?')
    door = input('1, 2, or 3 ')
    door_num = int(door)
    if door_num == ghost_door:
        print('GHOST')
        feeling_brave = False
    if door_num > 3:
        print('Sorry, that is not an option!')
        quit()
 
    else:
        print('No Ghost')
        print('You enter the next room.')
        score = score + 1

#end        
print('Run away')
print('Game over! you scored!', score)
