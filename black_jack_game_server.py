
import random
import shutil
import os

import blackjack0 as player1
import blackjack1 as player2


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
            num_aces -= 1
        else:
            break
    return value

# Given a hand, returns a human-friendly version, excluding suits
def get_pretty_hand(hand):
    # Sort hand
    hand = sorted(hand,key=lambda x: x[0]) 
    # Make a readable hand, putting aces at the end
    readable_hand = ""
    #aces = ""
    for card in hand:
        if card[0] == 1:
            readable_hand += "[A]"
        elif card[0] == 11:
            readable_hand += "[J]"
        elif card[0] == 12:
            readable_hand += "[Q]"
        elif card[0] == 13:
            readable_hand += "[K]"
        else:
            readable_hand += "["+str(card[0]) + "]" 
    # Return a string of the readable hand 
    return readable_hand# + aces

# Given all hands on table, prints them prettily
def print_table(hands):
    print "##################################################"
    print "#                                                "
    print "#                     " + get_pretty_hand(hands[len(hands)-1]) 
    print "#                                                "
    display = ""
    for h in range(len(hands)-1):
        hand = hands[h]
        display += get_pretty_hand(hand) + "    "
    print "#    " + display
    print "##################################################"
    

def get_user_files():
    print "Getting user files..."
    # Copy blackjack files 
    cwd = os.getcwd()
    users_with_black_jack_file = ['/home/carser/Dropbox/NHS/CS/Cards/player1',
                                  '/home/carser/Dropbox/NHS/CS/Cards/player2']
    for fpath in users_with_black_jack_file:
        # See if file exists
        print "Attempting to get " + fpath + " ..."
        if os.path.isfile(fpath+'/blackjack.py'):
            print '      Adding file ' + fpath
            shutil.copy2(fpath+'/blackjack.py',cwd+'/blackjack'+str(iter)+'.py')

def count_players():
    player_count = 0
    files = os.listdir(os.getcwd())
    for f in files:
        print f
        if 'blackjack' in f[0:9] and f[len(f)-3:len(f)]=='.py' and f[len(f)-4].isdigit():
            player_count += 1
    return player_count

def play_hand():
    num_players = count_players()
    print "Starting game with " + str(num_players) + " players ..." 
    
    # Get 4 decks
    decks = [get_new_deck(), get_new_deck(), get_new_deck(), get_new_deck()]
    deck = []
    for i in range(52):
        for d in decks:
            deck.append(d[i])
    deck = shuffle_deck(deck)
    
    # Deal hands to players and dealer
    hands = []
    deck_index = 0
    for p in range(num_players+1):
        hands.append([deck[deck_index], deck[deck_index+1]])
        deck_index += 2
    print_table(hands)
    
    # Players 
    print player1.hand_value(hands[0])
    player2.identify()
    
    # Dealer play
    while hand_value(hands[len(hands)-1]) < 17:
        print "   dealer hits, " + str(hand_value(hands[len(hands)-1])) + ", " + get_pretty_hand(hands[len(hands)-1])
        hands[len(hands)-1].append(deck[deck_index])
        deck_index += 1
    print_table(hands)
    
    
    
    
    
##########################################        
get_user_files()
play_hand()






















