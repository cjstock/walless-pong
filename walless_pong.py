""" Walless Pong
    Written by: Corey Stock
    CPSC 386
"""

import pygame, time, random
from pygame.locals import *
from pygame.math import Vector2

# pygame settings
WINDOWWIDTH = 1920
WINDOWHEIGHT = 1080
window_surface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
pygame.display.set_caption('Walless Pong')

# set colors
WHITE = ('#FFFFFF')

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

            

class player:
    """Manages a player"""
    def __init__(self, is_player=True, speed=10):
        """ Initializes a player instance. Defaults to creating a human player, but can create a computer by passing False."""
        self.score = 0
        self.paddle_speed = speed
        self.top_paddle = paddle()
        self.bottom_paddle = paddle()
        self.middle_paddle = paddle()

    def scored(self):
        self.score += 1

    def score_reset(self):
        self.score = 0

    def get_top_bottom_paddles(self):
        return (self.top_paddle, self.bottom_paddle)

    def get_middle_paddle(self):
        return self.middle_paddle
    

class paddle:
    """Manages a paddle"""
    def __init__(self, width=50, height=10, xpos=100, ypos=100):
        """Initializes a paddle"""
        self.width = width
        self.heigh = height
        self.xpos = xpos
        self.ypos = ypos
        self.vector = Vector2()


class ball:
    """Manages a ball"""
    def __init__(self, radius=10, xpos=BALL_START_POSITION[0], ypos=BALL_START_POSITION[1], velocity=BALL_SPEED_VECTOR, color=(255,255,255)):
        """Initializes a ball"""
        self.radius = radius
        self.color = color
        self.xpos = xpos
        self.ypos = ypos
        self.rect = pygame.Rect(self.xpos, self.ypos, radius/2, radius/2)
        self.velocity = velocity
    def __str__(self):
        return 'Ball: rect={}, velocity={}'.format(self.box, self.velocity)

    def get_velocity(self):
        return self.velocity

    def get_rect(self):
        return self.rect

    def move_ball(self):
        self.rect.left += self.velocity[0]
        self.rect.top += self.velocity[1]
