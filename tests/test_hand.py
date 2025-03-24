import unittest
from poker.card import Card
from poker.deck import Deck
from poker.hand import Hand

class HandTest(unittest.TestCase):


    def test_starts_out_with_no_cards(self):
        hand = Hand()
        self.assertEqual(hand.cards, [])

    def test_shows_all_its_card_in_technical_representation(self):
        cards = [
            Card(rank="Ace",suit="Diamonds"),
            Card(rank="6",suit="Clubs")
        ]

        hand = Hand()
        hand.add_cards(cards)
        self.assertEqual(
            repr(hand),
            "6 of Clubs, Ace of Diamonds"
        )   

    def test_recieves_and_stores(self):
        ace_of_spades = Card(rank="5",suit="Diamonds")
        six_of_cards = Card(rank="6",suit="Clubs")
        cards = [
            ace_of_spades,
            six_of_cards
        ]

        hand = Hand()
        hand.add_cards(cards)

        self.assertEqual(hand.cards,
                         [
                            ace_of_spades,
                            six_of_cards
                         ])

    def test_figures_out_no_card_is_the_best(self):
        hand = Hand()
        self.assertEqual(
            hand.best_rank(),
            "No Cards"
        )
    


    def test_figures_out_high_card_is_the_best(self):
        cards = [
            Card(rank="Ace",suit="Diamonds"),
            Card(rank="6",suit="Clubs")
        ]
        # every combo is a high card
        hand = Hand()
        hand.add_cards(cards=cards)
        self.assertEqual(
            hand.best_rank(),
            "High Card"
        )

    def test_figures_out_pair_is_best_rank(self):
        cards = [
            Card(rank='Ace', suit='Spades'),
            Card(rank='Ace', suit='Clubs')
        ]

        hand = Hand()
        hand.add_cards(cards=cards)
        self.assertEqual(
            hand.best_rank(),
            "Pair"
        )

    def test_figure_out_two_pair_is_best_rank(self):
        cards = [
            Card(rank='Ace', suit='Spades'),
            Card(rank='5', suit='Clubs'),
            Card(rank='Ace', suit='Clubs'),
            Card(rank='King', suit='Hearts'),
            Card(rank="King", suit='Diamonds')
        ]

        hand = Hand()
        hand.add_cards(cards=cards)
        self.assertEqual(
            hand.best_rank(),
            "Two Pair"
        )

    def test_figure_out_three_of_a_kind_is_best_rank(self):
        cards = [
            Card(rank="King", suit='Clubs'),
            Card(rank="King", suit='Hearts'),
            Card(rank="King", suit='Diamonds'),
            Card(rank="Ace", suit='Spades'),
            Card(rank="5", suit='Diamonds')
        ]

        hand = Hand()
        hand.add_cards(cards=cards)

        self.assertEqual(
            hand.best_rank(),
            "Three of a Kind"
        )

    def  test_figure_out_straight_is_best_rank(self):
        cards = [
            Card(rank="6", suit='Clubs'),
            Card(rank="7", suit='Hearts'),
            Card(rank="8", suit='Diamonds'),
            Card(rank="9", suit='Spades'),
            Card(rank="10", suit='Diamonds')
        ]

        hand = Hand()
        hand.add_cards(cards=cards)
        self.assertEqual(
            hand.best_rank(),
            "Straight"
        )

    def test_does_not_deem_two_consectuive_cards_as_staright(self):
        cards = [
            Card(rank='6', suit='Hearts'),
            Card(rank='7', suit='Diamonds')
        ]

        hand = Hand()
        hand.add_cards(cards=cards)

        self.assertEqual(
            hand.best_rank(),
            "High Card"
        )

    def test_figure_out_flush_best_rank(self):
        cards = [
            Card(rank=rank, suit="Hearts")
            for rank in ["2","3","4","8","Ace"]
        ]

        hand = Hand()
        hand.add_cards(cards=cards)
        self.assertEqual(
            hand.best_rank(),
            "Flush"
        )

    def test_figure_out_full_house_is_best_rank(self):
        cards = [
            Card(rank="3", suit="Spades"),
            Card(rank="3", suit="Hearts"),
            Card(rank="3", suit="Spades"),
            Card(rank="9", suit="Diamonds"),
            Card(rank="9", suit="Spades"),
            
        ]

        hand = Hand()
        hand.add_cards(cards=cards)
        self.assertEqual(
            hand.best_rank(),
            "Full House"
        )

    def test_figure_out_four_of_a_kind_is_best_rank(self):
        cards = [
            Card(rank="3", suit="Spades"),
            Card(rank="3", suit="Hearts"),
            Card(rank="3", suit="Spades"),
            Card(rank="3", suit="Diamonds"),
            Card(rank="9", suit="Spades"),
            
        ]

        hand = Hand()
        hand.add_cards(cards=cards)
        self.assertEqual(
            hand.best_rank(),
            "Four of a Kind"
        )

    def test_figure_out_straight_flush_is_best_rank(self):
        cards = [
            Card(rank="3", suit="Spades"),
            Card(rank="4", suit="Spades"),
            Card(rank="5", suit="Spades"),
            Card(rank="6", suit="Spades"),
            Card(rank="7", suit="Spades"),
            
        ]

        hand = Hand()
        hand.add_cards(cards=cards)
        self.assertEqual(
            hand.best_rank(),
            "Straight Flush"
        )

    
    def test_figure_out_royal_flush_is_best_rank(self):
        cards = [
            Card(rank="10", suit="Spades"),
            Card(rank="Jack", suit="Spades"),
            Card(rank="Queen", suit="Spades"),
            Card(rank="King", suit="Spades"),
            Card(rank="Ace", suit="Spades"),
            
        ]

        hand = Hand()
        hand.add_cards(cards=cards)
        self.assertEqual(
            hand.best_rank(),
            "Royal Flush"
        )

                       
