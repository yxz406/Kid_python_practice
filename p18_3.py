import pygame, sys
pygame.init()
delay = 100
interval = 50
pygame.key.set_repeat(delay, interval)
screen = pygame.display.set_mode([1024, 720])
background = pygame.Surface(screen.get_size())
background.fill([255,255,255])
clock = pygame.time.Clock()
class Ball(pygame.sprite.Sprite):
    def __init__(self, image_file, location, speed):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location
        self.speed = speed
    def move(self):
        if self.rect.left <= screen.get_rect().left or \
            self.rect.right >= screen.get_rect().right:
            self.speed[0] = -self.speed[0]
        newpos = self.rect.move(self.speed)
        self.rect = newpos
my_ball = Ball("ball.jpg", [10,0],[20,20])
running = True
help_down = False
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            help_down = True
        elif event.type ==  pygame.MOUSEBUTTONUP:
            help_down = False
        elif event.type == pygame.MOUSEMOTION:
            if help_down:
                my_ball.rect.center = event.pos
    clock.tick(30)
    screen.blit(background, (0,0))
    my_ball.move()
    screen.blit(my_ball.image, my_ball.rect)
    pygame.display.flip()
pygame.quit()