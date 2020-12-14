#import functions
from turtle import *
import random

#define variables + assign a color to said variable
COL = random.choice(['red','orange','yellow','green','blue','magenta'])
COL2 = random.choice(['red','orange','yellow','green','blue','magenta'])

#check if both colors picked are the same, if so change them 
if COL == COL2:
    COL = random.choice(['red','orange','yellow','green','blue','magenta'])
else:
    color(COL)
    
#set background of turtle window
bgcolor(COL2)

#mainloop
for i in range (10):
    for i in range (2):
        forward(100)
        right(60)
        forward(100)
        right(120)
    right(36)
    

