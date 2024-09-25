import pygame

class Player:
    def __init__(self, x, y):
        self.x = int(x)
        self.y = int(y)
        self.player_size = 10
        self.rect = pygame.Rect(self.x, self.y, self.player_size, self.player_size)
        self.color = (250, 120, 60)
        self.vel_x = 0
        self.vel_y = 0
        self.top_pressed = False
        self.left_pressed = False
        self.bottom_pressed = False
        self.right_pressed = False
        self.speed = 4

    def get_current(self, x, y, grid):
        for cell in grid:
            if cell.x == x and cell.y == y:
                return cell

    def move(self, size, grid, width):
        current_x = self.x // size
        current_y = self.y // size
        current = self.get_current(current_x, current_y, grid)
        current_ax = current_x * size
        current_ay = current_y * size
        if self.top_pressed:
            if current.walls['top']:
                if self.y <= current_ay + width:
                    self.top_pressed = False
        elif self.left_pressed:
            if current.walls['left']:
                if self.x <= current_ax + width:
                    self.left_pressed = False
        elif self.bottom_pressed:
            if current.walls['bottom']:
                if self.y >= current_ax + width:
                    self.bottom_pressed = False
        elif self.right_pressed:
            if current.walls['right']:
                if self.x >= current_ay + width:
                    self.right_pressed = False

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)

    def update(self):
        if self.top_pressed and not self.bottom_pressed:
            self.vel_y -= self.speed
        elif self.left_pressed and not self.right_pressed:
            self.vel_x -= self.speed
        elif self.bottom_pressed and not self.top_pressed:
            self.y += self.speed
        elif self.right_pressed and not self.left_pressed:
            self.x += self.speed
        self.x += self.vel_x
        self.y += self.vel_y
        self.rect = pygame.Rect(int(self.x), int(self.y), self.player_size, self.player_size)
