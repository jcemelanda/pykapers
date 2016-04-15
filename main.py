from sys import exit

import pygame
from pygame import Color
from pygame import Rect
from pygame.sprite import Sprite
from pygame.sprite import Group
from pygame import FULLSCREEN
from pygame import DOUBLEBUF
from pygame import HWSURFACE
from pygame import K_ESCAPE


FLAGS = FULLSCREEN | HWSURFACE | DOUBLEBUF


class Ball(Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([10, 10])
        self.image.fill(Color('red'))

        self.rect = self.image.get_rect()

    def update(self):
        self.rect = self.rect.move(10, 0)

class Scene:
    def __init__(self):
        self.sprites = Group()

    def draw(self):
        pass

    def update(self):
        pass

    def handle_events(self):
        pass


class GameScene(Scene):
    def __init__(self, size):
        super().__init__()
        self.score = 0
        self.lifes = 4
        self.movement = -10
        self.bg_size = (size[0] * 3, int(1000 / 1080 * size[1]))
        self.bg = pygame.transform.scale(
            pygame.image.load('bg.png').convert(),
            self.bg_size)
        self.screen = pygame.display.set_mode(size, FLAGS, 32)
        self.camera = Rect(self.bg_size[0]-size[0], 0, *size)
        self.release_ball = False
        self.ball_cooldown = 20

    def draw(self):
        self.screen.blit(self.bg, (0, 0), self.camera)
        self.sprites.draw(self.screen)

    def update(self):
        if self.camera.x <= 0:
            print('invert')
            self.movement *= -1
        elif self.camera.x > self.bg_size[0]-self.camera.width:
            print('invert')
            self.movement *= -1
        self.camera = self.camera.move(self.movement, 0)
        if self.ball_cooldown:
            self.ball_cooldown -= 1
        else:
            self.ball_cooldown = 20
            self.sprites.add(Ball())
        self.sprites.update()


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
