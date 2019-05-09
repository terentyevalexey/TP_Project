from abc import abstractmethod
from singleton import singleton


class Unit:
    @abstractmethod
    def move(self):
        pass


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
        self.weapon = "fists"
        self.x_cor = 0
        self.y_cor = 0
        self.rightward = False
        self.downward = False
        self.leftward = False
        self.upward = False

    def attack(self, enemies):
        # weapon fists/sword then we check for enemies in front
        # weapon magic/bow then we make a projectile
        pass

    def move(self):
        diag_diff = round(self.move_speed - ((self.move_speed ** 2) / 2) ** .5)
        if not (self.downward and self.upward):
            if self.upward:
                self.y_cor += self.move_speed
                if self.rightward | self.leftward:
                    self.y_cor -= diag_diff
            if self.downward:
                self.y_cor -= self.move_speed
                if self.rightward | self.leftward:
                    self.y_cor += diag_diff
        if not (self.rightward and self.leftward):
            if self.rightward:
                self.x_cor += self.move_speed
                if self.upward | self.downward:
                    self.x_cor -= diag_diff
            if self.leftward:
                self.x_cor -= self.move_speed
                if self.upward | self.downward:
                    self.x_cor += diag_diff


class Enemies(Unit):
    """
    Enemies are created using factory method, because we want to expand types
    """

    @abstractmethod
    def move(self):
        pass

    @abstractmethod
    def attack(self):
        pass
