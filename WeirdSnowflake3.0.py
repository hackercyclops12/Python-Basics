from turtle import *
import random
speed("fastest")
pensize(20)
N = 1
COL = random.choice(['red','orange','yellow','green','blue','magenta'])
bgcolor("grey")
while True:
    N = N + 2.5
    for i in range (2):
        COL = random.choice(['red','orange','yellow','green','blue','magenta'])
        color(COL)
        forward(N)
        right(150)
        forward(N)
        right(150)
    right(222)

    
    

