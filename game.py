import random
import sys
import pygame
import factory
import characters

TICK_RATE = 30
GRAY = (42, 42, 42)
CLOCK = pygame.time.Clock()
WIDTH = 640
HEIGHT = 480
GAME_NAME = "Dungeon"


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


def main():
    character_info = open("character.txt", "r").readlines()
    main_character = characters.MainCharacter()
    for string in character_info:
        key, val = string.strip("\n").split(" ")
        main_character.__dict__[key] = val

    pygame.init()
    pygame.display.set_caption(GAME_NAME)
    screen = pygame.display.set_mode((WIDTH, HEIGHT))

    current_room = Room()

    while True:
        CLOCK.tick(TICK_RATE)
        screen.fill(GRAY)
        draw_characters(current_room)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()
