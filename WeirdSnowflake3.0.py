#import functions
from turtle import *
import random

#print to console + set turtle mode + set variable
print("The longer you wait the better this looks!")
speed("fastest")
pensize(20)
N = 1

#define varible + choose color to assign to said variable 
COL = random.choice(['red','orange','yellow','green','blue','magenta'])
bgcolor("grey")

#mainloop
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
    
    
