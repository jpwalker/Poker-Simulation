'''
Created on Mar 14, 2016

@author: jpwalker
'''

from StdDeck import StdDeck, StdCard

def check_count(deck, cards, rmv = True):
    count = 52 
    color_count = {'red':26, 'black':26}
    suite_count = {'Spade':13, 'Club':13, 'Heart':13, 'Diamond':13}
    rank_count = {'Ace':4, '2':4, '3':4, '4':4, '5':4, '6':4, '7':4, 
                  '8':4, '9':4, '10':4, 'Jack':4, 'Queen':4, 'King':4}
    if rmv:
        for c in cards:
            count -= 1
            color_count[c.color] -= 1
            suite_count[c.suite] -= 1
            rank_count[c.rank] -= 1
    test1 = count == deck.count
    test2 = color_count == deck.color_count
    test3 = suite_count == deck.suite_count
    test4 = rank_count == deck.rank_count
    print 'The counts are {0}.'.format(test1 and test2 and test3 and test4)

def init():
    print('Creating deck...')
    deck = StdDeck()
    print('Printing StdDeck...')
    for i in deck.deck:
        print i
    return deck

def test1(deck):
    print('Drawing 5 cards...')
    cards = deck.draw(5)
    p_cards = [str(c) for c in cards]
    print('Cards drawn: {0}'.format('\t'.join(p_cards)))
    print('Checking counts after drawing...')
    check_count(deck, cards)
    return cards
    
def test2(deck, cards):
    print('Reinserting 5 drawn cards...')
    deck.insert(cards)
    print('Checking counts after reinserting...')
    check_count(deck, cards, False)
    
def error_test(deck):
    print('Drawing 54 cards and checking error...')
    try:
        deck.draw(54)
    except RuntimeError as err:
        print 'Error detected: {0}'.format(err)
    print('Creating mis-colored StdCard and checking error...')
    try:
        StdCard('Heart', 'Ace', 'Black')
    except RuntimeError as err:
        print 'Error detected: {0}'.format(err)

if __name__ == '__main__':
    pass