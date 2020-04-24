import pygame, sys, random


# classes
class player():
    def __init__(self, obj, size, position, speed, color):
        self.obj = obj
        self.size = size
        self.pos = position
        self.speed = speed
        self.color = color

class screen():
    def __init__(self, obj, x, y, mid_x, mid_y, color):
        self.obj = obj
        self.x = x
        self.y = y
        self.mid_x = mid_x
        self.mid_y = mid_y
        self.color = color


# init program
pygame.init()
clock = pygame.time.Clock()
pygame.display.set_caption("Box Game")
game_font = pygame.font.Font("freesansbold.ttf", 24)


# init objects
screen = screen()
screen.x = 1000
screen.mid_x = round(screen.x/2)
screen.y = 500
screen.mid_y = round(screen.y/2)
screen.obj = pygame.display.set_mode((screen.x,screen.y))
screen.color = (0,0,0)
player = player()
player.size = (25,25)
player.pos = (screen.mid_x - 200, screen.mid_y)
player.obj = pygame.Rect(player.pos, player.size)
player.speed = 0
player.color = (200,200,200)


# functions
def screen_update():
    screen.obj.fill(screen.color)
    pygame.draw.rect(screen.obj, player.color, player.obj)
    pygame.display.flip()

def event_handler(event):
    global player_speed
    if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_UP:
            player_speed -= 7
        if event.key == pygame.K_DOWN:
            player_speed += 7
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_UP:
            player_speed += 7
        if event.key == pygame.K_DOWN:
            player_speed -= 7


# Main Loop
while True:

    # event handler
    for event in pygame.event.get():
        event_handler(event)

    # update animations


    # screen update
    screen_update()
    clock.tick(60)
