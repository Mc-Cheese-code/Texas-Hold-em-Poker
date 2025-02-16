import unittest
from poker.card import Card
from poker.deck import Deck
from poker.hand import Hand

class HandTest(unittest.TestCase):

    def test_recieves_and_stores(self):
        cards = [
            Card(rank="5",suit="Diamonds"),
            Card(rank="6",suit="Clubs")
        ]

        hand = Hand(cards = cards)
        self.assertEqual(hand.cards, cards)

    def test_figures_out_high_card_is_the_best(self):
        cards = [
            Card(rank="Ace",suit="Diamonds"),
            Card(rank="6",suit="Clubs")
        ]
        # every combo is a high card
        hand = Hand(cards = cards)
        self.assertEqual(
            hand.best_rank(),
            "High Card"
        )

    def test_figures_out_pair_is_best_rank(self):
        cards = [
            Card(rank='Ace', suit='Spades'),
            Card(rank='Ace', suit='Clubs')
        ]

        hand = Hand(cards=cards)
        self.assertEqual(
            hand.best_rank(),
            "Pair"
        )

