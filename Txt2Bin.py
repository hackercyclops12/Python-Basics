import pygame
pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
 

print(">>>>>>>>>>Text to Binary Convertor<<<<<<<<<<\n")

conversion=input("Enter text to convert to Binary: ")


size = (600, 400)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("Binary Conversion")

done = False
clock = pygame.time.Clock()
 
text_rotate_degrees = 0

Binary=(' '.join(format(ord(x), 'b') for x in conversion))

while not done:
 
    for event in pygame.event.get():  
        if event.type == pygame.QUIT:  
            done = True  

    screen.fill(WHITE)
    font = pygame.font.SysFont('Calibri', 25, True, False)
    
    text = font.render(Binary, True, BLACK)
    text = pygame.transform.rotate(text, text_rotate_degrees)
    text_rotate_degrees += 1
    screen.blit(text, [100, 50])
    pygame.display.flip()

    clock.tick(60)

pygame.quit()


print(' '.join(format(ord(x), 'b') for x in conversion))
