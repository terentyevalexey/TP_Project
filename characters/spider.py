from characters.characters import Enemies


class Spider(Enemies):
    def update(self):
        """move left or right to meet character or turn"""
        diag_diff = round(self.move_speed - ((self.move_speed ** 2) / 2) ** .5)
        if not (self.rightward and self.leftward):
            if self.rightward:
                self.x_cor += self.move_speed
                if self.upward or self.downward:
                    self.x_cor -= diag_diff
            if self.leftward:
                self.x_cor -= self.move_speed
                if self.upward or self.downward:
                    self.x_cor += diag_diff
        self.attack()

    def attack(self):
        """shoot the player's direction slows enemy"""
