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
            New_player = player(name)
            self.players.append(New_player)
            if num_players < 5:
                for deck in range(7):
                    
            
            
            
        # cards_to_deal = 7 if num_players < 5 else 5
        # for p in self.players:
        #     p.hand = self.deck.deal(cards_to_deal)
# TODO CHALLENGE 1: Create a new main/game python file and then create a go fish/game class
# The constructor of the class should include
    # a deck of cards object
    # a list to store players
    # a property that tracks if the game is still being played
# HINT: Don’t forget to import any necessary files/classes at the top!
# TODO CHALLENGE 2: Inside of the class, create a game setup method
# The method should allow you to customize the number of players!

# Inside of the method:
# 0- Create a deck of cards object for dealing
# 1- We want to create the number of players as player objects and add them to the list of players
# HINT: What do we create to do more than one thing at a time?
# HINT: Don't forget that each player will need an assigned name! 

# 2- We also want to track each player in the list
# HINT: What do we create for tracking information? How do we access items in a list?

# 3- If there are less than 5 players selected, deal each player 7 cards from the deck
# 4- Otherwise, deal each player 5 cards from the deck
# HINT: How do we deal cards from the deck? How would we say which player









