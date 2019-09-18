""" Walless Pong
    Written by: Corey Stock
    CPSC 386
"""

import pygame, time, random
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

class settings:
    """Defines settings used for walless_pong"""
    # Game Settings
    WINDOWWIDTH = 1920
    WINDOWHEIGHT = 1080

    # Ball Settings
    BALL_SPEED_SCALE = 1
    BALL_SPEED_VECTOR = Vector2(BALL_SPEED_SCALE, BALL_SPEED_SCALE)
    BALL_RADIUS = 10
    BALL_START_POSITION = [WINDOWWIDTH/2, WINDOWHEIGHT/2]

    # CPU Settings
    CPU_PADDLE_WIDTH = 10
    CPU_PADDLE_SPEED = 10

    # Human Settings
    HUMAN_PADDLE_WIDTH = 10


    def __init__(self):


class walless_pong:
    """Defines a walless_pong game."""
    def __init__(self):
        """Initializes a walless_pong game."""
        self.game_count = 0
        self.ball = 
        self.human_player = player()
        self.computer_player = player(is_player=False)

    def play(self):
        """Begins a game of walless_pong"""

        settings = settings()

        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_LEFT or event.key == K_a:
                        """Move top and bottom paddles left"""

                        human_player.move_paddle(
                    if event.key == K_RIGHT or event.key == K_d:
                        """Move top and bottom paddles right"""
                    if event.key == K_UP or event.key == K_s:
                        """Move middle paddle up"""
                    if event.key == K_DOWN or event.key == K_w:
                        """Move middle paddle down"""
                if event.type == KEYUP:
                    if event.key == K_LEFT or event.key == K_a:
                        """Stop top and bottom paddles left"""
                        self.left_player.stop_paddle
                    if event.key == K_RIGHT or event.key == K_d:
                        """Stop top and bottom paddles right"""
                    if event.key == K_UP or event.key == K_s:
                        """Stop middle paddle up"""
                    if event.key == K_DOWN or event.key == K_w:
                        """Stop middle paddle down"""

            

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


class ball:
    """Manages a ball"""
    def __init__(self, radius=BALL_RADIUS, xpos=BALL_START_POSITION[0], ypos=BALL_START_POSITION[1], velocity=BALL_SPEED_VECTOR, color='#FFFFFF'):
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
