import pygame


class Button:
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)

    def __init__(self, background, width, height):
        self.background = background
        self.width = width
        self.height = height

    def new_game_btn(self, left, top, pressed):

        pygame.init()
        if pressed:
            pygame.draw.rect(self.background, self.WHITE, (left, top, self.width, self.height))
        else:
            pygame.draw.rect(self.background, self.BLACK, (left, top, self.width, self.height))
        pygame.draw.rect(self.background, self.WHITE, (left + 2, top + 2, self.width - 3, self.height - 3))
        font = pygame.font.SysFont("arialms", 20)
        text2 = font.render("Новая игра", 0, (0, 0, 0))
        self.background.blit(text2, ((left + self.width / 2 - 50), (top + self.height / 2 - 15)))

    def diff1_btn(self, left, top, pressed):
        pygame.init()
        if pressed:
            pygame.draw.rect(self.background, self.WHITE, (left, top, self.width, self.height))
        else:
            pygame.draw.rect(self.background, self.BLACK, (left, top, self.width, self.height))
        pygame.draw.rect(self.background, self.WHITE, (left + 2, top + 2, self.width - 3, self.height - 3))
        font = pygame.font.SysFont("arialms", 20)
        text2 = font.render("Сложность 1", 0, (0, 0, 0))
        self.background.blit(text2, ((left + self.width / 2 - 50), (top + self.height / 2 - 15)))

    def diff2_btn(self, left, top, pressed):
        pygame.init()
        if pressed:
            pygame.draw.rect(self.background, self.WHITE, (left, top, self.width, self.height))
        else:
            pygame.draw.rect(self.background, self.BLACK, (left, top, self.width, self.height))
        pygame.draw.rect(self.background, self.WHITE, (left + 2, top + 2, self.width - 3, self.height - 3))
        font = pygame.font.SysFont("arialms", 20)
        text2 = font.render("Сложность 2", 0, (0, 0, 0))
        self.background.blit(text2, ((left + self.width / 2 - 50), (top + self.height / 2 - 15)))
