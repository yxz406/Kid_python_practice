import pygame, sys, random
from pygame.color import THECOLORS
pygame.init()
screen = pygame.display.set_mode([720, 640])
screen.fill([255,255,255])
for i in range(1000):
    width = random.randint(0, 250)
    height = random.randint(0, 100)
    top = random.randint(0, 500)
    left = random.randint(0, 600)
    color_name = random.choice(list(THECOLORS.keys()))
    color = THECOLORS[color_name]
    line_width = random.randint(1, 10)
    pygame.draw.rect(screen,color,[left,top,width,height],line_width)
pygame.display.flip()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit()