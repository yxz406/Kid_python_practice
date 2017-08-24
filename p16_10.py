import pygame, sys
pygame.init()
screen = pygame.display.set_mode([640, 480])
screen.fill([255, 255, 255])
my_ball = pygame.image.load("ball.jpg")
x = 40
y = 40
screen.blit(my_ball, [x, y])
pygame.display.flip()
for looper in range(1, 100):
    pygame.time.delay(10)
    pygame.draw.rect(screen, [255,255,255], [x,y,90,90], 0)
    x = x + 5
    screen.blit(my_ball, [x, y])
    pygame.display.flip()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit()