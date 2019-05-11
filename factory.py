from characters.characters import Enemies
from characters.bee import Bee
from characters.archer import Archer
from characters.spider import Spider
from characters.scorpion import Scorpion
from characters.zombie import Zombie


class EnemyFactory:
    def create(self, x_cor=0, y_cor=0):  # pylint: disable=no-self-use
        obj = Enemies()
        obj.race = 'Enemy'
        obj.x_cor = x_cor
        obj.y_cor = y_cor
        return obj


class SpiderFactory(EnemyFactory):
    def create(self, x_cor=0, y_cor=0):
        obj = Spider()
        obj.__dict__ = super().create(x_cor, y_cor).__dict__
        obj.name = "Spider"
        obj.health = 5
        obj.damage = 2
        return obj


class ZombieFactory(EnemyFactory):
    def create(self, x_cor=0, y_cor=0):
        obj = Zombie()
        obj.__dict__ = super().create(x_cor, y_cor).__dict__
        obj.name = "Zombie"
        obj.health = 3
        obj.damage = 2
        return obj


class ArcherFactory(EnemyFactory):
    def create(self, x_cor=0, y_cor=0):
        obj = Archer()
        obj.__dict__ = super().create(x_cor, y_cor).__dict__
        obj.name = "Archer"
        obj.health = 2
        obj.damage = 3
        return obj


class BeeFactory(EnemyFactory):
    def create(self, x_cor=0, y_cor=0):
        obj = Bee()
        obj.__dict__ = super().create(x_cor, y_cor).__dict__
        obj.name = "Bee"
        obj.health = 1
        obj.damage = 1
        return obj


class ScorpionFactory(EnemyFactory):
    def create(self, x_cor=0, y_cor=0):
        obj = Scorpion()
        obj.__dict__ = super().create(x_cor, y_cor).__dict__
        obj.name = "Scorpion"
        obj.health = 4
        obj.damage = 1
        return obj
