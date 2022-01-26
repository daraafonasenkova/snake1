import random
import pygame
from Result import *


pygame.init()
pygame.display.set_caption('Змейка')
size = width, height = 700, 800
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()


def message():
    from Menu import print_text
    from Menu import Buttons
    from Menu import menu

    result_tabel = Buttons(260, 40)
    exit_menu = Buttons(260, 40)
    rerun = Buttons(260, 40)

    run = True
    while run:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pass

        screen.fill((242, 99, 55))

        pygame.draw.rect(screen, (255, 199, 8),
                         (10, 60, 680, 700), 5)

        print_text("Вы врезались!", 250, 300, color=(255, 199, 8))
        result_tabel.draw(220, 340, 'Посмотреть результаты', data_base, 20)
        rerun.draw(220, 380, 'Начать заново', go_game, 20)
        exit_menu.draw(220, 420, 'Вернуться в меню', menu, 20)
        pygame.display.update()


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

        if x1 >= 680 or x1 < 0 or y1 >= 700 or y1 < 0:
            run = False
            message()

        x1 += x1_change
        y1 += y1_change

        screen.fill((242, 99, 55))

        pygame.draw.rect(screen, (255, 199, 8),
                         (10, 60, 680, 700), 5)  # границы
        from Menu import input_name, print_text
        print_text(f"Игрок {input_name}", 20, 20, color=(255, 199, 8))

        pygame.draw.rect(screen, (142, 200, 62),
                         (x1, y1, 40, 40))  # змейка

        pygame.display.update()
        clock.tick(30)
