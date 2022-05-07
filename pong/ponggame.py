#TO DO LIST

#ADD TIMER BEFORE BALL MOVES 
#ADD AUDIO
#IF PLAYER HITS 5 POINTS -> ANNOUNCE WINNER -> RESTART

import pygame, os, random
from paddle import Paddle
from ball import Ball
pygame.init()
pygame.font.init()

#colours
WHITE = (192, 192, 192)
BACKGROUND = (12, 35, 83) #background color

#frames
FPS = 60
VEL = 5

#screen dimensions
WIDTH, HEIGHT = 700, 500

#sprite dimensions/positions
PADDLE_WIDTH, PADDLE_HEIGHT = 10, 100
BALL_X_MAX = 690
BALL_Y_MAX = 490

#font
SCORE_FONT = pygame.font.Font("freesansbold.ttf", 40)

#scores
scoreA = 0
scoreB = 0


WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Pong')


def draw_window(ball, paddleA, paddleB, all_sprites_list, textA, textB):

    WIN.fill(BACKGROUND)
    pygame.draw.line(WIN, WHITE, [349, 0], [349, 500], 5)
    all_sprites_list.draw(WIN)
    WIN.blit(textA, (250, 10))
    WIN.blit(textB, (420, 10))
    
    pygame.display.flip()

def paddle_movement(keys_pressed, paddleA, paddleB):

    if paddleA.rect.y + VEL > 0 and keys_pressed[pygame.K_w]:
        paddleA.rect.y -= VEL
    if paddleA.rect.bottom + VEL <= HEIGHT and keys_pressed[pygame.K_s]:
        paddleA.rect.y += VEL
    if paddleB.rect.y + VEL > 0 and keys_pressed[pygame.K_UP]:
        paddleB.rect.y -= VEL
    if paddleB.rect.bottom <= HEIGHT and keys_pressed[pygame.K_DOWN]:
        paddleB.rect.y += VEL

def handle_ball(ball):
    global scoreA, scoreB

    if ball.rect.x >= BALL_X_MAX:
        scoreA += 1
        ball_restart(ball)
    if ball.rect.x <= 0:
        scoreB += 1
        ball_restart(ball)
    if ball.rect.y > BALL_Y_MAX:
        ball.velocity[1] = -ball.velocity[1]
    if ball.rect.y < 0:
        ball.velocity[1] = -ball.velocity[1]

    return scoreA, scoreB

def ball_restart(ball):
    ball.rect.x, ball.rect.y = WIDTH/2, HEIGHT/2
    ball.velocity[0] *= random.choice((1, -1))
    ball.velocity[1] *= random.choice((1, -1))

def handle_collision(ball, paddleA, paddleB):
    if pygame.sprite.collide_mask(ball, paddleA) or pygame.sprite.collide_mask(ball, paddleB):
        ball.bounce()


def main():

    ball = Ball(WHITE, 10, 10)
    ball.rect.x = 345
    ball.rect.y = 195

    paddleA = Paddle(WHITE, PADDLE_WIDTH, PADDLE_HEIGHT)
    paddleA.rect.x, paddleA.rect.y = 20, 200

    paddleB = Paddle(WHITE, PADDLE_WIDTH, PADDLE_HEIGHT)
    paddleB.rect.x, paddleB.rect.y = 670, 200

    all_sprites_list = pygame.sprite.Group()
    all_sprites_list.add(paddleA, paddleB, ball)

    clock = pygame.time.Clock()

    status = True
    while status:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                status = False
                pygame.quit()

        textA = SCORE_FONT.render(f"{scoreA}", False, WHITE)
        textB = SCORE_FONT.render(f"{scoreB}", False, WHITE)


        all_sprites_list.update()

        handle_ball(ball)
        handle_collision(ball, paddleA, paddleB)

        keys_pressed = pygame.key.get_pressed()
        paddle_movement(keys_pressed, paddleA, paddleB)

        draw_window(ball, paddleA, paddleB, all_sprites_list, textA, textB)

    main()

if __name__ == "__main__":
    main()