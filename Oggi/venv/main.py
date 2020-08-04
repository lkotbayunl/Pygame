import pygame
from random import randint
import os
from sprites import *
import time
from controls import *

pygame.init()


def game_intro():
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                pygame.QUIT
                quit()
                main(0, 0)
        pygame.font.init()
        os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (750, 300)
        screen = pygame.display.set_mode((480, 400), pygame.NOFRAME)
        splash = pygame.image.load('./Lib/splash.png').convert_alpha()
        screen.blit(splash, (0, 0))
        pygame.display.update()


def main(speed, difficulty):
    """Основная функция инициализирует окно, подгружает png, для спрайтов.

     Инициализация всех переменных, для основного цикла.
     """
    WINDOW_HEIGHT = 800
    WINDOW_WIDTH = 1200
    OGGI_SPRITE_UP = './Lib/Oggi_up.png'
    OGGI_SPRITE_DOWN = './Lib/Oggi_down.png'
    QUANTITY_ROACHES = 10
    list_roach_coords_x = list(range(QUANTITY_ROACHES))
    list_roach_coords_y = list(range(QUANTITY_ROACHES))
    list_roach_sprites = []
    list_grave_coords_x = []
    list_grave_coords_y = []
    list_btn_coords_1_x_y = [970, 150, 255, 360]  # первый элемент списка Х, остальные Y
    os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (500, 200)
    sc = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Oggi and cockroaches")
    background = pygame.image.load('./Lib/background.jpg').convert_alpha()
    background_rect = background.get_rect(topleft=(0, 0))
    sc.blit(background, background_rect)
    oggi_hero = Oggi()

    """Создается список roache_sprite, в котором содержится количество классов Cockroach, равное QUANTITY_ROACHES"""
    roache_sprite = [Cockroach(randint(70, 890), randint(70, 650), speed, difficulty) for i in range(QUANTITY_ROACHES)]
    grave = Gravestone()
    btn = Button(sc, 200, 50)  # передает ширину и высоту кнопок
    timer = pygame.time.Clock()
    for i2 in range(QUANTITY_ROACHES):
        list_roach_sprites.append(randint(1, 3))

    """==========Основной цикл программы============="""
    while 1:

        timer.tick(60)  # FPS
        pygame.mouse.set_visible(False)

        for mousebtn in pygame.event.get():
            mouse_x = pygame.mouse.get_pos()[0]
            mouse_y = pygame.mouse.get_pos()[1]
            if mousebtn.type == pygame.QUIT:
                exit()
        """-----Вызов методов "кнопок", класса Button, при вызове передаются координаты X, Y------"""
        btn.new_game_btn(list_btn_coords_1_x_y[0], list_btn_coords_1_x_y[1], False)
        btn.diff1_btn(list_btn_coords_1_x_y[0], list_btn_coords_1_x_y[2], False)
        btn.diff2_btn(list_btn_coords_1_x_y[0], list_btn_coords_1_x_y[3], False)
        # ---------------------------------------------------

        """---------Генерация тараканов, в случайных местах-----------"""
        for i3 in range(QUANTITY_ROACHES):
            roach = roache_sprite[i3]
            x, y = roach.tick(sc, list_roach_sprites[i3])
            list_roach_coords_x[i3] = x
            list_roach_coords_y[i3] = y

        if mousebtn.type == pygame.MOUSEBUTTONDOWN:
            if mousebtn.button == 1:
                """-----Проверка, нажата ли кнопка New Game ----"""
                # передает классу player.Oggi "background",
                # "path to img sprite", coords X, Y"
                # pygame.display.update()
                oggi_hero.draw(sc, OGGI_SPRITE_DOWN, mouse_x, mouse_y)
                if list_btn_coords_1_x_y[0] < mouse_x+10 < list_btn_coords_1_x_y[0] + btn.width:
                    if list_btn_coords_1_x_y[1] < mouse_y+70 < list_btn_coords_1_x_y[1] + btn.height:
                        """ Список list_btn_coords_1x_y в 0 элементе содержит координату по Х, она одинакова, для всех
                        кнопок остальные элементы списка - координаты по Y, для остальных кнопок идут в порядке: 
                        Новая игра, Сложность 1, Сложность 2
                        """
                        btn.new_game_btn(list_btn_coords_1_x_y[0], list_btn_coords_1_x_y[1], True)
                        pygame.display.update()
                        while len(list_roach_coords_x) > 0:
                            del list_roach_coords_x[len(list_roach_coords_x)-1]
                            del list_roach_coords_y[len(list_roach_coords_x)-1]
                        main(0, 0)
                """------Проверка, нажата ли кнопка Сложность 1----------------"""
                if list_btn_coords_1_x_y[0] < mouse_x + 10 < list_btn_coords_1_x_y[0] + btn.width:
                    if list_btn_coords_1_x_y[2] < mouse_y + 70 < list_btn_coords_1_x_y[2] + btn.height:
                        btn.diff1_btn(list_btn_coords_1_x_y[0], list_btn_coords_1_x_y[2], True)
                        while len(roache_sprite) > 0:
                            del roache_sprite[len(roache_sprite)-1]
                        main(2, 0)

                """-------Проверка, нажата ли кнопка Сложность 2---------------"""
                if list_btn_coords_1_x_y[0] < mouse_x + 10 < list_btn_coords_1_x_y[0] + btn.width:
                    if list_btn_coords_1_x_y[3] < mouse_y + 70 < list_btn_coords_1_x_y[3] + btn.height:
                        btn.diff1_btn(list_btn_coords_1_x_y[0], list_btn_coords_1_x_y[3], True)
                        while len(roache_sprite) > 0:
                            del roache_sprite[len(roache_sprite)-1]
                        main(2, 2)

                """Проверка попали ли курсором, по спрайту.

                Количество координат в LIST_ROACH_COORDS_X берется за основу количества тараканов.
                """
                for roach_nmbr in range(len(list_roach_coords_x)):
                    if list_roach_coords_x[roach_nmbr] < mouse_x + 10 < list_roach_coords_x[roach_nmbr] + 36:
                        if list_roach_coords_y[roach_nmbr] < mouse_y + 70 < list_roach_coords_y[roach_nmbr] + 50:
                            """+10 и +70 берется для сопоставления курсора и положения хлопушки, на спрайте"""
                            list_grave_coords_x.append(list_roach_coords_x[roach_nmbr])
                            list_grave_coords_y.append(list_roach_coords_y[roach_nmbr])
                            del list_roach_coords_x[roach_nmbr]
                            del list_roach_coords_y[roach_nmbr]
                            del roache_sprite[roach_nmbr]
                            del list_roach_sprites[roach_nmbr]
                            QUANTITY_ROACHES -= 1
                            break
        else:
            oggi_hero.draw(sc, OGGI_SPRITE_UP, mouse_x, mouse_y)
        for i6 in range(len(list_grave_coords_x)):
            grave.draw(sc, './Lib/gravestone.png', list_grave_coords_x[i6], list_grave_coords_y[i6])
        pygame.display.update()
        sc.blit(background, (0, 0))  # перерисовываем фон


if __name__ == '__main__':
    game_intro()
