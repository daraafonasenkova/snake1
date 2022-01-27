import random
import pygame
from Result import *


pygame.init()
pygame.display.set_caption('Змейка')
size = width, height = 700, 800
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()


def game_over():
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


def snake(list, w, h, color):
    for i in list:
        pygame.draw.rect(screen, color,
                         (i[0], i[1], w, h))  # змейка



scor = 0


def score(sco, col):
    from Menu import print_text
    from Menu import input_name
    print_text(f"Ваш счёт {sco}", 450, 20, color=col)
    con = sqlite3.connect("namesandresults.db")
    cur = con.cursor()
    res = cur.execute(
        """UPDATE results SET result = ? WHERE name = ?""", (sco, input_name))
    con.commit()
    con.close()

def go_game():
    from Menu import Buttons
    next_complexity = Buttons(220, 35)
    global score
    snake_speed = 30

    x1 = width / 2
    y1 = height / 2

    x1_change = 0
    y1_change = 0

    snake_list = []
    lensnake = 1

    foodx = round(random.randrange(20, width - 40) / 10.0) * 10.0
    foody = round(random.randrange(100, width - 40) / 10.0) * 10.0  # генерация еды

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
                    x1_change = 0  # управление змейкой

        if x1 >= 680 or x1 < 0 or y1 >= 700 or y1 < 0:
            run = False
            game_over()

        x1 += x1_change
        y1 += y1_change

        screen.fill((242, 99, 55))

        pygame.draw.rect(screen, (255, 199, 8),
                         (10, 60, 680, 700), 5)  # границы

        from Menu import input_name, print_text
        print_text(f"Игрок {input_name}", 20, 20, color=(255, 199, 8))

        pygame.draw.rect(screen, (243, 145, 28),
                         (foodx, foody, 40, 40))  # еда для змейки

        next_complexity.draw(20, 760, 'Другая сложность', go_game_complexity, 20)


        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)
        if len(snake_list) > lensnake:
            del snake_list[0]

        for x in snake_list[:-1]:
            if x == snake_head:
                run = False
                game_over()


        snake(snake_list, 40, 40, (142, 200, 62))
        scor = lensnake - 1
        score(scor, (255, 199, 8))

        pygame.display.update()

        for i in range(int(foodx - 39), int(foodx + 39)):
            for j in range(int(foody - 39), int(foody + 39)):
                if x1 == i and y1 == j:
                    foodx = round(random.randrange(20, width - 40) / 10.0) * 10.0
                    foody = round(random.randrange(100, width - 40) / 10.0) * 10.0
                    lensnake += 1

        clock.tick(snake_speed)


def go_game_complexity():  # тут змейка маленькая и бешеная
    from Menu import Buttons
    next_complexity = Buttons(220, 35)
    global score
    snake_speed = 50

    x1 = width / 2
    y1 = height / 2

    x1_change = 0
    y1_change = 0

    snake_list = []
    lensnake = 1

    foodx = round(random.randrange(20, width - 20) / 10.0) * 10.0
    foody = round(random.randrange(100, width - 20) / 10.0) * 10.0  # генерация еды

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
                    x1_change = 0  # управление змейкой

        if x1 >= 680 or x1 < 0 or y1 >= 700 or y1 < 0:
            run = False
            game_over()

        x1 += x1_change
        y1 += y1_change

        screen.fill((142, 200, 62))

        pygame.draw.rect(screen, (242, 99, 55),
                         (10, 60, 680, 700), 5)  # границы

        from Menu import input_name, print_text
        print_text(f"Игрок {input_name}", 20, 20, color=(242, 99, 55))

        pygame.draw.rect(screen, (242, 99, 55),
                         (foodx, foody, 20, 20))  # еда для змейки
        next_complexity.draw(20, 760, 'Другая сложность', go_game_complexity, 20)


        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)
        if len(snake_list) > lensnake:
            del snake_list[0]

        for x in snake_list[:-1]:
            if x == snake_head:
                run = False
                game_over()


        snake(snake_list, 20, 20, (1, 78, 127))
        scor = lensnake - 1
        score(scor, (242, 99, 55))

        pygame.display.update()

        for i in range(int(foodx - 19), int(foodx + 19)):
            for j in range(int(foody - 19), int(foody + 19)):
                if x1 == i and y1 == j:
                    foodx = round(random.randrange(20, width - 20) / 10.0) * 10.0
                    foody = round(random.randrange(100, width - 20) / 10.0) * 10.0
                    lensnake += 1

        clock.tick(snake_speed)
