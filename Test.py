import pygame, sys, random


# init program
pygame.init()
clock = pygame.time.Clock()
pygame.display.set_caption("Box Game")
game_font = pygame.font.Font("freesansbold.ttf", 24)


# classes
class screen():
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        self.mid_x = x/2
        self.mid_y = y/2
        self.obj = pygame.display.set_mode((x,y))


# init objects
screen = screen(1000, 500, (0,0,0))

# functions
def screen_update():
    screen.obj.fill(screen.color)
    pygame.display.flip()

def event_handler(event):
    global player_speed
    if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()


# Main Loop
while True:

    # event handler
    for event in pygame.event.get():
        event_handler(event)

    # update animations


    # screen update
    screen_update()
    clock.tick(60)













    https://www.youtube.com/watch?v=ZDa-Z5JzLYM
