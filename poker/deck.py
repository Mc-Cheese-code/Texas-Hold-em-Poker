import random
class Deck():
    def __init__(self):
        self.cards = []


    def add_cards(self, card):
        return self.cards.extend(card) 


    def shuffle(self):
        random.shuffle(self.cards)    