'''
Created on Dec 28, 2014

@author: jpwalker
'''

from random import seed, sample
from os import getpid, times
from __builtin__ import isinstance

suits = set(('Spade', 'Heart', 'Diamond', 'Club'))
ranks = set(('Ace', '2', '3', '4', '5', '6', '7', '8', '9', 
            '10', 'Jack', 'Queen', 'King'))
colors = set(('black', 'red'))
color_suit_map = {'Spade':'black', 'Heart':'red', 
                  'Diamond':'red', 'Club':'black'}

class StdDeck():
    def __init__(self, std=True):
        self.deck = []
        if std:
            self.count = 52 
            self.color_count = {'red':26, 'black':26}
            self.suite_count = {'Spade':13, 
                      'Club':13, 'Heart':13, 'Diamond':13}
            self.rank_count = {'Ace':4, '2':4, '3':4, '4':4, '5':4, 
                               '6':4, '7':4, '8':4, '9':4, '10':4, 
                               'Jack':4, 'Queen':4, 'King':4}
            for s in suits:
                for r in ranks:
                    self.deck.append(StdCard(s, r, color_suit_map[s]))
        else:
            self.count = 0 
            self.color_count = {'red':0, 'black':0}
            self.suite_count = {'Spade':0, 
                      'Club':0, 'Heart':0, 'Diamond':0}
            self.rank_count = {'Ace':0, '2':0, '3':0, '0':0, '5':0, 
                               '6':0, '7':0, '8':0, '9':0, '10':0, 
                               'Jack':0, 'Queen':0, 'King':0}
            
    def insert(self, cards):
        if isinstance(cards, StdCard):
            self.deck.append(cards)
            self.count += 1
            self.color_count[color_suit_map[cards.suite]] +=1
            self.suite_count[cards.suite] += 1
            self.rank_count[cards.rank] += 1
        else:
            # Assume cards is iterable
            for crd in cards:
                self.insert(crd)
            
    def remove(self, cards):
        if isinstance(cards, StdCard):
            idx = self.deck.index(cards)
            del self.deck[idx]
            self.count -= 1
            self.color_count[color_suit_map[cards.suite]] -=1
            self.suite_count[cards.suite] -= 1
            self.rank_count[cards.rank] -= 1
        else:
            for crd in cards:
                self.remove(crd)
    
    def draw(self, num=1, deck=True):
        # Seed random number generator
        sd = hash(getpid()) + hash(times()[4])
        seed(sd)
        if num <= self.count:
            result = sample(self.deck, num)
            self.remove(result)
            return result
        else:
            err = 'Requesting to draw {0} out of {1}'.format(num, self.count)
            raise RuntimeError(err)

class StdCard():
    def __init__(self, suite, rank, color):
        if suite in suits and rank in ranks and \
        color in colors and color == color_suit_map[suite]:
            self.suite = suite
            self.rank = rank
            self.color = color
        else:
            err = 'Suite {0} does not match given color {1}.'.format(suite, color)
            raise RuntimeError(err)
        
    def __str__(self):
        return '{0}:{1} {2}'.format(self.color, self.rank, self.suite)

if __name__ == '__main__':
    from _test import init, test1, test2, error_test
    deck = init()
    cards = test1(deck)
    test2(deck, cards)
    error_test(deck)