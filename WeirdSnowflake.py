from turtle import *
import random
COL = random.choice(['red','orange','yellow','green','blue','magenta'])
COL2 = random.choice(['red','orange','yellow','green','blue','magenta'])
if COL == COL2:
    COL = random.choice(['red','orange','yellow','green','blue','magenta'])
else:
    color(COL)
bgcolor(COL2)
for i in range (10):
    for i in range (2):
        forward(100)
        right(60)
        forward(100)
        right(120)
    right(36)
    

