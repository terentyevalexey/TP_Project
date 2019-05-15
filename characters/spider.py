from characters.characters import Enemies


class Spider(Enemies):
    def update(self):
        """move left or right to meet character or turn"""
        if not (self.rightward and self.leftward):
            if self.rightward:
                self.x_cor += self.move_speed
            if self.leftward:
                self.x_cor -= self.move_speed
        self.attack()

    def attack(self):
        """shoot the player's direction slows enemy"""
