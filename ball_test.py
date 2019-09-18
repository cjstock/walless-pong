
import pygame
import sys
import time
from pygame.locals import *
from pygame.math import Vector2

# Game Settings
WINDOWWIDTH = 1920
WINDOWHEIGHT = 1080
surf = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)

# Ball Settings
BALL_SPEED_SCALE = 10
BALL_SPEED_VECTOR = Vector2(1 * BALL_SPEED_SCALE, 2 * BALL_SPEED_SCALE)
BALL_RADIUS = 10
BALL_START_POSITION = [WINDOWWIDTH/2, WINDOWHEIGHT/2]
BALL_COLOR = "#FFFFFF"


class ball:
    """Manages a ball"""
    def __init__(self, radius=BALL_RADIUS, xpos=BALL_START_POSITION[0], ypos=BALL_START_POSITION[1], velocity=BALL_SPEED_VECTOR, color=BALL_COLOR):
        """Initializes a ball"""
        self.radius = radius
        self.color = color
        self.xpos = xpos
        self.ypos = ypos
        self.rect = pygame.Rect(self.xpos, self.ypos, radius/2, radius/2)
        self.velocity = velocity
    def __str__(self):
        return 'Ball: rect={}, velocity={}'.format(self.rect, self.velocity)

    def get_velocity(self):
        return self.velocity
    
    def set_velocity(self, dx=1, dy=1):
        if dx > 0:
            pass
        else:
            self.velocity[0] *= -1
        if dy > 0:
            pass
        else:
            self.velocity[1] *= -1

    def get_color(self):
        return Color(self.color)

    def get_radius(self):
        return self.radius

    def get_rect(self):
        return self.rect

    def get_center(self):
        return (self.rect.left + self.radius, self.rect.top + self.radius)

    def move_ball(self):
        self.rect.left += self.velocity[0]
        self.rect.top += self.velocity[1]

    def bounce(self):
        pass



def play():
    pygame.display.set_caption('Walless Pong')

    b = ball()

    quit_game = False
    while not quit_game:
        for event in pygame.event.get():
            if event.type == QUIT:
                quit_game = True
        surf.fill(Color('#000000'))

        b.move_ball()



        pygame.draw.circle(surf, b.get_color(), b.get_center(), b.get_radius())
        pygame.display.update()
        time.sleep(0.02)

    pygame.quit()
    sys.exit()

play()
