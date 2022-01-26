import random
import pygame


pygame.init()
pygame.display.set_caption('Змейка')
size = width, height = 700, 800
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()


def go_game():

    x1 = 330
    y1 = 370

    x1_change = 0
    y1_change = 0

    from Menu import menu
    run = True
    while run:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    menu()
                if event.key == pygame.K_LEFT:
                    x1_change = -10
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = 10
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -10
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = 10
                    x1_change = 0

        x1 += x1_change
        y1 += y1_change

        screen.fill((242, 99, 55))

        pygame.draw.rect(screen, (255, 199, 8),
                         (10, 60, 680, 700), 5)

        pygame.draw.rect(screen, (142, 200, 62),
                         (x1, y1, 40, 40)) #змейка

        pygame.display.update()
        clock.tick(30)
