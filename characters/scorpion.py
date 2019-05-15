from characters.characters import Enemies


class Scorpion(Enemies):
    def update(self):
        """moves to the character"""
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
        self.attack()

    def attack(self):
        """DOT debuffing enemy"""
