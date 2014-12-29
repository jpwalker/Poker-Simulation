'''
Created on Dec 27, 2014

@author: jpwalker
'''

from collections import MutableSequence

class Deck(MutableSequence):
    def __init__(self, seq):
        self.deck = []
        self.deck.extend(seq)
    
    def __getitem__(self, index):
        return self.deck[index]
    
    def __setitem__(self, index, value):
        self.deck[index] = value
    
    def __delitem__(self, index):
        self.deck.pop(index)
    
    def __len__(self):
        return len(self.deck)
    
    def insert(self, index, value):
        self.deck.insert(index, value)

if __name__ == '__main__':
    # Tests for the Deck Class
    deck1 = Deck([0,1,3])
    print(deck1.deck)
    drawn = deck1.pop()
    print(drawn)
    print(deck1.deck)
    deck1.insert(0, drawn)
    print(deck1.deck)