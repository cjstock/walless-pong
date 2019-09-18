import pygame
import math
import sys
import time
import random
from pygame.locals import *
from pygame.math import Vector2

pygame.init()

# Game Settings
WINDOWWIDTH = 1920
WINDOWHEIGHT = 1080
surf = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
FONT = pygame.font.Font('freesansbold.ttf', 42)
# Ball Settings
BALL_RADIUS = 10
BALL_START_POSITION = [WINDOWWIDTH/2, WINDOWHEIGHT/2]
BALL_COLOR = "#FFFFFF"

# Paddle Settings
MID_PAD_WIDTH = 20
MID_PAD_HEIGHT = 300
TOP_PAD_WIDTH = 300
TOP_PAD_HEIGHT = 20
BOT_PAD_WIDTH = 300
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

def get_ball_start_vector():
    BALL_SPEED_SCALE = 1
    BALL_POSS_VECT_VAL = [-x for x in range(1, 11) if x  != 0]
    BALL_SPEED_VECTOR = Vector2(random.choice(BALL_POSS_VECT_VAL) * BALL_SPEED_SCALE, random.choice(BALL_POSS_VECT_VAL) * BALL_SPEED_SCALE)
    return BALL_SPEED_VECTOR


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

class score:
    """Manages the score"""
    def __init__(self):
        self.hu_score = 10
        self.hu_needed = 11
        self.cp_score = 10
        self.cp_needed = 11
        self.color = Color("#FFFFFF")

    def update_scores(self):
        # Update hu score
        hu_text = str(self.hu_score) + '/' + str(self.hu_needed)
        hu_score_surf = FONT.render((hu_text), True, self.color)
        hu_score_rect = hu_score_surf.get_rect()
        hu_score_rect.midtop = (HU_TOP_PAD_START_POS[0] + TOP_PAD_WIDTH/2, WINDOWWIDTH/24)
        surf.blit(hu_score_surf, hu_score_rect)
        # Update cp score
        cp_text = str(self.cp_score) + '/' + str(self.cp_needed)
        cp_score_surf = FONT.render((cp_text), True, self.color)
        cp_score_rect = cp_score_surf.get_rect()
        cp_score_rect.midtop = (CP_TOP_PAD_START_POS[0] + TOP_PAD_WIDTH/2, WINDOWWIDTH/24)
        surf.blit(cp_score_surf, cp_score_rect)

    def hu_scored(self):
        self.hu_score += 1
        
        if self.hu_score == self.hu_needed and (self.hu_score - self.cp_score) >= 2:
            print("hu won")
            return True
        else:
            if self.hu_score <= 11:
                self.hu_needed = self.cp_score + 2
            return False
    def cp_scored(self):
        self.cp_score += 1

        if self.cp_score == self.cp_needed and (self.cp_score - self.hu_score) >= 2:
            print("cp won")
            return True

        else:
            if self.cp_score <= 11:
                self.cp_needed = self.hu_score + 2
            return False

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
    def __init__(self, radius=BALL_RADIUS, xpos=BALL_START_POSITION[0], ypos=BALL_START_POSITION[1], color=BALL_COLOR):
        """Initializes a ball"""
        self.radius = radius
        self.color = color
        self.xpos = xpos
        self.ypos = ypos
        self.rect = pygame.Rect(self.xpos, self.ypos, radius/2, radius/2)
        self.velocity = get_ball_start_vector()
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
        self.rect.left += self.velocity[0]
        self.rect.top += self.velocity[1]
    
    def reset(self):
        self.get_rect().left = BALL_START_POSITION[0]
        self.get_rect().top = BALL_START_POSITION[1]
        self.velocity = get_ball_start_vector()

    def bounce_x(self):
        self.velocity[0] *= -1
        self.velocity[0] += self.velocity[0] * 0.1
        self.velocity[1] += self.velocity[1] * 0.1

    def bounce_y(self):
        self.velocity[1] *= -1
        self.velocity[0] += self.velocity[0] * 0.1
        self.velocity[1] += self.velocity[1] * 0.1

def play():
    pygame.display.set_caption('Walless Pong')

    b = ball()
    h1 = human()
    c1 = cpu()
    scores = score()
    done = False
    move_left = False
    move_right = False
    move_up = False
    move_down = False

    quit_game = False
    while not quit_game and not done:
        for event in pygame.event.get():
            if event.type == QUIT:
                quit_game = True
            if event.type == KEYDOWN:
                if event.key == K_LEFT:
                    move_right = False
                    move_left = True
                if event.key == K_RIGHT:
                    move_left = False
                    move_right = True
                if event.key == K_UP:
                    move_down = False
                    move_up = True
                if event.key == K_DOWN:
                    move_up = False
                    move_down = True
            if event.type == KEYUP:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                if event.key == K_LEFT:
                    move_left = False
                if event.key == K_RIGHT:
                    move_right = False
                if event.key == K_UP:
                    move_up = False
                if event.key == K_DOWN:
                    move_down = False

        if move_down and h1.mid_paddle.rect.bottom < h1.bot_paddle.rect.top:
            h1.mid_paddle.rect.top += HU_PAD_SPEED_SCALE
        if move_up and h1.mid_paddle.rect.top > h1.top_paddle.rect.bottom:
            h1.mid_paddle.rect.top -= HU_PAD_SPEED_SCALE
        if move_left and h1.top_paddle.rect.left > h1.mid_paddle.rect.right:
            h1.top_paddle.rect.left -= HU_PAD_SPEED_SCALE
            h1.bot_paddle.rect.left -= HU_PAD_SPEED_SCALE
        if move_right and h1.top_paddle.rect.right < WINDOWWIDTH/2:
            h1.top_paddle.rect.left += HU_PAD_SPEED_SCALE
            h1.bot_paddle.rect.left += HU_PAD_SPEED_SCALE


        surf.fill(Color('#000000'))

        if(done):
            # reset game
            pass

        b.update()

        # Bounce off verticle paddles
        vert_paddles = [h1.mid_paddle, c1.mid_paddle]
        for pad in vert_paddles:
            if b.rect.colliderect(pad):
                b.bounce_x()

        # Bounce off horizontal paddles
        horiz_paddles = [h1.top_paddle, h1.bot_paddle, c1.top_paddle, c1.bot_paddle]
        for pad in horiz_paddles:
            if b.rect.colliderect(pad):
                b.bounce_y()


        # Change this logic to score points
        if b.get_rect().left <= 0:
            done = scores.cp_scored()
            b.reset()
        if b.get_rect().right >= WINDOWWIDTH:
            done = scores.hu_scored()
            b.reset()

        if b.get_rect().top <= 0:
            if b.get_center()[0] >= WINDOWWIDTH/2:
                done = scores.hu_scored()
            else:
                done = scores.cp_scored()
            b.reset()

        if b.get_rect().bottom >= WINDOWHEIGHT:
            if b.get_center()[0] >= WINDOWWIDTH/2:
                done = scores.hu_scored()
            else:
                done = scores.cp_scored()
            b.reset()

        scores.update_scores()   

        h1.draw_paddles()
        c1.draw_paddles()

        pygame.draw.circle(surf, b.get_color(), b.get_center(), b.get_radius())
        pygame.display.update()
        time.sleep(1/60)

    pygame.quit()
    sys.exit()

play()
