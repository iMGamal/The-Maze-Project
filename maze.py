import pygame
from cell import Cell

class Maze:
    def __init__(self, cols, rows):
        self.cols = cols
        self.rows = rows
        self.width = 4
        self.grid = [Cell(i, j, self.width) for x in range(self.cols) for j in range(self.rows)]

    def remove_walls(self, current, next):
        diff_x = current.x - next.x
        if diff_x == 1:
            current.walls['left'] = False
            next.walls['right'] = False
        elif diff_x == -1:
            current.walls['right'] = False
            next.walls['left'] = False
        diff_y = current.y - next.y
        if diff_y == 1:
            current.walls['top'] = False
            next.walls['bottom'] = False
        elif diff_y == -1:
            current.walls['bottom'] = False
            next.walls['top'] = False

    def generate_maze(self):
        current_cell = self.grid[0]
        maze_array = []
        count = 1
        while count != len(self.grid):
            current_cell.visited = True
            next_cell = current_cell.check_neighbors(self.cols, self.rows, self.grid)
            if next_cell:
                next_cell.visited = True
                count += 1
                maze_array.append(current_cell)
                self.remove_walls(current_cell, next_cell)
                current_cell = next_cell
            elif maze_array:
                current_cell = maze_array.pop()

        return self.grid
