# -*- coding: utf-8 -*-
"""
@author: carser
"""

import random

# Returns an un-shuffled deck of cards.  Each card is a two-tuple where the
# first entry is the card number, and the second is the suit, for example, the
# Queen of hearts is represented as (12,'h'), and the 5 of spades is 
# represented as (5,'s').
def get_new_deck():
    suits = ["h","c","d","s"]
    num = range(2,11)
    num.extend([11,12,13,1])
    deck = [(i,j) for j in suits for i in num]
    return deck

# Given a deck, shuffles and returns the deck.
def shuffle_deck(deck):
    random.shuffle(deck)
    return deck

# Given a hand, returns the best value of that hand
def hand_value(hand):
    value = 0
    num_aces = 0
    for card in hand:
        if card[0] == 1:
            value += 11
            num_aces += 1
        elif card[0] > 9:
            value += 10
        else:
            value += card[0]
    while num_aces > 0:
        if value > 21:
            value -= 10
        else:
            break
    return value

# Given a hand, prints a human-friendly version, excluding suits
def pretty_print_hand(hand):
    # Sort hand
    hand = sorted(hand,key=lambda x: x[0]) 
    # Make a readable hand, putting aces at the end
    readable_hand = ""
    aces = ""
    for card in hand:
        if card[0] == 1:
            aces += "A "
        elif card[0] == 11:
            readable_hand += "J "
        elif card[0] == 12:
            readable_hand += "Q "
        elif card[0] == 13:
            readable_hand += "K "
        else:
            readable_hand += str(card[0]) + " " 
    # Print the readable hand (no return statement)
    print readable_hand + aces
    
    
def identify():
    print "Player 1"








