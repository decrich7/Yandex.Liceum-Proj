# -*- coding: utf-8 -*-
import pygame


class Counter:
    def __init__(self):
        self.blue = 0
        self.yellow = 0

    def add_blue(self):
        self.blue += 1

    def add_yellow(self):
        self.yellow += 1

    def render_winner_count(self, screen):
        f1 = pygame.font.Font(None, 35)
        blue = f1.render(f'Синий: {self.blue}', 7, pygame.Color('#1B4DF3'))
        yellow = f1.render(f'Желтый: {self.yellow}', 7, pygame.Color('#EEEE3D'))
        screen.blit(blue, (10, 80))
        screen.blit(yellow, (10, 115))