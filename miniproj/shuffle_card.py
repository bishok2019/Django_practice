import random
class Cards:
    def __init__(self):
        self.suites=['Hearts', 'Diamonds', 'Spades', 'Clubs']
        self.values=['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']
        self.deck = [(suite, value) for suite in self.suites for value in self.values]

    def shuffle_deck(self):
        random.shuffle(self.deck)
    
    def draw_card(self):
        if self.deck:
            return self.deck.pop()
        else:
            return "No cards left in the deck"
    
cards = Cards()
cards.shuffle_deck()
print(cards.draw_card())
print(len(cards.deck))

# mylist = ['apple', 'banana', 'cherry']
# mylist.insert(0, 'orange')
# print(mylist[1])
# print(mylist)
# print(mylist[1])

# fruits = ['apple', 'banana', 'cherry']
# # newlist = ['apple' for x in fruits]
# # print(newlist)
# b= fruits[::-1]
# print(b)
# # print(newlist)