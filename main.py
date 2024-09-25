import pygame
from maze import Maze
from game import Game
from clock import Clock
from player import Player

pygame.init()
pygame.font.init()

class Main():
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.SysFont('impact', 30)
        self.running = True
        self.over = False
        self.fps = pygame.time.Clock()

    def instructions(self):
        instructions1 = self.font.render('Use', True, self.message_color)
        instructions2 = self.font.render('Arrow Keys', True, self.message_color)
        instructions3 = self.font.render('to Move', True, self.message_color)
        self.screen.blit(instructions1,(655,300))
        self.screen.blit(instructions2,(610,331))
        self.screen.blit(instructions3,(630,362))

    def render(self, maze, size, player, game, clock):
        [cell.draw(self.screen, size) for cell in maze.grid]
        game.add_goal(self.screen)
        player.draw(self.screen)
        player.update()
        self.instructions()
        if self.game_over:
            clock.stop()
            self.screen.blit(game.message(), (610, 120))
        else:
            clock.update()
        self.screen.blit(clock.display(), (625, 200))
        pygame.display.update()

    def main(self, frame, size):
        cols = frame[0] // size
        rows = frame[-1] // size
        maze = Maze(cols, rows)
        game = Game(maze.grid[-1], size)
        player = Player(size // 3, size // 3)
        clock = Clock()
        maze.generate_maze()
        clock.start()
        while self.running:
            self.screen.fill('gray')
            self.screen.fill(pygame.Color('darkslategray'), (603, 0, 752, 752))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            if event.type == pygame.KEYDOWN and not self.over:
                if event.key == pygame.K_UP:
                    player.top_pressed = True
                elif event.key == pygame.K_LEFT:
                    player.left_pressed = True
                elif event.key == pygame.K_DOWN:
                    player.bottom_pressed = True
                elif event.key == pygame.K_RIGHT:
                    player.right_pressed = True
                player.move(size, maze.grid, maze.width)
            if game.game_over(player):
                self.over = True
                player.top_pressed = False
                player.left_pressed = False
                player.bottom_pressed= False
                player.right_pressed = False
            self.render(maze, size, player, game, clock)
            self.fps.tick(60)

    if __name__ == "__main__":
        window_size = (602, 602)
        screen = (window_size[0] + 150, window_size[-1])
        tile_size = 30
        screen = pygame.display.set_mode(screen)
        pygame.display.set_caption("The Maze")
        game = Main(screen)
        game.main(window_size, tile_size)
