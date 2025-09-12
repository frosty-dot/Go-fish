# TODO: Create a player file that has a class. 
class player:
    def __init__(self, name):
        self.name = name      # Allows name customization/setup
        self.hand = []        # Empty hand property
        self.score = 0        # Score property

    def shuffle(self):
        for index in range(len(self.deck_of_cards) - 1):
            num = random.randint(index + 1, len(self.deck_of_cards) - 1)
            temp = self.deck_of_cards[index]
            # print("Index: {} Num: {}".format(index, num))
            self.deck_of_cards[index] = self.deck_of_cards[num]
            self.deck_of_cards[num] = temp

def display_hand(self):
    for card in self.hand:
        card.print_card() 


    def check_my_hand(self, asking_rank):
        for card in self.hand:
            pass



            
        
    
# The class should allow name customization/set up, 
# should create an empty hand property, 
# and should have a score property. 
# Also, create a method/function that displays the hand

