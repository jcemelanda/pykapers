from sys import exit

import pygame


class Scene:
    def draw(self):
        pass

    def update(self):
        pass

    def handle_events(self):
        pass


class GameScene(Scene):
    pass


class MainGame:
    def __init__(self):
        pygame.init()
        self.score = 0
        self.lifes = 4
        self.screen = pygame.display.set_mode((956, 560), 0, 32)
        self.current_scene = GameScene()

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
