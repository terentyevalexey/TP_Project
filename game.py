import random
import sys
import pygame
import factory
from handler import EventHandler
from characters import characters
from constants import HEIGHT, WIDTH, TICK_RATE, Colors


class Room:
    # creating some enemies in the room and tells if it is a bonus
    # will be a graph sometime
    def __init__(self):
        self.enemies = {
            factory.BeeFactory().create(random.randint(WIDTH // 2, WIDTH),
                                        random.randint(0, HEIGHT // 2))
            for _ in range(random.randint(1, 3))}
        self.enemies.update({factory.SpiderFactory().create(
            random.randint(0, WIDTH // 2), random.randint(0, HEIGHT // 2)
        ) for _ in range(random.randint(0, 3))})
        self.bonus = random.randint(1, 10) > 8
        self.doors = random.randint(1, 4)


def draw_characters(room: Room):
    for _ in room.enemies:
        pass


def game_loop():
    character_info = open("character.txt", "r").readlines()
    main_character = characters.MainCharacter()
    for string in character_info:
        key, val = string.strip("\n").split(" ")
        main_character.__dict__[key] = val

    current_room = Room()
    clock = pygame.time.Clock()
    screen = pygame.display.get_surface()

    while True:
        clock.tick(TICK_RATE)
        screen.fill(Colors.GRAY)
        draw_characters(current_room)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()


class GameHandler(EventHandler):
    def __init__(self):
        """
        init the world
        """

    def on_key_down(self, key):
        """
        on key down handler
        """

    def on_mouse_click(self, *point):
        """
        on mouse click handler
        """

    def update(self):
        """
        update world handler
        """
