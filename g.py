import pygame

pygame.font.init()

class Game:
    def __init__(self, goal, size):
        self.goal = goal
        self.size = size
        self.font = pygame.font.SysFont('impact', 35)
        self.message_color = pygame.Color('darkorange')

    def add_goal(self, screen):
        img_path = ''
        img = pygame.image.load(img_path)
        img = pygame.transform.scale(img, (self.size, self.size))
        screen.blit(img, (self.goal.x * self.size, self.goal.y * self.size))

    def message(self):
        message = self.font.render('You win!', True, self.message_color)
        return message

    def game_over(self, player):
        goal_ax = self.goal.x * self.size
        goal_ay = self.goal.y * self.size
        if player.x >= goal_ax and player.y >= goal_ay:
            return True
        else:
            return False
