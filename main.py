# -*- coding: utf-8 -*-
import pygame
import os
import sys
from WINNER import get_win
from table import Board
from boal import BoalGame
screen = pygame.display.set_mode((600, 500))
image = pygame.image.load("a.jpg")
image1 = pygame.transform.scale(image, (700, 700))
screen.blit(image1, (0, 0))
board = Board(7, 6, image1)
running = True
board.coord()

boal = BoalGame(7, 6, image1)
boal.coord()


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
                print(boal.list_move)
                boal.drow_ball(screen, coord)
                get_win(boal.list_move)
            pygame.display.flip()


