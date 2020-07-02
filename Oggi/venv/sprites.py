from pygame import *
"""Много простых классов, порой ненужных, либо избыточных. Пытаюсь понять механизм работы классов и наследования =)"""

class Oggi(sprite.Sprite):
    def __init__(self):
        sprite.Sprite.__init__(self)
        self.rect = Rect(0, 0, 64, 64)

    def draw(self, screen: "background", path_img: "path to img sprite", mouse_x: "coords X", mouse_y: "coords Y"):
        self.image = image.load(path_img).convert_alpha()
        screen.blit(self.image, (mouse_x, mouse_y))


class Cockroach(sprite.Sprite):
    def __init__(self):
        sprite.Sprite.__init__(self)
        self.rect = Rect(0, 0, 36, 36)

    def draw(self, screen: "background", path_img: "path to img sprite", coords_x, coords_y):
        self.image = image.load(path_img).convert_alpha()
        screen.blit(self.image, (coords_x, coords_y))

class Gravestone(sprite.Sprite):
    def __init__(self):
        sprite.Sprite.__init__(self)
        self.rect = Rect(0, 0, 40, 40)

    def draw(self, screen: "background", path_img: "path to img sprite", coords_x, coords_y):
        self.image = image.load(path_img).convert_alpha()
        screen.blit(self.image, (coords_x, coords_y))
