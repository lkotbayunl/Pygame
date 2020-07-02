import pygame
import random
from sprites import *

HEIGHT = 800
WIDTH = 1000
QUANTITY_ROACHES = random.randint(5, 10)
OGGI_SPRITE_UP = './Lib/1.jpg'
OGGI_SPRITE_DOWN = './Lib/Oggi_down.png'
LIST_ROACH_COORDS_X = []
LIST_ROACH_COORDS_Y = []
LIST_GRAVE_COORDS_X = []
LIST_GRAVE_COORDS_Y = []
ROACH_SPRITES = []


def main():
    """Основная функция инициализирует окно, подгружает png, для спрайтов. Инициализируется класс Oggi,
    который отвечает за отрисовку спрайта курсора. В основном цикле реализован механизм
    отслеживания позиции курсора, а также нажатия кнопки мыши. """
    NEW_GAME = True
    pygame.init()
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
                               LIST_ROACH_COORDS_Y[i3])  # roache_sprite.draw(background_layout,
            # path_to_image, coords_x, coords_y)
        for i4 in pygame.event.get():
            mouse_x = pygame.mouse.get_pos()[0]
            mouse_y = pygame.mouse.get_pos()[1]
        if i4.type == pygame.QUIT:
            exit()
        if i4.type == pygame.MOUSEBUTTONDOWN:
            if i4.button == 1:
                for i5 in range(len(LIST_ROACH_COORDS_X)):
                    if LIST_ROACH_COORDS_X[i5] < mouse_x < LIST_ROACH_COORDS_X[i5] + 36:
                        if LIST_ROACH_COORDS_Y[i5] < mouse_y < LIST_ROACH_COORDS_Y[i5] + 50:
                            print('Spoted')
                            LIST_GRAVE_COORDS_X.append(LIST_ROACH_COORDS_X[i5])
                            LIST_GRAVE_COORDS_Y.append(LIST_ROACH_COORDS_Y[i5])
                            del LIST_ROACH_COORDS_X[i5]
                            del LIST_ROACH_COORDS_Y[i5]
                            break
                oggi_hero.draw(sc, OGGI_SPRITE_DOWN, mouse_x,
                               mouse_y)  # передает классу player.Oggi "background", "path to img sprite", coords X, Y"
                pygame.display.update()
        else:
            oggi_hero.draw(sc, OGGI_SPRITE_UP, mouse_x, mouse_y)
        for i6 in range(len(LIST_GRAVE_COORDS_X)):
            grave.draw(sc, './Lib/gravestone.png', LIST_GRAVE_COORDS_X[i6], LIST_GRAVE_COORDS_Y[i6])
        pygame.display.update()
        sc.blit(background, (0, 0))  # перерисовываем фон


if __name__ == '__main__':
    main()
