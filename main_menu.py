import pygame
import sys
import os
from game import GameHandler
from singleton import singleton
from handler import EventHandler
from button import Button, Buttons
from background import Background
from characters.characters import MainCharacter
from constants import WIDTH, HEIGHT, GAME_NAME, Colors


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
    # insert a name
    name = "OLEG"
    main_character = MainCharacter(name)
    character_info = open("character.txt", "w")
    for attr_name in main_character.__dict__:
        character_info.write(
            attr_name + " " + str(main_character.__dict__[attr_name]) + "\n")
    character_info.close()


def play():
    Main().current_handler = GameHandler()


def new_game():
    create_character()
    play()


def settings():
    pass


def exit_app():
    pygame.quit()
    sys.exit()


def create_window():
    """
    initializing window: this implementation is for pygame
    """
    pygame.init()
    pygame.display.init()
    pygame.display.set_caption(GAME_NAME)
    pygame.display.set_mode((WIDTH, HEIGHT))


@singleton
class MainMenu:
    """
    Menu class that stores buttons, background image and has method draw
    """

    def __init__(self, buttons: Buttons):
        self._background = Background('BackgroundMainMenu')
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


def make_buttons():
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

    return Buttons(continue_button, start_button, settings_button, exit_button)


@singleton
class MainMenuHandler(EventHandler):
    def __init__(self):
        buttons = make_buttons()
        self.menu = MainMenu(buttons)
        self.menu.draw()

    def on_key_down(self, key):
        if key == pygame.K_DOWN and pygame.K_s:
            self.menu.next()
        elif key == pygame.K_UP and pygame.K_w:
            self.menu.prev()
        elif key in (pygame.K_KP_ENTER, pygame.K_RETURN, pygame.K_LEFT):
            self.menu.handle_keyboard_push()

    def on_mouse_click(self, *point):
        self.menu.handle_mouse_click(*point)

    def update(self):
        self.menu.draw()


def check_events(handler):
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0] == 1:
                mouse_pt = pygame.mouse.get_pos()
                handler.on_mouse_click(mouse_pt)
        elif event.type == pygame.KEYDOWN:
            handler.on_key_down(event.key)
        else:
            continue
        handler.update()


@singleton
class Main:
    def __init__(self):
        create_window()
        self.current_handler = MainMenuHandler()

    def event_loop(self):
        while True:
            check_events(self.current_handler)


if __name__ == '__main__':
    loop = Main()
    loop.event_loop()
