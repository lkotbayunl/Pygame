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
    """Основная функция инициализирует окно, подгружает png, для спрайтов. Инициализируется класс Oggi,
        который отвечает за отрисовку спрайта курсора. В основном цикле реализован механизм
        отслеживания позиции курсора, а также нажатия кнопки мыши. """
    HEIGHT = 800
    WIDTH = 1200
    OGGI_SPRITE_UP = './Lib/Oggi_up.png'
    OGGI_SPRITE_DOWN = './Lib/Oggi_down.png'
    QUANTITY_ROACHES = 10
    LIST_ROACH_COORDS_X = list(range(QUANTITY_ROACHES))
    LIST_ROACH_COORDS_Y = list(range(QUANTITY_ROACHES))
    LIST_ROACH_SPRITES = []
    LIST_GRAVE_COORDS_X = []
    LIST_GRAVE_COORDS_Y = []
    LIST_BTN_COORDS_1X_Y = [970, 150, 255, 360]  # первый элемент списка Х, остальные Y
    timer = pygame.time.Clock()
    # ------------------------------------------------------------------------------------ #
    os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (500, 200)
    sc = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Oggi and cockroaches")
    background = pygame.image.load('./Lib/background.jpg').convert_alpha()
    background_rect = background.get_rect(topleft=(0, 0))
    sc.blit(background, background_rect)
    oggi_hero = Oggi()
    roache_sprite = [Cockroach(randint(70, 890), randint(70, 650), speed, difficulty) for i in range(QUANTITY_ROACHES)]
    """Создается список roache_sprite, в котором содержится количество классов Cockroach, равное QUANTITY_ROACHES"""
    grave = Gravestone()
    btn = Button(sc, 200, 50)  # передает ширину и высоту кнопок
    timer = pygame.time.Clock()
    for i2 in range(QUANTITY_ROACHES):
        LIST_ROACH_SPRITES.append(randint(1, 3))

    while 1:

        timer.tick(60)  # FPS
        pygame.mouse.set_visible(False)

        for i_mouse_btn in pygame.event.get():
            mouse_x = pygame.mouse.get_pos()[0]
            mouse_y = pygame.mouse.get_pos()[1]
            if i_mouse_btn.type == pygame.QUIT:
                exit()
        # ----- вызов методов "кнопок", класса Button, при вызове передаются координаты X, Y -------
        btn.new_game_btn(LIST_BTN_COORDS_1X_Y[0], LIST_BTN_COORDS_1X_Y[1], False)
        btn.diff1_btn(LIST_BTN_COORDS_1X_Y[0], LIST_BTN_COORDS_1X_Y[2], False)
        btn.diff2_btn(LIST_BTN_COORDS_1X_Y[0], LIST_BTN_COORDS_1X_Y[3], False)
        # ---------------------------------------------------

        # ---------Генерация тараканов, в случайных местах-----------
        for i3 in range(QUANTITY_ROACHES):
            roach = roache_sprite[i3]
            x, y = roach.tick(sc, LIST_ROACH_SPRITES[i3])
            LIST_ROACH_COORDS_X[i3] = x
            LIST_ROACH_COORDS_Y[i3] = y
        # -----------------------------------------------------------

        if i_mouse_btn.type == pygame.MOUSEBUTTONDOWN:
            if i_mouse_btn.button == 1:
                # -----проверка, нажата ли кнопка New Game ---------------------------------------------
                oggi_hero.draw(sc, OGGI_SPRITE_DOWN, mouse_x, mouse_y)  # передает классу player.Oggi "background",
                                                                        # "path to img sprite", coords X, Y"
                #pygame.display.update()
                if LIST_BTN_COORDS_1X_Y[0] < mouse_x + 10 < LIST_BTN_COORDS_1X_Y[0] + btn.width:
                    if LIST_BTN_COORDS_1X_Y[1] < mouse_y + 70 < LIST_BTN_COORDS_1X_Y[1] + btn.height:
                        """ Список LIST_BTN_COORDS_1X_Y в 0 элементе содержит координату по Х, она одинакова, для всех
                            кнопок остальные элементы списка - координаты по Y, для остальных кнопок идут в порядке: 
                            Новая игра, Сложность 1, Сложность 2"""
                        btn.new_game_btn(LIST_BTN_COORDS_1X_Y[0], LIST_BTN_COORDS_1X_Y[1], True)
                        pygame.display.update()
                        while len(LIST_ROACH_COORDS_X) > 0:
                            del LIST_ROACH_COORDS_X[len(LIST_ROACH_COORDS_X) - 1]
                            del LIST_ROACH_COORDS_Y[len(LIST_ROACH_COORDS_X) - 1]
                            #del ROACH_SPRITES[len(LIST_ROACH_COORDS_X) - 1]

                        main(0, 0)
                # -------проверка, нажата ли кнопка Сложность 1---------------------------
                if LIST_BTN_COORDS_1X_Y[0] < mouse_x + 10 < LIST_BTN_COORDS_1X_Y[0] + btn.width:
                    if LIST_BTN_COORDS_1X_Y[2] < mouse_y + 70 < LIST_BTN_COORDS_1X_Y[2] + btn.height:
                        btn.diff1_btn(LIST_BTN_COORDS_1X_Y[0], LIST_BTN_COORDS_1X_Y[2], True)
                        while len(roache_sprite) > 0:
                            del roache_sprite[len(roache_sprite)-1]
                        main(2, 0)
                # -------проверка, нажата ли кнопка Сложность 2---------------------------
                if LIST_BTN_COORDS_1X_Y[0] < mouse_x + 10 < LIST_BTN_COORDS_1X_Y[0] + btn.width:
                    if LIST_BTN_COORDS_1X_Y[3] < mouse_y + 70 < LIST_BTN_COORDS_1X_Y[3] + btn.height:
                        btn.diff1_btn(LIST_BTN_COORDS_1X_Y[0], LIST_BTN_COORDS_1X_Y[3], True)
                        while len(roache_sprite) > 0:
                            del roache_sprite[len(roache_sprite)-1]
                        main(2, 2)

                for i_shooted in range(len(LIST_ROACH_COORDS_X)):
                    """Проверка попали ли курсором, по спрайту.
                       Количество координат в LIST_ROACH_COORDS_X берется за основу количества тараканов"""
                    if LIST_ROACH_COORDS_X[i_shooted] < mouse_x + 10 < LIST_ROACH_COORDS_X[i_shooted] + 36:
                        if LIST_ROACH_COORDS_Y[i_shooted] < mouse_y + 70 < LIST_ROACH_COORDS_Y[i_shooted] + 50:
                            """+10 и +70 берется для сопоставления курсора и положения хлопушки, на спрайте"""
                            LIST_GRAVE_COORDS_X.append(LIST_ROACH_COORDS_X[i_shooted])
                            LIST_GRAVE_COORDS_Y.append(LIST_ROACH_COORDS_Y[i_shooted])
                            del LIST_ROACH_COORDS_X[i_shooted]
                            del LIST_ROACH_COORDS_Y[i_shooted]
                            del roache_sprite[i_shooted]
                            del LIST_ROACH_SPRITES[i_shooted]
                            QUANTITY_ROACHES -= 1
                            break

        else:
            oggi_hero.draw(sc, OGGI_SPRITE_UP, mouse_x, mouse_y)
        for i6 in range(len(LIST_GRAVE_COORDS_X)):
            grave.draw(sc, './Lib/gravestone.png', LIST_GRAVE_COORDS_X[i6], LIST_GRAVE_COORDS_Y[i6])
        pygame.display.update()
        sc.blit(background, (0, 0))  # перерисовываем фон


if __name__ == '__main__':
    game_intro()
