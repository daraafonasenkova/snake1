from Menu import *
from Game import *
import sys

if __name__ == '__main__':
    menu()
    pygame.quit()
    quit()


def start_game():
    # print(1)
    result_tabel = Buttons(260, 40)
    run = True
    while run:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                run = False
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    menu()

        screen.fill((242, 99, 55))
        pygame.draw.rect(screen, (255, 199, 8),
                         (10, 60, 680, 700), 5)
        print_text(f"Игрок {input_name}", 20, 20, color=(255, 199, 8))
        result_tabel.draw(430, 20, 'Посмотреть результаты', data_base, 20)
        pygame.display.update()