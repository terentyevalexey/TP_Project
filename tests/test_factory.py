import unittest
from factory import *


class TestFactory(unittest.TestCase):
    def test_spider(self):
        spider = SpiderFactory().create()
        self.assertEqual(spider.race, "Enemy")
        self.assertEqual(spider.name, "Spider")
        self.assertEqual(spider.health, 5)
        self.assertEqual(spider.damage, 2)
        self.assertEqual(spider.move.__doc__,
                         "move left or right to meet character or turn")
        self.assertEqual(spider.attack.__doc__,
                         "shoot the player's direction slows enemy")

    def test_archer(self):
        archer = ArcherFactory().create()
        self.assertEqual(archer.race, "Enemy")
        self.assertEqual(archer.name, "Archer")
        self.assertEqual(archer.health, 2)
        self.assertEqual(archer.damage, 3)
        self.assertEqual(archer.move.__doc__, "no move")
        self.assertEqual(archer.attack.__doc__, "attack ranged")

    def test_bee(self):
        bee = BeeFactory().create()
        self.assertEqual(bee.race, "Enemy")
        self.assertEqual(bee.name, "Bee")
        self.assertEqual(bee.health, 1)
        self.assertEqual(bee.damage, 1)
        self.assertEqual(bee.move.__doc__,
                         "randomly until sees a wall or decides to turn")
        self.assertEqual(bee.attack.__doc__,
                         "attack when in close range near the character")

    def test_scorpion(self):
        scorpion = ScorpionFactory().create()
        self.assertEqual(scorpion.race, "Enemy")
        self.assertEqual(scorpion.name, "Scorpion")
        self.assertEqual(scorpion.health, 4)
        self.assertEqual(scorpion.damage, 1)
        self.assertEqual(scorpion.move.__doc__, "moves to the character")
        self.assertEqual(scorpion.attack.__doc__, "DOT debuffing enemy")

    def test_zombie(self):
        zombie = ZombieFactory().create()
        self.assertEqual(zombie.race, "Enemy")
        self.assertEqual(zombie.name, "Zombie")
        self.assertEqual(zombie.health, 3)
        self.assertEqual(zombie.damage, 2)
        self.assertEqual(zombie.move.__doc__, "go to character")
        self.assertEqual(zombie.attack.__doc__, "attack melee")

