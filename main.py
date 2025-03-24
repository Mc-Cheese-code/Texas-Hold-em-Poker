from poker.card import Card
from poker.deck import Deck
from poker.game_round import GameRound
from poker.hand import Hand
from poker.player import Player

deck = Deck()
cards = Card.create_standard_52_cards()
deck.add_cards(cards)

hand1 = Hand()
hand2 = Hand()
player1 = Player(name='Zed', hand=hand1)
player2 = Player(name='Ted', hand=hand2)
players = [player1, player2]


game_round = GameRound(deck=deck, players = players)
game_round.play()