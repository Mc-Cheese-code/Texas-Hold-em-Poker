import unittest
from poker.card import Card
from poker.player import Player

class PlayerTest(unittest.TestCase):

    def test_stores_name_and_cards(self):
        player = Player(name = "Sid")
        self.assertEqual(player.name, "Sid")
        self.assertEqual(player.cards, [])