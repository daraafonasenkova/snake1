from Result import *


pygame.init()
pygame.display.set_caption('Змейка')
size = width, height = 700, 800
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

pygame.mixer.music.load('pixsound.mp3')
pygame.mixer.music.play(-1)


class Buttons():
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def draw(self, x, y, text, action=None, size=30):
        mouse_pos = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if x < mouse_pos[0] < x + self.width and y < mouse_pos[1] < y + self.height:
            pygame.draw.rect(screen, (1, 78, 127), (x, y, self.width, self.height))
            if click[0] == 1 and action is not None:
                if action == quit:
                    pygame.quit()
                else:
                    action()

        else:
            pygame.draw.rect(screen, (242, 99, 55), (x, y, self.width, self.height))

        print_text(text=text, x=x + 10, y=y + 10, size=size)


def print_text(text, x, y, color=(255, 199, 8), font_type='Pixel Times.ttf', size=30):
    font_type = pygame.font.Font(font_type, size)
    text_ = font_type.render(text, True, color)
    screen.blit(text_, (x, y))


def menu():
    back = pygame.image.load('fon.xcf')

    start = Buttons(270, 80)
    exit = Buttons(270, 80)

    show = True

    while show:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                show = False
        screen.blit(back, (0, 0))
        start.draw(400, 510, 'Играть', name_input, 50)
        exit.draw(400, 650, 'Выход', quit, 50)  # не знаю почему возникает ошибка

        pygame.display.update()
        clock.tick(60)


input_name = ''

def name_input():
    show = True

    need_input = False
    global input_name

    while show:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                show = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    menu()
            if need_input and event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    need_input = False
                    zapis_name_base()
                    start_game()
                elif event.key == pygame.K_BACKSPACE:
                    input_name = input_name[:-1]
                else:
                    if len(input_name) < 11:
                        input_name += event.unicode

        screen.fill((242, 99, 55))
        pygame.draw.rect(screen, (243, 145, 28),
                         (200, 320, 300, 53), 10)
        pygame.draw.rect(screen, (243, 145, 28),
                         (200, 250, 300, 53))
        print_text("Введите имя", 220, 260, color=(255, 199, 8), font_type='Pixel Times.ttf', size=40)

        keys = pygame.key.get_pressed()

        if keys[pygame.K_SPACE]:
            need_input = True

        print_text(input_name, 220, 330, color=(255, 199, 8))

        pygame.display.update()
        clock.tick(60)

def zapis_name_base():
    con = sqlite3.connect("namesandresults.db")
    cur = con.cursor()
    res = cur.execute(
        '''SELECT * FROM results WHERE name LIKE ?''', (input_name,)).fetchall()
    if not res:
        res = cur.execute("""INSERT INTO results(name, result
                           ) VALUES(?,?)""", (input_name, 0)).fetchall()
    con.commit()
    con.close()


def start_game():
    # print(1)
    result_tabel = Buttons(260, 40)
    run = True
    while run:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    menu()

        screen.fill((242, 99, 55))
        pygame.draw.rect(screen, (255, 199, 8),
                         (10, 60, 680, 700), 5)
        print_text(f"Игрок {input_name}", 20, 20, color=(255, 199, 8))
        result_tabel.draw(430, 20, 'Посмотреть результаты', data_base, 20)
        pygame.display.update()