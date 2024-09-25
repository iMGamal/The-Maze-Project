import pygame
import time

pygame.font.init()

class Clock:
    def __init__(self):
        self.start = None
        self.passed = 0
        self.font = pygame.font.SysFont('monospace', 35)
        self.message_color = pygame.Color('yellow')
    
    def begin(self):
        self.start = time.time()

    def update(self):
        if self.start not None:
            self.passed = time.time() - self.start

    def display(self):
        seconds = int(self.passed % 60)
        minutes = int(self.passed / 60)
        my_time = self.font.render(f"{minutes:02}:{seconds:02}", True, self.message_color)
        return my_time

    def stop(self):
        self.start = None
