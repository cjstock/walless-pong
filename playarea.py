import pygame
import math
import sys
import time
import random
from pygame.locals import *
from pygame.math import Vector2


# Game Settings
WINDOWWIDTH = 1920
WINDOWHEIGHT = 1080
surf = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)

# Ball Settings
BALL_SPEED_SCALE = 20
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

# Human Settings
HU_MID_PAD_START_POS = [WINDOWWIDTH/8, WINDOWHEIGHT/2 - MID_PAD_HEIGHT/2]
HU_TOP_PAD_START_POS = [WINDOWWIDTH/8, WINDOWHEIGHT/8]
HU_BOT_PAD_START_POS = [WINDOWWIDTH/8, WINDOWHEIGHT - HU_TOP_PAD_START_POS[1]]
HU_PAD_SPEED_SCALE = 10
HU_PAD_COLOR = Color("#FF0000")

# CPU Settings
CP_MID_PAD_START_POS = [WINDOWWIDTH - HU_MID_PAD_START_POS[0], HU_MID_PAD_START_POS[1]]
CP_TOP_PAD_START_POS = [WINDOWWIDTH - HU_TOP_PAD_START_POS[0] - TOP_PAD_WIDTH, HU_TOP_PAD_START_POS[1]]
CP_BOT_PAD_START_POS = [CP_TOP_PAD_START_POS[0], HU_BOT_PAD_START_POS[1]]
CP_PAD_SPEED_SCALE = 10
CP_PAD_COLOR = Color("#00FF00")



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

class human:
    """Manages a human player"""
    def __init__(self, speed=HU_PAD_SPEED_SCALE):
        self.speed = speed
        self.score = 0
        self.games_won = 0
        self.top_paddle = paddle(speed, "HU_TOP")
        self.mid_paddle = paddle(speed, "HU_MID")
        self.bot_paddle = paddle(speed, "HU_BOT")

    def get_speed(self):
        return self.speed

    def get_score(self):
        return self.score

    def get_games_won(self):
        return self.games_won

    def scored(self):
        self.score += 1

    def reset_score(self):
        self.score = 0

    def reset_games_won(self):
        self.games_won = 0

    def get_paddles(self):
        return [self.top_paddle, self.mid_paddle, self.bot_paddle]

    def draw_paddles(self):
        for pad in self.get_paddles():
            pygame.draw.rect(surf, HU_PAD_COLOR, pad.get_rect())

class cpu:
    """Managed a CPU player"""
    def __init__(self, speed=CP_PAD_SPEED_SCALE):
        self.speed = speed
        self.score = 0
        self.games_won = 0
        self.top_paddle = paddle(speed, "CP_TOP")
        self.mid_paddle = paddle(speed, "CP_MID")
        self.bot_paddle = paddle(speed, "CP_BOT")

    def get_speed(self):
        return self.speed

    def get_score(self):
        return self.score

    def get_games_won(self):
        return self.games_won

    def scored(self):
        self.score += 1

    def reset_score(self):
        self.score = 0

    def reset_games_won(self):
        self.games_won = 0

    def get_paddles(self):
        return [self.top_paddle, self.mid_paddle, self.bot_paddle]

    def draw_paddles(self):
        for pad in self.get_paddles():
            pygame.draw.rect(surf, CP_PAD_COLOR, pad.get_rect())


class ball:
    """Manages a ball"""
    def __init__(self, radius=BALL_RADIUS, xpos=BALL_START_POSITION[0], ypos=BALL_START_POSITION[1], velocity=BALL_SPEED_VECTOR, color=BALL_COLOR):
        """Initializes a ball"""
        self.radius = radius
        self.color = color
        self.xpos = xpos
        self.ypos = ypos
        self.direction = 0
        self.rect = pygame.Rect(self.xpos, self.ypos, radius/2, radius/2)
        self.velocity = velocity
        self.speed = 10
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

    def update(self):
        direction_radians = math.radians(self.direction)

        self.xpos += self.speed * math.sin(direction_radians)
        self.ypos -= self.speed * math.cos(direction_radians)

        self.rect.left += self.xpos
        self.rect.top += self.ypos
    
    def reset(self):
        self.get_rect().left = BALL_START_POSITION[0]
        self.get_rect().top = BALL_START_POSITION[1]
        # self.direction = random.randrange(-45, 45)

    def bounce_x(self, diff):
        self.direction = (180-self.direction)%360
        self.direction -= diff


def play():
    pygame.display.set_caption('Walless Pong')

    b = ball()
    h1 = human()
    c1 = cpu()

    quit_game = False
    while not quit_game:
        for event in pygame.event.get():
            if event.type == QUIT:
                quit_game = True
        surf.fill(Color('#000000'))

        b.update()

        # Get all paddles
        human_paddles = h1.get_paddles()
        cpu_paddles = c1.get_paddles()
        # Get their rects
        human_rects = [ r.get_rect() for r in human_paddles]
        cpu_rects = [ r.get_rect() for r in cpu_paddles]
        # any_rects = human_rects + cpu_rects

        if b.rect.colliderect(c1.mid_paddle.rect):
            diff = (c1.mid_paddle.rect.x + c1.mid_paddle.rect.width/2) - (b.rect.x + b.width/2)

            b.bounce_x(diff)

        # # bounce off right mid paddle's left
        # if b.get_rect().right >= c1.mid_paddle.get_rect().left and b.get_rect().top <= c1.mid_paddle.get_rect().bottom and b.get_rect().bottom >= c1.mid_paddle.get_rect().top:
        #     b.get_velocity()[0] *= -1
        # # bounce off left mid paddle's right
        # if b.get_rect().left <= h1.mid_paddle.get_rect().right and b.get_rect().top <= h1.mid_paddle.get_rect().bottom and b.get_rect().bottom >= h1.mid_paddle.get_rect().top:
        #     b.get_velocity()[0] *= -1
        # # bounce off left mid paddles top
        # if b.get_rect().bottom == h1.mid_paddle.get_rect().top and b.get_rect().left <= h1.mid_paddle.get_rect().right:
        #     b.get_velocity()[1] *= -1
        # # bounce off left mid paddles top
        # if b.get_rect().bottom == h1.mid_paddle.get_rect().top and b.get_rect().right >= h1.mid_paddle.get_rect().left:
        #     b.get_velocity()[1] *= -1

        # # bounce off left mid paddles bot
        # if b.get_rect().top == h1.mid_paddle.get_rect().bottom and b.get_rect().left <= h1.mid_paddle.get_rect().right:
        #     b.get_velocity()[1] *= -1

        # # bounce off left mid paddles bot
        # if b.get_rect().top == h1.mid_paddle.get_rect().bottom and b.get_rect().right >= h1.mid_paddle.get_rect().left:
        #     b.get_velocity()[1] *= -1



        # Change this logic to score points
        if b.get_rect().left <= 0:
            c1.scored()
            b.reset()
        if b.get_rect().right >= WINDOWWIDTH:
            h1.scored()
            b.reset()

        if b.get_rect().top <= 0:
            if b.xpos >= WINDOWWIDTH/2:
                h1.scored()
            else:
                c1.scored()
            b.reset()

        if b.get_rect().bottom >= WINDOWHEIGHT:
            if b.xpos >= WINDOWWIDTH/2:
                h1.scored()
            else:
                c1.scored()
            b.reset()

        h1.draw_paddles()
        c1.draw_paddles()

        pygame.draw.circle(surf, b.get_color(), b.get_center(), b.get_radius())
        pygame.display.update()
        time.sleep(0.02)

    pygame.quit()
    sys.exit()

play()
