import pygame


class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * width for i in range(height)]
        self.left = 130
        self.top = 160
        self.cell_size = 50
        self.list = []
        self.count = 0
        self.list_xod = []
        self.list_boll = list()
        self.flag = True

    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self, screen):
        pygame.draw.rect(screen, pygame.Color('#EB6C63'), (
            self.left, self.top, 350,
            300))
        for y in range(self.height):
            for x in range(self.width):
                pygame.draw.rect(screen, pygame.Color('#DB3954'), (
                    x * self.cell_size + self.left, y * self.cell_size + self.top, self.cell_size,
                    self.cell_size), 1)
                pygame.draw.circle(screen, pygame.Color('#DB3954'),
                                   (x * self.cell_size + self.left + 25, y * self.cell_size + self.top + 25),
                                   22,
                                   4)
                # pygame.draw.circle(screen, pygame.Color('#DB3954'),
                #                    (x * self.cell_size + self.left + 25, y * self.cell_size + self.top + 25),
                #                    23,
                #                    3)

    def coord(self):
        for y in range(self.height + 1):
            a = []
            for x in range(self.width):
                a.append((x * self.cell_size + self.left, y * self.cell_size + self.top))
            self.list.append(a)

    def get_cell(self, mouse_pos):
        if mouse_pos[0] >= self.left and mouse_pos[0] <= 480 and mouse_pos[1] >= self.top and mouse_pos[1] <= 460:
            return mouse_pos
        else:
            return None

    def on_click(self, cell_coords):
        if cell_coords is not None:
            for i in range(len(self.list)):
                for j in range(len(self.list[i])):
                    if cell_coords[0] > self.list[i][j][0] and cell_coords[0] <= (
                            self.list[i][j][0] + self.cell_size) and \
                            cell_coords[1] > self.list[i][j][1] and cell_coords[1] <= (
                            self.list[i][j][1] + self.cell_size):
                        return j, i
        else:
            return None, None

