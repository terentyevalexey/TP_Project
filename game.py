import random
import sys
import factory
import pygame
from characters import characters
from constants import *


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
        screen.fill(GRAY)
        draw_characters(current_room)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()


def main():
    game_loop()
