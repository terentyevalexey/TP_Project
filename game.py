import random
import sys
from enum import Enum
import pygame
import factory
from background import Background
from maze_generator import Maze
from singleton import singleton
from characters import characters
from constants import HEIGHT, WIDTH, TICK_RATE, Colors


class Directions(Enum):
    LEFT = 0
    TOP = 1
    RIGHT = 2
    DOWN = 3


class Door:
    """
    door class
    """

    def __init__(self, direction):
        self.side = direction
        if direction == Directions.LEFT:
            self.rectangle = (0, HEIGHT // 5 * 2, WIDTH // 10, HEIGHT // 5)
        elif direction == Directions.TOP:
            self.rectangle = (WIDTH // 5 * 2, 0, WIDTH // 5, HEIGHT // 10)
        elif direction == Directions.RIGHT:
            self.rectangle = (WIDTH - WIDTH // 10, HEIGHT // 5 * 2,
                              WIDTH // 10, HEIGHT // 5)
        elif direction == Directions.DOWN:
            self.rectangle = (WIDTH // 5 * 2, HEIGHT - HEIGHT // 10,
                              WIDTH // 5, HEIGHT // 10)

    def has(self, *point):
        return pygame.Rect(self.rectangle).collidepoint(*point)

    def draw(self):
        screen = pygame.display.get_surface()
        pygame.draw.rect(screen, Colors.GREEN, self.rectangle)
        pygame.display.update()


class Doors:
    """
    doors class that contains doors and handles interactions with them
    """

    def __init__(self, directions):
        self._doors = []
        for i in range(4):
            if directions[i]:
                self._doors.append(Door(i))

    def draw(self):
        for door in self._doors:
            door.draw()


class EnemyArmy:
    def __init__(self):
        self.enemies = [
            factory.BeeFactory().create(random.randint(WIDTH // 2, WIDTH),
                                        random.randint(0, HEIGHT // 2))
            for _ in range(random.randint(1, 3))]
        self.enemies.extend([factory.SpiderFactory().create(
            random.randint(0, WIDTH // 2), random.randint(0, HEIGHT // 2)
        ) for _ in range(random.randint(0, 3))])

    def draw(self):
        for enemy in self.enemies:
            enemy.draw()


class Room:
    def __init__(self, directions):
        """
        creating enemies, doors, borders, setting main character's position
        there is chance to be a bonus room
        :param directions: 4 bool tuple for doors existence
        """
        self.background = Background('BackgroundRoom')
        self.enemies = EnemyArmy()
        self.bonus = random.randint(1, 10) > 8
        self.doors = Doors(Directions(directions))

    def draw(self):
        """
        draw background(floor and walls texture), doors, enemies, player
        """
        self.background.draw()
        self.doors.draw()
        self.enemies.draw()


@singleton
class World:
    def __init__(self):
        """
        generate a maze, create hero
        dungeon is the Matrix of Rooms
        """
        # creating character from the save file
        with open("character.txt", "r").readlines() as character_info:
            self.main_character = characters.MainCharacter()
            for string in character_info:
                key, val = string.strip("\n").split(" ")
                self.main_character.__dict__[key] = val
        # creating a maze of rooms
        width = height = 10  # number of rooms in row / column
        min_dist = width // 2  # min manhattan distance between begin and end
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
        self.current_room = begin  # coordinates of current room

    def draw(self):
        """
        draw dungeon:
        draw current room with enemies
        draw main character
        """
        self.dungeon[self.current_room[0]][self.current_room[1]].draw()
        self.main_character.draw()


def game_loop():
    # seems useless, will be replaced for a GameHandler
    clock = pygame.time.Clock()
    screen = pygame.display.get_surface()
    world = World()
    while True:
        clock.tick(TICK_RATE)
        screen.fill(Colors.GRAY)
        world.draw()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()
