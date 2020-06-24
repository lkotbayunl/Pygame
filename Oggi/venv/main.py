import pygame
from sprites import *


def main():
    """Основная функция инициализирует окно, подгружает png, для спрайтов. Инициализируется класс Oggi,
    который отвечает за отрисовку спрайта курсора. В основном цикле реализован механизм
    отслеживания позиции курсора, а также нажатия кнопки мыши. """
    left_btn = False
    Oggi_sprite_up = './Lib/Oggi_up.png'
    Oggi_sprite_down = './Lib/Oggi_down.png'
    pygame.init()
    sc = pygame.display.set_mode((1000, 800))
    pygame.display.set_caption("Oggi and cockroaches")
    background = pygame.image.load('./Lib/background.jpg').convert_alpha()
    background_rect = background.get_rect(topleft=(0, 0))
    sc.blit(background, background_rect)
    oggi_hero = Oggi()

    timer = pygame.time.Clock()

    while 1:
        timer.tick(60)  # FPS
        pygame.mouse.set_visible(False)
        for i in pygame.event.get():
            mouse_x = pygame.mouse.get_pos()[0]
            mouse_y = pygame.mouse.get_pos()[1]
        if i.type == pygame.QUIT:
            exit()
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                oggi_hero.draw(sc, Oggi_sprite_down, mouse_x,
                               mouse_y)  # передает классу player.Oggi "background", "path to img sprite", coords X, Y"
                pygame.display.update()
        else:
            oggi_hero.draw(sc, Oggi_sprite_up, mouse_x, mouse_y)
        pygame.display.update()
        sc.blit(background, (0, 0))  # перерисовываем фон


if __name__ == '__main__':
    main()
