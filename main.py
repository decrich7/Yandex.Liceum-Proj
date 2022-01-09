# -*- coding: utf-8 -*-
import pygame
import os
import sys

from table import Board
from boal import BoalGame
board = Board(7, 6)
running = True
board.coord()
boal = BoalGame(7, 6)
boal.coord()
screen = pygame.display.set_mode((600, 500))
image = pygame.image.load("a.jpg")
image1 = pygame.transform.scale(image, (700, 700))
screen.blit(image1, (0, 0))

board.render(screen)
pygame.display.flip()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            coord = board.on_click(board.get_cell(event.pos))
            # print(board.get_cell(event.pos))
            # print(boal.list)
            if boal.flag:
                boal.drow_ball(screen, coord)
            pygame.display.flip()


