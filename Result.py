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
                    from Menu import menu
                    menu()
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


   # def basa(self):
        #con = sqlite3.connect("nameandresult.db")
        #cur = con.cursor()
        #result = cur.execute(
            #'''SELECT * FROM results WHERE name LIKE ?''', (name,)).fetchall()
        #nikto, fails, wins = result[0][1], result[0][2], result[0][3]
        #if not hand.cards:
            #wins += 1
        #elif not hand2.cards:
            #fails += 1
        #else:
            #nikto += 1
        #result = cur.execute("""UPDATE
        #results SET number_nikto = ?, number_prongr = ?, number_of_wins = ?
        #WHERE name = ?""", (nikto, fails, wins, name))
        #con.commit()
        # con.close()      запись результата игры


