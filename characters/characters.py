from abc import abstractmethod
from enum import Enum
import pygame
from singleton import singleton
from constants import WIDTH, HEIGHT, Colors


class Unit:
    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def draw(self):
        pass


class Weapons(Enum):
    FISTS = 'fists'
    SWORD = 'sword'
    MAGIC = 'magic'
    BOW = 'bow'


# singleton usage because of the only one main character existence
@singleton
class MainCharacter(Unit):
    def __init__(self, name=""):
        self.race = "Player"
        self.name = name
        self.damage = 1
        self.health = 6
        self.move_speed = 10
        self.armor = 0
        self.weapon = Weapons.FISTS
        self.width = WIDTH // 20
        self.height = HEIGHT // 20
        self.x_cor = (WIDTH - self.width) // 2
        self.y_cor = (HEIGHT - self.height) // 2
        self.rightward = False
        self.downward = False
        self.leftward = False
        self.upward = False

    def attack(self):
        # weapon fists/sword then we check for enemies in front
        # weapon magic/bow then we make a projectile
        pass

    def update(self):
        diag_diff = round(self.move_speed - ((self.move_speed ** 2) / 2) ** .5)
        if not (self.downward and self.upward):
            if self.upward:
                self.y_cor -= self.move_speed
                if self.rightward or self.leftward:
                    self.y_cor += diag_diff
            if self.downward:
                self.y_cor += self.move_speed
                if self.rightward or self.leftward:
                    self.y_cor -= diag_diff
        if not (self.rightward and self.leftward):
            if self.rightward:
                self.x_cor += self.move_speed
                if self.upward or self.downward:
                    self.x_cor -= diag_diff
            if self.leftward:
                self.x_cor -= self.move_speed
                if self.upward or self.downward:
                    self.x_cor += diag_diff

    def draw(self):
        rectangle = (int(self.x_cor), int(self.y_cor),
                     int(self.width), int(self.height))
        screen = pygame.display.get_surface()
        pygame.draw.rect(screen, Colors.RED, rectangle)


class Enemies(Unit):
    """
    Enemies are created using factory method, because we want to expand types
    """
    def __init__(self):
        self.move_speed = 5
        self.rightward = False
        self.downward = False
        self.leftward = False
        self.upward = False
        self.x_cor = 0
        self.y_cor = 0
        self.height = HEIGHT // 20
        self.width = WIDTH // 20

    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def attack(self):
        pass

    def draw(self):
        """
        should be an abstract method
        """
        rectangle = (int(self.x_cor), int(self.y_cor),
                     int(self.width), int(self.height))
        screen = pygame.display.get_surface()
        pygame.draw.rect(screen, Colors.COOLCOLOR, rectangle)
