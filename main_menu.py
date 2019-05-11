import pygame
import game
from button import Button
from characters.characters import MainCharacter
from constants import WIDTH, HEIGHT, GAME_NAME, Colors


def enable_continue():
    """
    check for character existence, if exists then we enable continue
    :return: True if player exists, so he can continue the game
    """
    try:
        file = open("character.txt", "x")
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


def new_game():
    create_character()
    game.main()


def create_window():
    """
    initializing window: this implementation is for pygame
    """
    pygame.init()
    pygame.display.init()
    pygame.display.set_caption(GAME_NAME)
    pygame.display.set_mode((WIDTH, HEIGHT))


def make_buttons():
    return (Button(new_game, 'Start a game', Colors.GREEN,
                   (WIDTH // 2, HEIGHT // 2)),)


def event_loop():
    """
    main menu loop:
    initializing window,
    following commands:
    start new game
    continue
    settings
    exit
    """
    create_window()
    buttons = make_buttons()
    while True:
        for button in buttons:
            button.draw()


if __name__ == '__main__':
    event_loop()
