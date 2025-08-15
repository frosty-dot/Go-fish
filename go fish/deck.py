# imported the class from the code file it is in
from card import Card
import random

# TODO: Create a suits list that stores all 4 as strings
suits = ['Hearts', 'Clubs', 'Spades', 'Diamonds']

# TODO: Create a class for the deck of cards
# Create constructor with no new properties
# Inside of the constructor:
    # Create an empty list
class Deck():
    def __init__(self):
        self.deck_of_cards = []
        for suit in suits:
            for rank in range(1, 14):
                card = Card(rank. suit)

                # Create a card object (set the rank and the suit)
    def shuffle(self):
        for index in range(len(self.deck_of_cards) - 1):
            num = random.randint(index + 1, len(self.deck_of_cards) - 1)
            temp = self.deck_of_cards[index]
            # print("Index: {} Num: {}".format(index, num))
            self.deck_of_cards[index] = self.deck_of_cards[num]
            self.deck_of_cards[num] = temp

    def deal_card(self, player, player_name):
    # Check if there are cards in the deck
        if len(self.deck_of_cards) > 0:
            random_card = random.choice(self.deck_of_cards)
            player.hand.append(random_card)
            self.deck_of_cards.remove(random_card)
        else:
            print("empty deck!")
    
        


    # TODO: Create a method/function that displays the entire deck of cards
    def display_deck(self):
        for card in self.deck_of_cards:
            card.print_card()



