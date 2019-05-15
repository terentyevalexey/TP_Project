import os
import pygame
from constants import WIDTH, HEIGHT


class Image:
    def __init__(self, name, png=False):
        if png:
            self._image = pygame.image.load(os.path.join('data',
                                                         f'{name}.png'))
        else:
            self._image = pygame.image.load(os.path.join('data',
                                                         f'{name}.jpg'))

    def draw(self):
        screen = pygame.display.get_surface()
        screen.blit(pygame.transform.scale(self._image, (WIDTH, HEIGHT)),
                    (0, 0))
        pygame.display.update()
