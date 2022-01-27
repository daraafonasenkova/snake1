import pygame
import sqlite3


pygame.init()
pygame.display.set_caption('Таблица результатов')
size = width, height = 1024, 768
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()


def data_base():
    con = sqlite3.connect("namesandresults.db")
    cur = con.cursor()
    names = cur.execute(
        '''SELECT name FROM results''').fetchall()
    res = cur.execute(
        '''SELECT result FROM results''').fetchall()
    if names:
        result = sorted(list(names), key=lambda x: x[-1], reverse=True)

    run = True
    while run:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    from Game import game_over
                    game_over()
        screen.fill((242, 99, 55))
        from Menu import print_text
        print_text('Имя             Счёт', 50, 10, color=(255, 199, 8), size=45)
        x = 50
        y = 35
        for i in names:
            y += 21
            print_text(str(i[0]), x, y, color=(255, 199, 8), size=20)
        x1 = 350
        y = 35
        for i in res:
            y += 21
            print_text(str(i[0]), x1, y, color=(255, 199, 8), size=20)
        pygame.display.update()



