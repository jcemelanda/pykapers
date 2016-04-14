from sys import exit

import pygame


pygame.init()
score = 0
lifes = 4

screen = pygame.display.set_mode((956, 560), 0, 32)


def handle_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()


def draw():
    pygame.display.update()


def main():
    while True:
        handle_events()
        draw()

if __name__ == '__main__':
    main()
