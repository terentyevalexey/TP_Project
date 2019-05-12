import random
import sys
import pygame
import factory
from maze_generator import Maze
from singleton import singleton
from characters import characters
from constants import HEIGHT, WIDTH, TICK_RATE, Colors


class Room:
    # creating some enemies in the room and tells if it is a bonus
    # will be a graph sometime
    def __init__(self, doors):
        self.enemies = {
            factory.BeeFactory().create(random.randint(WIDTH // 2, WIDTH),
                                        random.randint(0, HEIGHT // 2))
            for _ in range(random.randint(1, 3))}
        self.enemies.update({factory.SpiderFactory().create(
            random.randint(0, WIDTH // 2), random.randint(0, HEIGHT // 2)
        ) for _ in range(random.randint(0, 3))})
        self.bonus = random.randint(1, 10) > 8
        self.doors = doors  # LEFT UP RIGHT DOWN

    def draw(self):
        for _ in self.enemies:
            pass


@singleton
class World:
    def __init__(self):
        """
        generate a maze
        """
        width = height = 10
        min_dist = width // 2
        begin = (random.randint(0, width - 1), random.randint(0, height - 1))
        possible_ends = []
        for i in range(height):
            for j in range(width):
                if begin[0] - i + begin[1] - j > min_dist:
                    possible_ends.append((i, j))
        end = random.choice(possible_ends)
        maze = Maze(width, height, begin, end)
        self.dungeon = [
            [Room(maze.accessible_sides((i, j))) for i in range(height)]
            for j in range(width)]


def game_loop():
    character_info = open("character.txt", "r").readlines()
    main_character = characters.MainCharacter()
    for string in character_info:
        key, val = string.strip("\n").split(" ")
        main_character.__dict__[key] = val

    current_room = Room((0, 0, 0, 0))
    clock = pygame.time.Clock()
    screen = pygame.display.get_surface()

    while True:
        clock.tick(TICK_RATE)
        screen.fill(Colors.GRAY)
        current_room.draw()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()
