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

class walless_pong:
    """Defines a walless_pong game."""
    def __init__(self):
        """Initializes a walless_pong game."""
        self.game_count = 0
        self.ball = ball()
        self.human_player = player()
        self.computer_player = player(is_player=False)

    def play(self):
        """Begins a game of walless_pong"""
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
    
    def move_top_bottom_paddle(self):

    def move_middle_paddle(self):
        

class paddle:
    """Manages a paddle"""
    def __init__(self, width=50, height=10, xpos=100, ypos=100):
        """Initializes a paddle"""
        self.width = width
        self.heigh = height
        self.xpos = xpos
        self.ypos = ypos
        self.box = pygame.Rect(self.xpos, self.ypos, self.width, self.height)
        self.vector = Vector2()


class ball:
    """Manages a ball"""
    def __init__(self, width=10, height=10, xpos=150, ypos=150, xvel=10, yvel=10):
        """Initializes a paddle"""
        self.width = width
        self.height = height
        self.xpos = xpos
        self.ypos = ypos
        self.box = pygame.Rect(self.xpos, self.ypos, self.width, self.height)
        self.xvel = xvel
        self.yvel = yvel
