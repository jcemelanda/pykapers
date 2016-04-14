from sys import exit

import pygame
from pygame import Rect


class Scene:
    def draw(self):
        pass

    def update(self):
        pass

    def handle_events(self):
        pass


class GameScene(Scene):
    def __init__(self, size):
        self.score = 0
        self.lifes = 4
        bg_size = (size[0] * 3, int(1000 / 1080 * size[1]))
        self.bg = pygame.transform.scale(
            pygame.image.load('bg.png').convert(),
            bg_size)
        self.screen = pygame.display.set_mode(size, 0, 32)
        self.camera = Rect(bg_size[0]-size[0], 0, *size)

    def draw(self):
        self.screen.blit(self.bg, (0, 0), self.camera)


class MainGame:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((956, 560), 0, 32)
        self.current_scene = GameScene((956, 560))

    def run(self):
        while True:
            self.handle_events()
            self.update()
            self.draw()

    def draw(self):
        self.current_scene.draw()
        pygame.display.update()

    def handle_events(self):
        self.current_scene.handle_events()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

    def update(self):
        self.current_scene.update()

if __name__ == '__main__':
    MainGame().run()
