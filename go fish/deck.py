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
                # Add the object to the empty deck_of_cards list

    # TODO: Create a method/function that displays the entire deck of cards

# TESTING: Create a deck of cards object and print them to the console