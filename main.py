from sys import exit

import pygame
from pygame import FULLSCREEN
from pygame import DOUBLEBUF
from pygame import HWSURFACE
from pygame import K_ESCAPE

from scenes import GameScene


FLAGS = FULLSCREEN | HWSURFACE | DOUBLEBUF


class MainGame:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((956, 560), FLAGS, 32)
        self.current_scene = GameScene((956, 560))

    def run(self):
        clock = pygame.time.Clock()
        while True:
            self.handle_events()
            self.update()
            self.draw()
            time_passed = clock.tick(30)

    def draw(self):
        self.current_scene.draw()
        pygame.display.update()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit(0)
        keys = pygame.key.get_pressed()
        if keys[K_ESCAPE]:
            exit(0)
        self.current_scene.handle_events()

    def update(self):
        self.current_scene.update()

if __name__ == '__main__':
    MainGame().run()
