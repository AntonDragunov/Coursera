# * Override vampire's `attack` method. Vampire drains blood, so if he didn't miss,
#   increase his health by 1 point.
#   Hint: use `super` to use original behaviour and don't forget to return result.
#
# * Add extra character class to the game: Ghost. Ghost can't be killed,
#   so override Ghost's `damage` method to do nothing.
import random


class Character:
    health = 10
    strength = 5
    accuracy = 0.5

    def __init__(self, name):
        self.name = name

    def damage(self, value):
        self.health = max(self.health - value, 0)

    def attack(self, character):
        hit = random.random() < self.accuracy
        if hit:
            character.damage(self.strength)
        return hit


class Player(Character):
    pass


class Enemy(Character):
    pass


class Dragon(Enemy):
    pass


class Vampire(Enemy):
    def attack(self, character):
        hit = random.random() < self.accuracy
        super().attack(self)
        if hit:
            character.damage(self.strength)
            self.health = self.health + 1
        else:
            pass
        return hit, self.health


class Ghost(Character):
    def damage(self, value):
        super().damage(value=0)
        self.health = max(self.health, 0)

    #
