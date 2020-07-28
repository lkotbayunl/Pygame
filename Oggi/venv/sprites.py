from pygame import *
from random import randint
from math import *
import time

"""Много простых классов, порой ненужных, либо избыточных. Пытаюсь понять механизм работы классов и наследования =)"""


class Oggi(sprite.Sprite):
    def __init__(self):
        sprite.Sprite.__init__(self)
        self.rect = Rect(0, 0, 64, 64)

    def draw(self, screen: "background", path_img: "path to img sprite", mouse_x: "coords X", mouse_y: "coords Y"):
        self.image = image.load(path_img).convert_alpha()
        screen.blit(self.image, (mouse_x, mouse_y))


class Cockroach(sprite.Sprite):

    def __init__(self, random_x, random_y, speed, difficulty):
        sprite.Sprite.__init__(self)
        self.difficulty = difficulty
        self.image = 0
        self.coords_x, self.coords_y = random_x, random_y
        self.dx, self.dy = (speed, speed)

    def move(self):
        self.coords_x += self.dx
        self.coords_y += self.dy
        if self.coords_y >= 720 or self.coords_y <= 30:
            self.dy *= -1

        if self.coords_x >= 870 or self.coords_x <= 30:
            self.dx *= -1
        # ---------------Почти хаотичное движение тараканов, на сложности 2 -------------------
        if self.difficulty == 2:
            if 200 > self.coords_y > 180:
                if 600 > self.coords_x >100:
                    self.coords_x = self.coords_x + randint(1, 5)
            if 200 > self.coords_y > 180:
                if 600 > self.coords_x >100:
                    self.dx *= -1
            if 700 > self.coords_y > 680:
                if 600 > self.coords_x >100:
                    self.dx *= -1
            if 700 > self.coords_y > 680:
                if 600 > self.coords_x >100:
                    self.coords_x = self.coords_x + randint(1, 5)
            if 300 > self.coords_x > 280:
                if 600 > self.coords_y >100:
                    self.dx *= -1
            if 300 > self.coords_x > 290:
                if 600 > self.coords_y >100:
                    self.coords_y = self.coords_y + randint(1, 5)
                    self.coords_y = self.coords_y + randint(1, 5)
            if 400 > self.coords_x > 380:
                if 600 > self.coords_y >100:
                    self.dy *= -1
            if 400 > self.coords_x > 390:
                if 600 > self.coords_y >100:
                    self.coords_y = self.coords_y + randint(1, 5)
            if 500 > self.coords_x > 480:
                if 600 > self.coords_y >100:
                    self.dy *= -1
            if 700 > self.coords_x > 690:
                if 600 > self.coords_y >100:
                    self.coords_y = self.coords_y + randint(1, 5)
        # -----------------------------------------------------------------------

    def draw(self, screen: "background", roach_sprites):
        self.image = image.load('./Lib/roach' + str(roach_sprites) + '.png').convert_alpha()
        screen.blit(self.image, (self.coords_x, self.coords_y))
        return self.coords_x, self.coords_y

    def tick(self, sc, nmbr_sprite):
        self.move()
        x, y = self.draw(sc, nmbr_sprite)
        return x, y


class Gravestone(sprite.Sprite):
    def __init__(self):
        sprite.Sprite.__init__(self)
        self.rect = Rect(0, 0, 40, 40)

    def draw(self, screen: "background", path_img: "path to img sprite", coords_x, coords_y):
        self.image = image.load(path_img).convert_alpha()
        screen.blit(self.image, (coords_x, coords_y))
