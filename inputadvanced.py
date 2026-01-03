import pygame
from random import uniform,randint
pygame.init()
CLOCK = pygame.time.Clock()
FPS=30
WHITE = (255,255,255)
WIDTH = 1000
HEIGHT = 600
WN=pygame.display.set_mode((WIDTH,HEIGHT))
run=True
WN.fill(WHITE)
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run=False
    pygame.display.flip()
    CLOCK.tick(FPS)
pygame.quit()
#https://www.youtube.com/watch?v=f29ZOu4rXlM