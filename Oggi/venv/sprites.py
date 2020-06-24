from pygame import *


class Oggi(sprite.Sprite):
    def __init__(self):
        sprite.Sprite.__init__(self)
        self.rect = Rect(0, 0, 36, 36)

    def draw(self, screen:"background", path_img:"path to img sprite", mouse_x:"coords X", mouse_y: "coords Y"):
        self.image = image.load(path_img).convert_alpha()
        screen.blit(self.image, (mouse_x, mouse_y))
