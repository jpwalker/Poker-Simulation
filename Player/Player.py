'''
Created on Mar 14, 2016

@author: jpwalker
'''
from numpy.oldnumeric.random_array import beta

class MyClass(object):
    '''
    classdocs
    '''
    
    def __init__(self, mny = 80):
        '''
        Constructor
        '''
        self.money = mny
        self.bet = 0
        self.match_comp = 0
    
    def change_bet(self, bet):
        self.bet = bet
    
    def place_bet(self):
        if self.money - self.bet > 0:
            self.money -= self.bet
            return 0
        else:
            return 1