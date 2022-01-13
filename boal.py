import pygame

from table import Board


class BoalGame(Board):

    def drow_ball(self, screen, coord):
        count = 0
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
                    pygame.draw.circle(screen, pygame.Color('#EEF351'),
                                       (self.list[coord[0]][coord[1]][1] - 5, y - 50 * (i[1])), 20)
                    pygame.draw.circle(screen, pygame.Color('#FFA200'),
                                       (self.list[coord[0]][coord[1]][1] - 5, y - 50 * (i[1])), 23, 3)
                    pygame.display.flip()
                else:
                    pygame.draw.circle(screen, pygame.Color('#5349DE'),
                                       (self.list[coord[0]][coord[1]][1] - 5, y - 50 * i[1]), 20)
                    pygame.draw.circle(screen, pygame.Color('#261BC0'),
                                       (self.list[coord[0]][coord[1]][1] - 5, y - 50 * i[1]), 23, 3)
                    pygame.display.flip()
                return

        coord[1] = 0
        self.list_boll.append(coord)
        self.list_move.append(tuple(coord))
        if self.count % 2 == 0:
            pygame.draw.circle(screen, pygame.Color('#EEF351'),
                               (self.list[coord[0]][coord[1]][1] - 5, y), 20)
            pygame.draw.circle(screen, pygame.Color('#FFA200'),
                               (self.list[coord[0]][coord[1]][1] - 5, y), 23, 3)
            pygame.display.flip()
        else:
            pygame.draw.circle(screen, pygame.Color('#5349DE'),
                               (self.list[coord[0]][coord[1]][1] - 5, y), 20)
            pygame.draw.circle(screen, pygame.Color('#261BC0'),
                               (self.list[coord[0]][coord[1]][1] - 5, y), 23, 3)
            pygame.display.flip()
        # print(self.list_move)
