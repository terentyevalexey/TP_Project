from singleton import singleton


class Unit:
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
        if not (self.downward and self.upward):
            if self.upward:
                self.y_cor += 10
                if self.rightward | self.leftward:
                    self.y_cor -= 3
            if self.downward:
                self.y_cor -= 10
                if self.rightward | self.leftward:
                    self.y_cor += 3
        if not (self.rightward and self.leftward):
            if self.rightward:
                self.x_cor += 10
                if self.upward | self.downward:
                    self.x_cor -= 3
            if self.leftward:
                self.x_cor -= 10
                if self.upward | self.downward:
                    self.x_cor += 3


# here we will use factory method to create Enemies, because we
# may want to expand Enemies types
class Enemies(Unit):
    def move(self):
        pass

    def attack(self):
        pass
