import pygame
from constants import *

pygame.init()
pygame.display.set_mode((WIDTH, HEIGHT))


class Button:
    """
    button class
    """

    def __init__(self, action, text, color, center, height=HEIGHT // 10,
                 width=WIDTH // 5 * 2):
        """
        :param action: button action        :type function
        :param text: button text            :type string
        :param color: color of button       :type tuple(int, int, int)
        :param center: pair of coordinates  :type tuple(int, int)

        :param height: height               :type int
        :param width: width                 :type int
        """
        self.action = action
        self.rectangle = pygame.Rect(center[0] - width // 2,  # left
                                     center[1] - height // 2,  # top
                                     width,  # width
                                     height  # height
                                     )
        self.color = color
        font_division_ratio = 2  # font size is this times less than rectangle
        text_y_shift = 0.04  # to center the text for perfectionists
        font_height = self.rectangle.height // font_division_ratio
        self.font = pygame.font.SysFont(CALIBRI, font_height, True)
        self.text = self.font.render(text, True, BLACK)
        self.text_rect = self.text.get_rect()
        self.text_rect.centerx = self.rectangle.centerx
        self.text_rect.centery = self.rectangle.centery + int(
            self.rectangle.height * text_y_shift)

    def draw(self, surface=pygame.display.get_surface()):
        """
        draw button
        :param surface: surface to blit a button on :type pygame surface
        """
        pygame.draw.rect(surface, self.color, self.rectangle)
        surface.blit(self.text, self.text_rect)

    def has(self, *point):
        """
        checks if point is in the button rectangular
        :param point: pair of coordinates        :type (int, int)
        :return: True if point is in the button  :type bool
        """
        return self.rectangle.collidepoint(*point)

    def push(self):
        """
        activates button action
        :return: result of an action or None if the action is not callable
        """
        if callable(self.action):
            return self.action()
        else:
            return None
