import pygame

from table import Board


class BoalGame(Board):

    def drow_ball(self, screen, coord):
        coord = list(coord)
        self.count += 1
        y = 435
        for i in self.list_boll:
            if coord[0] == i[0]:
                if i[1] >= 5:
                    return

                a = (i[0], i[1] + 1)
                self.list_move.append(a)
                i[1] = i[1] + 1

                if self.count % 2 == 0:
                    self.circle_drow(y=y, color='Blue', screen=screen, coord=coord, i=i)
                else:
                    self.circle_drow(y=y, color='Yellow', screen=screen, coord=coord, i=i)
                return

        coord[1] = 0
        self.list_boll.append(coord)
        self.list_move.append(tuple(coord))
        if self.count % 2 == 0:
            self.circle_drow(y=y, color='Yellow', screen=screen, coord=coord, i=None)
        else:
            self.circle_drow(y=y, color='Blue', screen=screen, coord=coord, i=None)

    def drow_static(self, screen):
        count = 0
        for i in self.list_move[0:-1]:
            count += 1
            if count % 2 == 0:
                pygame.draw.circle(screen, pygame.Color('#EEF351'),
                                   (self.list[i[0]][i[1]][1] - 5, 435 - 50 * (i[1])), 20)
                pygame.draw.circle(screen, pygame.Color('#FFA200'),
                                   (self.list[i[0]][i[1]][1] - 5, 435 - 50 * (i[1])), 23, 3)
            else:
                pygame.draw.circle(screen, pygame.Color('#5349DE'),
                                   (self.list[i[0]][i[1]][1] - 5, 435 - 50 * (i[1])), 20)
                pygame.draw.circle(screen, pygame.Color('#261BC0'),
                                   (self.list[i[0]][i[1]][1] - 5, 435 - 50 * (i[1])), 23, 3)

    def circle_drow(self, y, color, screen, coord, i):
        if color == 'Blue':
            if i is not None:
                y_pos = 120
                v = 150
                clock = pygame.time.Clock()
                while True:
                    screen.blit(self.image, (0, 0))
                    self.render(screen)
                    self.drow_static(screen)
                    pygame.draw.circle(screen, pygame.Color('#EEF351'),
                                       (self.list[coord[0]][coord[1]][1] - 5, y_pos), 20)
                    pygame.draw.circle(screen, pygame.Color('#FFA200'),
                                       (self.list[coord[0]][coord[1]][1] - 5, y_pos), 23, 3)
                    y_pos += v * clock.tick() / 1000
                    v *= 1.005
                    pygame.display.flip()
                    if y_pos >= y - 50 * (i[1]):
                        break
            else:
                y_pos = 120
                v = 150
                clock = pygame.time.Clock()
                while True:
                    screen.blit(self.image, (0, 0))
                    self.render(screen)
                    self.drow_static(screen)
                    pygame.draw.circle(screen, pygame.Color('#5349DE'),
                                       (self.list[coord[0]][coord[1]][1] - 5, y_pos), 20)
                    pygame.draw.circle(screen, pygame.Color('#261BC0'),
                                       (self.list[coord[0]][coord[1]][1] - 5, y_pos), 23, 3)
                    y_pos += v * clock.tick() / 1000
                    v *= 1.005
                    pygame.display.flip()
                    if y_pos >= y:
                        break
        else:
            if i is not None:
                y_pos = 120
                v = 150
                clock = pygame.time.Clock()
                while True:
                    screen.blit(self.image, (0, 0))
                    self.render(screen)
                    self.drow_static(screen)
                    pygame.draw.circle(screen, pygame.Color('#5349DE'),
                                       (self.list[coord[0]][coord[1]][1] - 5, y_pos), 20)
                    pygame.draw.circle(screen, pygame.Color('#261BC0'),
                                       (self.list[coord[0]][coord[1]][1] - 5, y_pos), 23, 3)
                    y_pos += v * clock.tick() / 1000
                    v *= 1.005

                    pygame.display.flip()
                    if y_pos >= y - 50 * (i[1]):
                        break
            else:
                y_pos = 120
                v = 150
                clock = pygame.time.Clock()
                while True:
                    screen.blit(self.image, (0, 0))
                    self.render(screen)
                    self.drow_static(screen)
                    pygame.draw.circle(screen, pygame.Color('#EEF351'),
                                       (self.list[coord[0]][coord[1]][1] - 5, y_pos), 20)
                    pygame.draw.circle(screen, pygame.Color('#FFA200'),
                                       (self.list[coord[0]][coord[1]][1] - 5, y_pos), 23, 3)
                    y_pos += v * clock.tick() / 1000
                    v *= 1.005

                    pygame.display.flip()
                    if y_pos >= y:
                        break
