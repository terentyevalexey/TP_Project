from collections.abc import Iterable
import pygame
from constants import WIDTH, HEIGHT, CALIBRI, Colors


class Button:
    """
    button class
    """

    def __init__(self, action, text, color, *rect):
        """
        :param action: button action        :type function
        :param text: button text            :type string
        :param color: color of button       :type tuple(int, int, int)
        :param rect: (center_x, center_y, width, height) or (c_x, c_y)
        """
        if len(rect) == 1:
            rect = rect[0]
        if len(rect) == 2:
            center_x, center_y = rect
            height = HEIGHT // 10
            width = WIDTH // 5 * 2
        elif len(rect) == 4:
            center_x, center_y, width, height = rect
        else:
            raise TypeError("wrong amount of arguments")
        self.action = action
        self.rectangle = pygame.Rect(center_x - width // 2,  # left
                                     center_y - height // 2,  # top
                                     width,  # width
                                     height  # height
                                     )
        self.color = color
        font_division_ratio = 2  # font size is this times less than rectangle
        text_y_shift = 0.04  # to center the text for perfectionists
        font_height = self.rectangle.height // font_division_ratio
        self.font = pygame.font.SysFont(CALIBRI, font_height, True)
        self.text = self.font.render(text, True, Colors.BLACK)
        self.text_rect = self.text.get_rect()
        self.text_rect.centerx = self.rectangle.centerx
        self.text_rect.centery = self.rectangle.centery + int(
            self.rectangle.height * text_y_shift)

    def draw(self, surface=None):
        """
        draw button
        :param surface: surface to blit a button on :type pygame surface
        """
        if surface is None:
            surface = pygame.display.get_surface()
        pygame.draw.rect(surface, self.color, self.rectangle)
        surface.blit(self.text, self.text_rect)
        pygame.display.update()

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
            self.action()


class Buttons:
    def __init__(self, *buttons):
        if len(buttons) == 1 and isinstance(buttons[0], Iterable):
            buttons = buttons[0]
        self._buttons = buttons
        self.cur_state = 0

    def draw(self):
        for button in self._buttons:
            button.draw()

    def next(self):
        if self.cur_state < len(self._buttons) - 1:
            self.cur_state += 1

    def prev(self):
        if self.cur_state > 0:
            self.cur_state -= 1

    def handle_keyboard_push(self):
        if self._buttons:
            self._buttons[self.cur_state].push()

    def handle_mouse_click(self, *point):
        for button in self._buttons:
            if button.has(point):
                button.push()
