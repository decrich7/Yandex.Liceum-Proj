# -*- coding: utf-8 -*-
import pygame
import os
import sys
from WINNER import get_win
from table import Board
from boal import BoalGame
pygame.init()
screen = pygame.display.set_mode((600, 500))
running = True
pygame.mixer.music.load('sound/sound.mp3')
pygame.mixer.music.set_volume(0.4)
pygame.mixer.music.play(-1)
image_fon_load = pygame.image.load("picture/start.jpg")
image_fon = pygame.transform.scale(image_fon_load, (700, 700))
play_load = pygame.image.load("picture/play_button.png")
play_load.set_colorkey('WHITE')
play_fon = pygame.transform.scale(play_load, (50, 50)).convert_alpha()
screen.blit(image_fon, (0, 0))
screen.blit(play_fon, (325, 145))
f1 = pygame.font.Font(None, 55)
play = f1.render('Play', 80, pygame.Color('#F23454'))
screen.blit(play, (240, 150))
pygame.display.flip()
image = pygame.image.load("picture/back_pic.jpg")
image1 = pygame.transform.scale(image, (700, 700))
board = Board(7, 6, image1)
board.coord()
boal = BoalGame(7, 6, image1)
boal.coord()
fon = True
board.render(screen)
boal.drow_static(screen)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if fon is False:
                screen.blit(image1, (0, 0))
                pygame.display.flip()
                coord = board.on_click(board.get_cell(event.pos))
                if boal.flag:
                    boal.drow_ball(screen, coord)
                    print(get_win(boal.list_move))
                    pygame.mixer.music.pause()
                    sound_drop = pygame.mixer.Sound('sound/drop_boal.mp3')
                    sound_drop.play()
                    pygame.mixer.music.unpause()
                    boal.drow_static(screen)
                pygame.display.flip()
            else:
                if event.pos[0] > 240 and event.pos[0] < 375 and event.pos[1] > 150 and event.pos[1] < 200:
                    screen.blit(image1, (0, 0))
                    boal.render(screen)
                    pygame.display.flip()

                    fon = False

