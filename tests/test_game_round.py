import unittest
from unittest.mock import MagicMock, call
from poker.game_round import GameRound
from poker.card import Card

class GameRoundTest(unittest.TestCase):

    def test_stores_deck_and_players(self):
        deck = MagicMock()

        players = [
            MagicMock(),
            MagicMock()
        ]
        game_round = GameRound(
            deck = deck,
            players = players
        )

        self.assertEqual(
            game_round.deck,
            deck
        )

        self.assertEqual(
            game_round.players,
            players
        )


    def test_game_play_shuffles_deck(self):
        mock_deck = MagicMock()

        players = [
            MagicMock(),
            MagicMock()
        ]
        game_round = GameRound(
            deck = mock_deck,
            players = players
        )

        game_round.play()

        mock_deck.shuffle.assert_called_once()


    def test_deals_with_two_initial_cards_from_deck_to_each_player(self):

        first_two_cards = [
            Card(rank="2", suit="Hearts"),
            Card(rank="6", suit="Clubs")
        ]

        next_two_cards = [
            Card(rank="9", suit='Diamonds'),
            Card(rank="4", suit="Spades")
        ]
        mock_deck = MagicMock()
        mock_deck.remove_cards.side_effect = [first_two_cards, next_two_cards]

        mock_player1 = MagicMock()
        mock_player2 = MagicMock()
        players = [mock_player1, mock_player2]

        game_round = GameRound(
            deck = mock_deck,
            players = players
        )

        game_round.play()

        mock_deck.remove_cards.assert_has_calls([
            call(2), call(2)
        ])

        mock_player1.add_cards.assert_called_with(first_two_cards)
        mock_player2.add_cards.assert_called_with(next_two_cards)
    
    def test_removes_player_if_not_willing_to_bet(self):
        deck = MagicMock()

        player1 = MagicMock()
        player2 = MagicMock()

        player1.wants_to_fold.return_value = True
        player2.wants_to_fold.return_value = False
        players = [player1, player2]
        game_round = GameRound(deck=deck, players=players)
        game_round.play()

        self.assertEqual(
            game_round.players,
            [player2]
        )

    def test_deals_same_three_community_cards_to_all_players_in_flop(self):
        mock_player1 = MagicMock()
        mock_player1.wants_to_fold.return_value = False

        mock_player2 = MagicMock()
        mock_player2.wants_to_fold.return_value = False


        community_cards = [
            
        ]
        mock_deck = MagicMock()
        mock_deck.remove_cards.side_effect = [
            [],
            [],
            community_cards
        ]





