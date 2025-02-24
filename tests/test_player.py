import unittest
from unittest.mock import MagicMock
from poker.card import Card
from poker.player import Player
from poker.hand import Hand

class PlayerTest(unittest.TestCase):

    def test_stores_name_and_cards(self):
        hand = Hand(cards= [])
        player = Player(name = "Sid", hand=hand)
        self.assertEqual(player.name, "Sid")
        self.assertEqual(player.hand,hand)

    def test_figure_out_best_hand(self):
        #magicmock can react to any method
        mock_hand = MagicMock()
        mock_hand.best_rank.return_value = "Straight Flush"
        player = Player(name="Boris", hand=mock_hand)

        self.assertEqual(
            player.best_hand(),
            "Straight Flush"
        )
        mock_hand.best_rank.assert_called()
