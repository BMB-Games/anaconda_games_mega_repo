import pygame

WIDTH = 640
HEIGHT = 480

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)
pygame.display.set_caption("Test")
screen.fill((0, 0, 0))

ball = pygame.image.load("./images/football.png")

game_over = False

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
    screen.blit(ball, (WIDTH//2 - ball.get_width()//2, HEIGHT//2 - ball.get_height()//2))
    pygame.display.update()


pygame.quit()
