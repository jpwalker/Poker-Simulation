'''
Created on Dec 28, 2014

@author: jpwalker
'''

from Decks import Deck, Card

suits = {0:'Spades', 1:'Hearts', 2:'Diamonds', 3:'Clubs'}
ranks = {0:'Ace', 1:'2', 2:'3', 3:'4', 4:'5', 5:'6', 6:'7', 7:'8', 8:'9', 
         9:'10', 10:'Jack', 11:'Queen', 12:'King'}
class StdDeck(Deck):
    def __init__(self):
        for s in suits:
            for r in ranks:
                Card

if __name__ == '__main__':
    pass