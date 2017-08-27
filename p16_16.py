import pygame, sys
pygame.init()
screen = pygame.display.set_mode([640, 480])
screen.fill([255, 255, 255])
my_ball = pygame.image.load("ball.jpg")
x = 40
y = 40
x_speed = 10

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.time.delay(50)
    pygame.draw.rect(screen, [255,255,255], [x,y,90,90], 0)
    x = x + x_speed
    if x > screen.get_width():
        x = -99
    screen.blit(my_ball, [x, y])
    pygame.display.flip()
pygame.quit()