#import functions
import pygame, sys, random
import pygame.locals as GAME_GLOBALS
import pygame.event as GAME_EVENTS
from time import sleep

#set window and variables
pygame.init()
clock = pygame.time.Clock()
windowWidth = 1920
windowHeight = 1080
surface = pygame.display.set_mode((windowWidth, windowHeight))
pygame.display.set_caption("Shh! You're PC is sleeping")
squareX = 0
squareY = 0
greenSquareX = windowWidth / 2
greenSquareY = windowHeight / 2
blueSquareX = 0.0
blueSquareY = 0.0
blueSquareVX = 1
blueSquareVY = 1

#mainloop
while True:
    COL1 = random.randint(0,255)
    COL2 = random.randint(0,255)
    COL3 = random.randint(0,255)
    surface.fill((255,255,255))
    pygame.draw.rect(surface, (COL1,COL2,COL3), (random.randint(0, windowWidth), random.randint(0, windowHeight), 200, 200 ) )
    sleep(0.2)
    for event in GAME_EVENTS.get():
        if event.type == GAME_GLOBALS.QUIT:
            pygame.quit()
            sys.exit()
    clock.tick(240)
    pygame.display.update()
