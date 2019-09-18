import pygame
import sys
import time
from pygame.locals import *
from pygame.math import Vector2


# Game Settings
WINDOWWIDTH = 1920
WINDOWHEIGHT = 1080

# Ball Settings
BALL_SPEED_SCALE = 10
BALL_SPEED_VECTOR = Vector2(BALL_SPEED_SCALE, BALL_SPEED_SCALE)
BALL_RADIUS = 10
BALL_START_POSITION = [WINDOWWIDTH/2, WINDOWHEIGHT/2]
BALL_COLOR = "#FFFFFF"

# Paddle Settings
MID_PAD_WIDTH = 20
MID_PAD_HEIGHT = 200
TOP_PAD_WIDTH = 200
TOP_PAD_HEIGHT = 20
BOT_PAD_WIDTH = 200
BOT_PAD_HEIGHT = 20
PAD_COLOR = "#FF0000"

# Human Settings
HU_MID_PAD_START_POS = [WINDOWWIDTH/8, WINDOWHEIGHT/2 - MID_PAD_HEIGHT/2]
HU_TOP_PAD_START_POS = [WINDOWWIDTH/8, WINDOWHEIGHT/8]
HU_BOT_PAD_START_POS = [WINDOWWIDTH/8, WINDOWHEIGHT - HU_TOP_PAD_START_POS[1]]
HU_PAD_SPEED_SCALE = 10

# CPU Settings
CP_MID_PAD_START_POS = [WINDOWWIDTH - HU_MID_PAD_START_POS[0], HU_MID_PAD_START_POS[1]]
CP_TOP_PAD_START_POS = [WINDOWWIDTH - HU_TOP_PAD_START_POS[0] - TOP_PAD_WIDTH, HU_TOP_PAD_START_POS[1]]
CP_BOT_PAD_START_POS = [CP_TOP_PAD_START_POS[0], HU_BOT_PAD_START_POS[1]]
CP_PAD_SPEED_SCALE = 10


PADDLE_TYPE = {
        "HU_MID": pygame.Rect(HU_MID_PAD_START_POS[0], HU_MID_PAD_START_POS[1], MID_PAD_WIDTH, MID_PAD_HEIGHT),
        "HU_TOP": pygame.Rect(HU_TOP_PAD_START_POS[0], HU_TOP_PAD_START_POS[1], TOP_PAD_WIDTH, TOP_PAD_HEIGHT),
        "HU_BOT": pygame.Rect(HU_BOT_PAD_START_POS[0], HU_BOT_PAD_START_POS[1], BOT_PAD_WIDTH, BOT_PAD_HEIGHT),
        "CP_MID": pygame.Rect(CP_MID_PAD_START_POS[0], CP_MID_PAD_START_POS[1], MID_PAD_WIDTH, MID_PAD_HEIGHT),
        "CP_TOP": pygame.Rect(CP_TOP_PAD_START_POS[0], CP_TOP_PAD_START_POS[1], TOP_PAD_WIDTH, TOP_PAD_HEIGHT),
        "CP_BOT": pygame.Rect(CP_BOT_PAD_START_POS[0], CP_BOT_PAD_START_POS[1], BOT_PAD_WIDTH, BOT_PAD_HEIGHT)}

class paddle:
    """Manages a paddle"""
    def __init__(self, speed, paddle_type):
        self.speed = speed
        self.paddle_type = paddle_type
        self.rect = PADDLE_TYPE[paddle_type]
        self.color = color

    def get_rect(self):
        return self.rect

    def get_speed(self):
        return self.speed

    def get_color(self):
        return Color(self.color)

# class human:
#     """Manages a player"""
#     def ___init___(self, speed=HU_PAD_SPEED_SCALE):
#         self.speed = speed
#         self.score = 0
#         self.games_wons = 0

#         self.middle_paddle = paddle(pos=HU_MID_PAD_START_POS, speed=self.speed)


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

        
def play():
    surf = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
    pygame.display.set_caption('Walless Pong')

    b = ball()
    h1 = paddle(HU_PAD_SPEED_SCALE, "HU_TOP")
    h2 = paddle(HU_PAD_SPEED_SCALE, "HU_MID")
    h3 = paddle(HU_PAD_SPEED_SCALE, "HU_BOT")
    c1 = paddle(CP_PAD_SPEED_SCALE, "CP_TOP")
    c2 = paddle(CP_PAD_SPEED_SCALE, "CP_MID")
    c3 = paddle(CP_PAD_SPEED_SCALE, "CP_BOT")

    print(b)

    quit_game = False
    while not quit_game:
        for event in pygame.event.get():
            if event.type == QUIT:
                quit_game = True
        surf.fill(Color('#000000'))

        b.move_ball()
        if b.get_rect().left <= 0 or b.get_rect().right >= WINDOWWIDTH:
            b.get_velocity()[0] *= -1
        if b.get_rect().top <= 0 or b.get_rect().bottom >= WINDOWHEIGHT:
            b.get_velocity()[1] *= -1

        pygame.draw.rect(surf, Color(PAD_COLOR), h1.get_rect())
        pygame.draw.rect(surf, Color(PAD_COLOR), h2.get_rect())
        pygame.draw.rect(surf, Color(PAD_COLOR), h3.get_rect())
        pygame.draw.rect(surf, Color(PAD_COLOR), c1.get_rect())
        pygame.draw.rect(surf, Color("#0000FF"), c2.get_rect())
        pygame.draw.rect(surf, Color("#FFFFFF"), c3.get_rect())
        pygame.draw.circle(surf, b.get_color(), b.get_center(), b.get_radius())
        pygame.display.update()
        time.sleep(0.02)

    pygame.quit()
    sys.exit()

play()
