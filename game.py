from factory import *
from characters import *
import pygame
import random
import sys

tick_rate = 30
gray = (42, 42, 42)
clock = pygame.time.Clock()
width = 640
height = 480


class Room:
    # creating some enemies in the room and tells if it is a bonus
    # will be a graph sometime
    def __init__(self):
        self.enemies = {BeeFactory().create(random.randint(width // 2, width),
                                            random.randint(0, height // 2))
                        for _ in range(random.randint(1, 3))}
        self.enemies.update({SpiderFactory().create(
            random.randint(0, width // 2),
            random.randint(0, height // 2)) for _ in
            range(random.randint(0, 3))})
        self.bonus = random.randint(1, 10) > 8
        self.doors = random.randint(1, 4)


def draw_characters(room):
    pass


def main():
    character_info = open("character.txt", "r").readlines()
    main_character = MainCharacter()
    for i in range(len(character_info)):
        key, val = character_info[i].strip("\n").split(" ")
        main_character.__dict__[key] = val

    pygame.init()
    pygame.display.set_caption("Dungeon")
    screen = pygame.display.set_mode((width, height))

    current_room = Room()

    while True:
        clock.tick(tick_rate)
        screen.fill(gray)
        draw_characters(current_room)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()
