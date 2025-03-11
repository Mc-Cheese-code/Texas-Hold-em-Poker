import random
class Deck():
    def __init__(self):
        self.cards = []


    def add_cards(self, card):
        return self.cards.extend(card)

    def remove_cards(self, number):
        cards_to_remove = self.cards[:number]
        del self.cards[:number]
        return cards_to_remove 


    def shuffle(self):
        random.shuffle(self.cards)    