# -*- coding: utf-8 -*-
import pygame
from WINNER import get_win
from table import Board
from boal import BoalGame

pygame.init()
screen = pygame.display.set_mode((600, 500))
running = True

pygame.mixer.music.load('sound/sound.mp3')
pygame.mixer.music.set_volume(0.4)
pygame.mixer.music.play(-1)

replay = pygame.image.load("picture/replay2.png")
replay_pc = pygame.transform.scale(replay, (70, 70)).convert_alpha()

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
# board.render(screen)
# boal.drow_static(screen)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if 260 < event.pos[0] < 335 and 75 < event.pos[1] < 145 and get_win(boal.list_move) == 'Blue':
                boal.clean_data()
                boal.coord()
                screen.blit(image1, (0, 0))
                boal.render(screen)
                pygame.display.flip()
                continue
            elif 260 < event.pos[0] < 335 and 75 < event.pos[1] < 145 and get_win(boal.list_move) == 'Yellow':
                boal.clean_data()
                boal.coord()
                screen.blit(image1, (0, 0))
                boal.render(screen)
                pygame.display.flip()
                continue

                # pygame.display.update()
            if fon is False:
                screen.blit(image1, (0, 0))
                pygame.display.flip()
                coord = board.on_click(board.get_cell(event.pos))
                # print(boal.flag)
                if boal.flag:
                    if coord != (None, None):
                        boal.drow_ball(screen, coord)
                        # print(get_win(boal.list_move))
                        pygame.mixer.music.pause()
                        sound_drop = pygame.mixer.Sound('sound/drop_boal.mp3')
                        sound_drop.play()
                        pygame.mixer.music.unpause()
                        boal.drow_static(screen)
                        if get_win(boal.list_move) == 'Blue':
                            font = pygame.font.Font(None, 55)
                            winner_b = font.render('Синий выйграл!', 200, pygame.Color('#1B4DF3'))
                            screen.blit(replay_pc, (265, 75))
                            screen.blit(winner_b, (150, 30))
                            pygame.mixer.music.pause()
                            sound_win_b = pygame.mixer.Sound('sound/победа.mp3')
                            sound_win_b.play()
                            pygame.mixer.music.unpause()

                            # boal.clean_data()
                            # boal.coord()

                            # board.render(screen)
                            pygame.display.flip()
                        elif get_win(boal.list_move) == 'Yellow':
                            boal.flag = False
                            font = pygame.font.Font(None, 55)
                            winner_y = font.render('Желтый выйграл!', 200, pygame.Color('#EEEE3D'))
                            screen.blit(winner_y, (150, 30))
                            screen.blit(replay_pc, (265, 75))

                            pygame.mixer.music.pause()
                            sound_win = pygame.mixer.Sound('sound/победа.mp3')
                            pygame.mixer.music.unpause()
                            sound_win.play()

                            pygame.display.flip()
                else:
                    board.render(screen)
                    boal.drow_static(screen)
                    pygame.display.flip()
            else:
                if 240 < event.pos[0] < 375 and \
                        150 < event.pos[1] < 200:
                    screen.blit(image1, (0, 0))
                    boal.render(screen)
                    pygame.display.flip()

                    fon = False
# pyinstaller --noconfirm --onefile --windowed --name "4 in row" --add-data "C:/Users/PAJILOY PAVUK/PycharmProjects/Game/picture/back_pic.jpg;." --add-data "C:/Users/PAJILOY PAVUK/PycharmProjects/Game/picture/play_button.png;." --add-data "C:/Users/PAJILOY PAVUK/PycharmProjects/Game/picture/replay2.png;." --add-data "C:/Users/PAJILOY PAVUK/PycharmProjects/Game/picture/start.jpg;." --add-data "C:/Users/PAJILOY PAVUK/PycharmProjects/Game/sound/drop_boal.mp3;." --add-data "C:/Users/PAJILOY PAVUK/PycharmProjects/Game/sound/sound.mp3;." --add-data "C:/Users/PAJILOY PAVUK/PycharmProjects/Game/sound/победа.mp3;."  "C:/Users/PAJILOY PAVUK/PycharmProjects/Game/main.py" "C:/Users/PAJILOY PAVUK/PycharmProjects/Game/WINNER.py" "C:/Users/PAJILOY PAVUK/PycharmProjects/Game/table.py" "C:/Users/PAJILOY PAVUK/PycharmProjects/Game/boal.py"
# 'pyinstaller --onefile --add-data "picture\start.jpg;picture\replay2.png;picture\play_button.png;picture\back_pic.jpg" main.py boal.py table.py WINNER.py'