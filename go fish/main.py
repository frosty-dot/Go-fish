from deck import Deck
from player import player 
class GoFishGame:
    def __init__(self):
        self.deck = Deck()       
        self.players = []        
        self.is_playing = True

    def game_setup(self):
        self.deck.shuffle()
        num_players = int(input("How many players? "))
        for i in range(num_players):
            name = input(f"Enter name for player {i+1}: ")
            self.players.append(player(name))
# TODO CHALLENGE 1: Create a new main/game python file and then create a go fish/game class
# The constructor of the class should include
    # a deck of cards object
    # a list to store players
    # a property that tracks if the game is still being played
# HINT: Don’t forget to import any necessary files/classes at the top!










