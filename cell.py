import pygame
from random import choice

class Cell:
    def __init__(self, x, y, width):
        self.x = x
        self.y = y
        self.width = width
        self.walls = {'top': True, 'left': True, 'bottom': True, 'right': True}
        self.visited = False

    def draw(self, screen, size):
        x = self.x * size
        y = self.y * size
        if self.walls['top']:
            pygame.draw.line(screen, pygame.Color('darkgreen'), (x, y), (x + size, y), self.width)
        elif self.walls['left']:
            pygame.draw.line(screen, pygame.Color('darkgreen'), (x, y + size), (x, y), self.width)
        elif self.walls['bottom']:
            pygame.draw.line(screen, pygame.Color('darkgreen'), (x + size, y + size), (x, y + size), self.width)
        elif self.walls['right']:
            pygame.draw.line(screen, pygame.Color('darkgreen'), (x + size, y), (x + size, y + size), self.width)

    def check_cells(self, x, y, cols, rows, grid):
        index = lambda x, y: x + y * cols
        if x < 0 or x > cols - 1 or y < 0 or y > rows - 1:
            return False
        return grid[index(x, y)]

    def check_neighbors(self, cols, rows, grid):
        neighbors = []
        top = self.check_cells(self.x, self.y - 1, cols, rows, grid)
        left = self.check_cells(self.x - 1, self.y, cols, rows, grid)
        bottom = self.check_cells(self.x, self.y + 1, cols, rows, grid)
        right = self.check_cells(self.x + 1, self.y, cols, rows, grid)
        if top and not top.visited:
            neighbors.append(top)
        elif left and not left.visited:
            neighbors.append(left)
        elif bottom and not bottom.visited:
            neighbors.append(bottom)
        elif right and not right.visited:
            neighbors.append(right)
        elif neighbors:
            return choice(neighbors)
        else:
            return False
