import pygame, sys, random

# init program
pygame.init()
clock = pygame.time.Clock()
pygame.display.set_caption("Box Game")
game_font = pygame.font.Font("freesansbold.ttf", 24)

# classes
class screen():
    def __init__(self, w, h, color):
        self.w = w
        self.h = h
        self.color = color
        self.mid_w = w/2
        self.mid_h = h/2
        self.obj = pygame.display.set_mode((w,h))
class player():
    def __init__(self, start_w, start_h, start_x, start_y, color):
        self.start_w = start_w
        self.start_h = start_h
        self.start_x = start_x
        self.start_y = start_y
        self.color = color
        self.obj = pygame.Rect(start_x, start_y, start_w, start_h)
        self.jumping = False
        self.speed_x = 0
        self.speed_y = 0
    def gravity(self):
        if self.obj.colliderect(platform.obj):
            self.obj.bottom = platform.obj.top + 1
        else: self.obj.y += 8
    def jump(self):
        #add check that player is jumping from ground and cannot jump again till touch ground again
        self.jumping = True
        player.speed_y = 24

class platform():
    def __init__(self, start_w, start_h, start_x, start_y, color):
        self.start_w = start_w
        self.start_h = start_h
        self.start_x = start_x
        self.start_y = start_y
        self.color = color
        self.obj = pygame.Rect(start_x, start_y, start_w, start_h)
    def move(self):
        self.obj.x -= 3.2


# init objects
screen = screen(1000, 500, (0,0,0))
player = player(25, 25, round(screen.mid_w - 300), round(screen.mid_h), (200,200,200))
platform = platform(100, 25, round(screen.mid_w - 300), round(screen.mid_h + 200), (50,255,50))

# functions
def event_handler(event):

    if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_SPACE:
            player.jump()
def screen_update():
    screen.obj.fill(screen.color)
    pygame.draw.rect(screen.obj, player.color, player.obj)
    pygame.draw.rect(screen.obj, platform.color, platform.obj)
    pygame.display.flip()


# Main Loop
while True:

    # event handler
    for event in pygame.event.get():
        event_handler(event)

    # update animations
    if player.jumping:
        player.obj.y -= player.speed_y
        player.speed_y -= 1
        if player.speed_y <= 0:
            player.jumping = False
    else:player.gravity()

    # screen update
    screen_update()
    clock.tick(60)
