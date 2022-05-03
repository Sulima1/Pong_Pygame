import pygame, os
from paddle import Paddle
from ball import Ball
pygame.init()

WHITE = (255, 255, 255)
GREEN = (56, 121, 7) #background color

FPS = 60
VEL = 5

WIDTH, HEIGHT = 700, 500

PADDLE_WIDTH, PADDLE_HEIGHT = 10, 100

BALL_X_MAX = 690
BALL_Y_MAX = 490
BALL_XY_MIN = 0


WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Pong')


def draw_window(ball, paddleA, paddleB, all_sprites_list):
    WIN.fill(GREEN)
    pygame.draw.line(WIN, WHITE, [349, 0], [349, 500], 5)
    all_sprites_list.draw(WIN)
    
    pygame.display.update()

def paddle_movement(keys_pressed, paddleA, paddleB):
    if keys_pressed[pygame.K_w]:
        paddleA.rect.y -= VEL
    if keys_pressed[pygame.K_s]:
        paddleA.rect.y += VEL
    if keys_pressed[pygame.K_UP]:
        paddleB.rect.y -= VEL
    if keys_pressed[pygame.K_DOWN]:
        paddleB.rect.y += VEL

def ball_movement(ball):
    if ball.rect.x >= BALL_X_MAX:
        ball.velocity[0] = -ball.velocity[0]
    if ball.rect.x <= BALL_XY_MIN:
        ball.velocity[0] = -ball.velocity[0]
    if ball.rect.y > BALL_Y_MAX:
        ball.velocity[1] = -ball.velocity[1]
    if ball.rect.y < BALL_XY_MIN:
        ball.velocity[1] = -ball.velocity[1]

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

        all_sprites_list.update()

        ball_movement(ball)
        handle_collision(ball, paddleA, paddleB)

        keys_pressed = pygame.key.get_pressed()
        paddle_movement(keys_pressed, paddleA, paddleB)

        draw_window(ball, paddleA, paddleB, all_sprites_list)

    main()

if __name__ == "__main__":
    main()