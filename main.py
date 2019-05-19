import sys
import os
import pygame
from game import World
from singleton import singleton
from handler import EventHandler
from button import Button, Buttons
from image import Image
from characters.characters import MainCharacter
from constants import WIDTH, HEIGHT, GAME_NAME, TICK_RATE, Colors
from logger_decorator import log_usage


def enable_continue():
    """
    check for character existence, if exists then we enable continue
    :return: True if player exists, so he can continue the game
    """
    try:
        file = open(os.path.join('characters', "character.txt"), "x")
        file.close()
        return False
    except FileExistsError:
        return True


def create_character():
    # insert a name, not working, no saves.
    name = "OLEG"
    MainCharacter(name)


# to check how often do players start a game
@log_usage
def play():
    Main().current_handler = GameHandler()


# to check how often do players create a new character
@log_usage
def new_game():
    create_character()
    play()


def settings():
    Main().current_handler = SettingsHandler()


def exit_app():
    pygame.quit()
    sys.exit()


def to_main_menu():
    Main().current_handler = MainMenuHandler()


def create_window():
    """
    initializing window: this implementation is for pygame
    """
    pygame.init()
    pygame.display.init()
    pygame.display.set_caption(GAME_NAME)
    pygame.display.set_mode((WIDTH, HEIGHT))


class Menu:
    """
    Menu class that stores buttons, background image and has method draw
    """

    def __init__(self, buttons: Buttons):
        self._background = Image('BackgroundMainMenu')
        self._buttons = buttons

    def draw(self):
        self._background.draw()
        self._buttons.draw()

    def next(self):
        self._buttons.next()

    def prev(self):
        self._buttons.prev()

    def handle_keyboard_push(self):
        self._buttons.handle_keyboard_push()

    def handle_mouse_click(self, *point):
        self._buttons.handle_mouse_click(point)


@singleton
class MainMenu(Menu):
    def __init__(self):
        if enable_continue():
            continue_button = Button(play, 'Continue', Colors.WHITE,
                                     (WIDTH // 2, HEIGHT // 10 * 2))
        else:
            continue_button = Button(None, 'Continue', Colors.GRAY,
                                     (WIDTH // 2, HEIGHT // 10 * 2))
        start_button = Button(new_game, 'Start a game', Colors.GREEN,
                              (WIDTH // 2, HEIGHT // 10 * 4))
        settings_button = Button(settings, 'Settings', Colors.COOLCOLOR,
                                 (WIDTH // 2, HEIGHT // 10 * 6))
        exit_button = Button(exit_app, 'Exit', Colors.RED,
                             (WIDTH // 2, HEIGHT // 10 * 8))
        super().__init__(
            Buttons(continue_button, start_button, settings_button,
                    exit_button))


@singleton
class Settings(Menu):
    def __init__(self):
        back_button = Button(to_main_menu, 'Exit', Colors.RED,
                             (WIDTH // 2, HEIGHT // 10 * 5))

        super().__init__(Buttons(back_button))


@singleton
class MainMenuHandler(EventHandler):
    def __init__(self):
        self.menu = MainMenu()
        self.menu.draw()

    def on_key_down(self, key):
        if key in (pygame.K_DOWN, pygame.K_s):
            self.menu.next()
        elif key in (pygame.K_UP, pygame.K_w):
            self.menu.prev()
        elif key in (pygame.K_KP_ENTER, pygame.K_RETURN, pygame.K_RIGHT):
            self.menu.handle_keyboard_push()

    def on_key_pressed(self, keys):
        pass

    def on_mouse_click(self, *point):
        self.menu.handle_mouse_click(*point)

    def update(self, changed):
        if changed:
            self.menu.draw()


@singleton
class SettingsHandler(EventHandler):
    def __init__(self):
        self.menu = Settings()
        self.menu.draw()

    def on_key_down(self, key):
        if key in (pygame.K_DOWN, pygame.K_s):
            self.menu.next()
        elif key in (pygame.K_UP, pygame.K_w):
            self.menu.prev()
        elif key in (pygame.K_KP_ENTER, pygame.K_RETURN, pygame.K_RIGHT):
            self.menu.handle_keyboard_push()

    def on_key_pressed(self, keys):
        pass

    def on_mouse_click(self, *point):
        self.menu.handle_mouse_click(*point)

    def update(self, changed):
        if changed:
            self.menu.draw()


@singleton
class GameHandler(EventHandler):
    def __init__(self):
        """
        init the world
        """
        self.world = World()
        self.world.draw()

    def on_key_down(self, key):
        """
        on key down handler
        """

    def on_key_pressed(self, keys):
        self.world.main_character.downward = keys[pygame.K_DOWN] or keys[
            pygame.K_s]
        self.world.main_character.upward = keys[pygame.K_UP] or keys[
            pygame.K_w]
        self.world.main_character.rightward = keys[pygame.K_RIGHT] or keys[
            pygame.K_d]
        self.world.main_character.leftward = keys[pygame.K_LEFT] or keys[
            pygame.K_a]
        return keys[pygame.K_DOWN] or keys[pygame.K_s] or keys[
            pygame.K_UP] or keys[pygame.K_w] or keys[pygame.K_RIGHT] or keys[
                pygame.K_d] or keys[pygame.K_LEFT] or keys[pygame.K_a]

    def on_mouse_click(self, *point):
        """
        on mouse click handler
        """

    def update(self, changed):
        """
        update world handler
        """
        self.world.update()
        self.world.draw()


@singleton
class Main:
    def __init__(self):
        create_window()
        self.current_handler = MainMenuHandler()
        self.clock = pygame.time.Clock()

    def event_loop(self):
        while True:
            changed = False
            self.clock.tick(TICK_RATE)
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if pygame.mouse.get_pressed()[0] == 1:
                        mouse_pt = pygame.mouse.get_pos()
                        self.current_handler.on_mouse_click(mouse_pt)
                elif event.type == pygame.KEYDOWN:
                    self.current_handler.on_key_down(event.key)
                else:
                    continue
                changed = True
            keys = pygame.key.get_pressed()
            self.current_handler.on_key_pressed(keys)
            self.current_handler.update(changed)


if __name__ == '__main__':
    Main().event_loop()
