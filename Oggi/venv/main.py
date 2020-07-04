import pygame
import random
import os
from sprites import *
import time

pygame.init()

HEIGHT = 800
WIDTH = 1000
QUANTITY_ROACHES = random.randint(5, 10)
OGGI_SPRITE_UP = './Lib/Oggi_up.png'
OGGI_SPRITE_DOWN = './Lib/Oggi_down.png'
LIST_SPRITES_NMBR = []
LIST_ROACH_COORDS_X = []
LIST_ROACH_COORDS_Y = []
LIST_GRAVE_COORDS_X = []
LIST_GRAVE_COORDS_Y = []
ROACH_SPRITES = []
timer = pygame.time.Clock()


def game_intro():
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                pygame.QUIT
                quit()
                main()
        pygame.font.init()
        os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (750, 300)
        screen = pygame.display.set_mode((480, 400), pygame.NOFRAME)
        splash = pygame.image.load('./Lib/splash.png').convert_alpha()
        screen.blit(splash, (0, 0))

        pygame.display.update()


def main():
    """Основная функция инициализирует окно, подгружает png, для спрайтов. Инициализируется класс Oggi,
    который отвечает за отрисовку спрайта курсора. В основном цикле реализован механизм
    отслеживания позиции курсора, а также нажатия кнопки мыши. """
    NEW_GAME = True
    os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (500, 200)
    sc = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Oggi and cockroaches")
    background = pygame.image.load('./Lib/background.jpg').convert_alpha()
    background_rect = background.get_rect(topleft=(0, 0))
    sc.blit(background, background_rect)
    oggi_hero = Oggi()
    roache_sprite = Cockroach()
    grave = Gravestone()
    timer = pygame.time.Clock()
    for i2 in range(QUANTITY_ROACHES):
        ROACH_SPRITES.append(random.randint(1, 3))
        LIST_ROACH_COORDS_X.append(random.randint(36, 950))
        LIST_ROACH_COORDS_Y.append(random.randint(36, 750))

    while 1:

        timer.tick(60)  # FPS
        pygame.mouse.set_visible(False)
        for i3 in range(len(LIST_ROACH_COORDS_X)):
            roache_sprite.draw(sc, './Lib/roach' + str(ROACH_SPRITES[i3]) + '.png', LIST_ROACH_COORDS_X[i3],
                               LIST_ROACH_COORDS_Y[i3])  # roache_sprite.draw(background_layout, # path_to_image,
                                                         # coords_x, coords_y)
        for i4 in pygame.event.get():
            mouse_x = pygame.mouse.get_pos()[0]
            mouse_y = pygame.mouse.get_pos()[1]
        if i4.type == pygame.QUIT:
            exit()
        if i4.type == pygame.MOUSEBUTTONDOWN:
            if i4.button == 1:
                for i5 in range(len(LIST_ROACH_COORDS_X)):
                    """Проверка попали ли курсором, по спрайту.
                       Количество координат в LIST_ROACH_COORDS_X берется за основу количества тараканов"""
                    if LIST_ROACH_COORDS_X[i5] < mouse_x + 10 < LIST_ROACH_COORDS_X[i5] + 36:
                        if LIST_ROACH_COORDS_Y[i5] < mouse_y + 70 < LIST_ROACH_COORDS_Y[i5] + 50:
                            """+10 и +70 берется для сопоставления курсора и положения хлопушки, на спрайте"""
                            print('Spoted')
                            LIST_GRAVE_COORDS_X.append(LIST_ROACH_COORDS_X[i5])
                            LIST_GRAVE_COORDS_Y.append(LIST_ROACH_COORDS_Y[i5])
                            del LIST_ROACH_COORDS_X[i5]
                            del LIST_ROACH_COORDS_Y[i5]
                            del ROACH_SPRITES[i5]
                            break
                oggi_hero.draw(sc, OGGI_SPRITE_DOWN, mouse_x, mouse_y)  # передает классу player.Oggi "background",
                # "path to img sprite", coords X, Y"
                pygame.display.update()
        else:
            oggi_hero.draw(sc, OGGI_SPRITE_UP, mouse_x, mouse_y)
        for i6 in range(len(LIST_GRAVE_COORDS_X)):
            grave.draw(sc, './Lib/gravestone.png', LIST_GRAVE_COORDS_X[i6], LIST_GRAVE_COORDS_Y[i6])
        pygame.display.update()
        sc.blit(background, (0, 0))  # перерисовываем фон


if __name__ == '__main__':
    game_intro()
