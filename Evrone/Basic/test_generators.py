##
# Tests for main.py
#
# All tests in the folder "test" are executed
# when the "Test" action is invoked.
#
##

import inspect
import unittest

import main


class mainTestCase(unittest.TestCase):
    def test_generate_names(self):
        names = main.generate_names("player", 5)
        self.assertEqual(names, ["player_0", "player_1", "player_2", "player_3", "player_4"])

    def test_generate_vampires(self):
        vampires = main.generate_vampires(2)
        self.assertTrue(inspect.isgenerator(vampires))
        vampires = list(vampires)
        self.assertEqual(len(vampires), 2)
        self.assertEqual(vampires[1].name, 'vampire_1')

    def test_generate_dragons(self):
        dragons = main.generate_dragons(3)
        self.assertTrue(inspect.isgenerator(dragons))
        dragons = list(dragons)
        self.assertEqual(len(dragons), 3)
        self.assertEqual(dragons[2].name, 'dragon_2')

    def test_generate_enemies(self):
        enemies = main.generate_enemies(vampires_count=2, dragons_count=1)
        self.assertEqual(len(enemies), 3)
        self.assertTrue(isinstance(enemies['vampire_1'], main.Vampire))
        self.assertTrue(isinstance(enemies['dragon_0'], main.Dragon))
