import pygame

from table import Board


class BoalGame(Board):

    def drow_ball(self, screen, coord):
        coord = list(coord)
        self.count += 1
        y = 435
        for i in self.list_boll:
            if coord[0] == i[0]:
                i[1] = i[1] + 1
                self.list_boll.append(coord)
                if i[1] >= 6:
                    self.flag = False
                else:
                    if self.count % 2 == 0:
                        pygame.draw.circle(screen, pygame.Color('#3669D0'),
                                           (self.list[coord[0]][coord[1]][1] - 5, y - 50 * i[1]), 20)
                        pygame.draw.circle(screen, pygame.Color('#8CB1FC'),
                                           (self.list[coord[0]][coord[1]][1] - 5, y - 50 * i[1]), 23, 3)
                        pygame.display.flip()
                    else:
                        pygame.draw.circle(screen, pygame.Color('#7EF566'),
                                           (self.list[coord[0]][coord[1]][1] - 5, y - 50 * i[1]), 20)
                        pygame.draw.circle(screen, pygame.Color('#2ABC0D'),
                                           (self.list[coord[0]][coord[1]][1] - 5, y - 50 * i[1]), 23, 3)
                        pygame.display.flip()

                    print(self.list_boll)
                    return

        coord[1] = 0
        self.list_boll.append(coord)
        if self.count % 2 == 0:
            pygame.draw.circle(screen, pygame.Color('#3669D0'),
                               (self.list[coord[0]][coord[1]][1] - 5, y), 20)
            pygame.draw.circle(screen, pygame.Color('#8CB1FC'),
                               (self.list[coord[0]][coord[1]][1] - 5, y), 23, 3)
            pygame.display.flip()
        else:
            pygame.draw.circle(screen, pygame.Color('#7EF566'),
                               (self.list[coord[0]][coord[1]][1] - 5, y), 20)
            pygame.draw.circle(screen, pygame.Color('#2ABC0D'),
                               (self.list[coord[0]][coord[1]][1] - 5, y), 23, 3)
            pygame.display.flip()
        print(self.list_boll)

