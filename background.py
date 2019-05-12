import os
import pygame
from constants import WIDTH, HEIGHT


class Background:
    def __init__(self, name, png=False):
        if png:
            self._background = pygame.image.load(os.path.join('data',
                                                              f'{name}.png'))
        else:
            self._background = pygame.image.load(os.path.join('data',
                                                              f'{name}.jpg'))

    def draw(self):
        screen = pygame.display.get_surface()
        screen.blit(pygame.transform.scale(self._background, (WIDTH, HEIGHT)),
                    (0, 0))
        pygame.display.update()
