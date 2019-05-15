import random
from enum import Enum
import pygame
import factory
from image import Image
from maze_generator import Maze
from singleton import singleton
from characters import characters
from constants import HEIGHT, WIDTH, Colors


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

    def has(self, *rect):
        return pygame.Rect(self.rectangle).colliderect(rect)

    def draw(self):
        screen = pygame.display.get_surface()
        pygame.draw.rect(screen, Colors.GREEN, self.rectangle)


class Doors:
    """
    doors class that contains doors and handles interactions with them
    """

    def __init__(self, directions):
        self._doors = []
        for i in range(4):
            if directions[i]:
                self._doors.append(Door(Directions(i)))

    def draw(self):
        for door in self._doors:
            door.draw()

    def in_door(self, *rect):
        for door in self._doors:
            if door.has(*rect):
                return door.side
        return None


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

    def update(self, goto_x_cor, goto_y_cor, goto_width, goto_height):
        for enemy in self.enemies:
            enemy.downward = goto_y_cor + goto_height >= \
                             enemy.y_cor + enemy.height
            enemy.upward = goto_y_cor <= enemy.y_cor
            enemy.leftward = goto_x_cor <= enemy.x_cor
            enemy.rightward = goto_x_cor + goto_width >= \
                enemy.x_cor + enemy.width
            enemy.update()


class Room:
    def __init__(self, directions):
        """
        creating enemies, doors, borders, setting main character's position
        there is chance to be a bonus room
        :param directions: 4 bool tuple for doors existence
        """
        # self.background = Image('BackgroundRoom')
        self.background = Image('BackgroundMainMenu')
        self.enemies = EnemyArmy()
        self.bonus = random.randint(1, 10) > 8
        self.doors = Doors(directions)

    def draw(self):
        """
        draw background(floor and walls texture), doors, enemies
        """
        self.background.draw()
        self.doors.draw()
        self.enemies.draw()

    def update(self, *rect):
        self.enemies.update(*rect)
        return self.doors.in_door(*rect)


@singleton
class World:
    def __init__(self):
        """
        generate a maze, create hero
        dungeon is the Matrix of Rooms
        """
        # creating character from the save file
        self.main_character = characters.MainCharacter()
        # creating a maze of rooms
        width = height = 10  # number of rooms in row / column
        min_dist = width // 2 - 2  # min manhattan distance between begin 7 end
        begin = (random.randint(0, width - 1), random.randint(0, height - 1))
        possible_ends = []
        for i in range(height):
            for j in range(width):
                if abs(begin[0] - i) + abs(begin[1] - j) > min_dist:
                    possible_ends.append((i, j))
        end = random.choice(possible_ends)
        maze = Maze(width, height, begin, end)
        self.dungeon = [
            [Room(maze.accessible_sides((i, j))) for i in range(height)]
            for j in range(width)]
        self.cur_room_xy = begin  # coordinates of current room

    def draw(self):
        """
        draw dungeon:
        draw current room with enemies
        draw main character
        """
        self.dungeon[self.cur_room_xy[0]][self.cur_room_xy[1]].draw()
        self.main_character.draw()
        pygame.display.update()

    def update(self):
        self.main_character.update()
        cur_room = self.dungeon[self.cur_room_xy[0]][self.cur_room_xy[1]]
        in_door = cur_room.update(self.main_character.x_cor,
                                  self.main_character.y_cor,
                                  self.main_character.width,
                                  self.main_character.height)
        player = self.main_character
        if in_door == Directions.LEFT:
            self.cur_room_xy = (self.cur_room_xy[0], self.cur_room_xy[1] - 1)
            self.main_character.x_cor = WIDTH - player.x_cor - player.width
        elif in_door == Directions.RIGHT:
            self.cur_room_xy = (self.cur_room_xy[0], self.cur_room_xy[1] + 1)
            self.main_character.x_cor = WIDTH - player.x_cor + player.width
        elif in_door == Directions.TOP:
            self.cur_room_xy = (self.cur_room_xy[0] - 1, self.cur_room_xy[1])
            self.main_character.y_cor = HEIGHT - player.y_cor - player.height
        elif in_door == Directions.DOWN:
            self.cur_room_xy = (self.cur_room_xy[0] + 1, self.cur_room_xy[1])
            self.main_character.y_cor = HEIGHT - player.y_cor + player.height
