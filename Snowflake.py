#import functions
from turtle import *
import random

#define varable + pick a color and asign it to said variable
COL = random.choice(['red','orange','yellow','green','blue','magenta'])
COL2 = random.choice(['red','orange','yellow','green','blue','magenta'])

#set turtle color + window background color 
color(COL)
bgcolor(COL2)

#mainloop
for i in range (10):
    for i in range (2):
        forward(100)
        right(60)
        forward(100)
        right(120)
    right(36)
    

