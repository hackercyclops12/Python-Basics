#import function
from turtle import *

#defien turtle modes + variable 
speed('fastest')
v = 66
pensize(150)

#change background color of the window 
bgcolor('grey')

#mainloop
while True:
    v = v + 0.5
    right(90)
    color('red')
    forward(v)
    rt(90)
    color('orange')
    forward(v)
    left(90)
    color('yellow')
    forward(v)
    lt(v)
    color('green')
    forward(v)
    right(90)
    color('cyan')
    forward(v)
    rt(90)
    color('blue')
    forward(v)
    left(90)
    color('purple')
    forward(v) 
    undo()
              
