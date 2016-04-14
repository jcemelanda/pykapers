from sys import exit

import pygame


class MainGame:
    def __init__(self):
        pygame.init()
        self.score = 0
        self.lifes = 4
        self.screen = pygame.display.set_mode((956, 560), 0, 32)

    def run(self):
        while True:
            self.handle_events()
            self.draw()

    def draw(self):
        pygame.display.update()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

if __name__ == '__main__':
    MainGame().run()
