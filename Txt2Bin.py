#import pygame and set it up
import pygame
pygame.init()

#set variables 
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
 
#print header to console
print(">>>>>>>>>>Text to Binary Convertor<<<<<<<<<<\n")

#ask use for what to convert to binary
conversion=input("Enter text to convert to Binary: ")

#create variable + draw pygame window (1920/1080)
size = (1920, 1080)
screen = pygame.display.set_mode(size)

#write text into said pygame window
pygame.display.set_caption("Binary Conversion")

#create variable
done = False
clock = pygame.time.Clock()
text_rotate_degrees = 0

Binary=(' '.join(format(ord(x), 'b') for x in conversion))

#mainloop
while not done: 
    for event in pygame.event.get():  
        if event.type == pygame.QUIT:  
            done = True  

    screen.fill(WHITE)
    font = pygame.font.SysFont('Calibri', 25, True, False)
    
    text = font.render(Binary, True, BLACK)
    text = pygame.transform.rotate(text, text_rotate_degrees)
    screen.blit(text, [100, 500])
    pygame.display.flip()
    clock.tick(60)

pygame.quit()


print(' '.join(format(ord(x), 'b') for x in conversion))
