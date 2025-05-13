import os.path

import pygame

WIDTH = 640
HEIGHT = 480

base_path = os.path.dirname(os.path.abspath(__file__))
imag_path = os.path.join(base_path, "images", "football.png")


pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)
pygame.display.set_caption("Test")
screen.fill((0, 0, 0))

ball = pygame.image.load(imag_path)
ball = pygame.transform.scale(ball, (24, 24))

ball_y = HEIGHT//2 - ball.get_height()//2
ball_x = WIDTH//2 - ball.get_width()//2

game_over = False

while not game_over:
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT and ball_x + ball.get_width() < WIDTH:
                ball_x += 10
            elif event.key == pygame.K_LEFT and ball_x > 0:
                ball_x -= 10

    screen.blit(ball, (ball_x, ball_y))
    pygame.display.update()


pygame.quit()
