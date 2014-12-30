'''
Created on Dec 27, 2014

@author: jpwalker
'''

from collections import MutableSequence
import random as rand

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
    
    def __repr__(self):
        return '{0}({1})'.format(self.__class__.__name__, self.deck)

    
    def shuffle(self, seed = None):
        if seed != None:
            rand.seed(seed)
        rand.shuffle(self.deck)
        
if __name__ == '__main__':
    # Tests for the Deck Class
    deck1 = Deck([0,1,3])
    print(deck1)
    drawn = deck1.pop()
    print(drawn)
    print(deck1)
    deck1.insert(0, drawn)
    print(deck1)
    deck1.extend([4,5,6])
    print(deck1)