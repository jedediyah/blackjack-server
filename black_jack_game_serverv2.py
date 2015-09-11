import random
import os
import shutil

class Card(object):
 
        #types of cards
        suits = ["Clubs", "Diamonds", "Hearts", "Spades"]
        ranks = ["joker", "Ace", "2", "3", "4", "5", "6","7", "8", "9", "10", "Jack", "Queen", "King"]

        #Initializes card class
        def __init__(self, suit, rank):
            self.suit = suit
            self.rank = rank
        #function to print the cards in a pretty format
        def printCard(self):
            print str(self.ranks[self.rank]) + " of " + str(self.suits[self.suit])
            
            
            
            
class Deck(object):
    
    #initializes deck class, n is number of cards in the deck
    def __init__(self):
        self.cards = []
        
    def deck(self):
        for suit in range(0,4):
            for rank in range (1,14):
                self.cards.append(Card(suit, rank))
                
                
    def printDeck(self):
        for i in range(0, len(self.cards)):
            print self.cards[i].printCard()
            
    def shuffleDeck(self):
        random.shuffle(self.cards)
        
        
def handValue(hand):
    value = 0
    num_aces = 0
    for card in hand:
        if card.rank == 1:
            value += 11
            num_aces += 1
        elif card.rank > 9:
            value += 10
        else:
            value += card.rank
    while num_aces > 0:
        if value > 21:
            value -= 10
            num_aces -= 1
        else:
            break
    return value
    
def countPlayers():
    player_count = 0
    files = os.listdir(os.getcwd())
    for f in files:
        print f
        if 'blackjack' in f[0:9] and f[len(f)-3:len(f)]=='.py' and f[len(f)-4].isdigit():
            player_count += 1
    return player_count
    
            
def getPlayerFiles():
    print "Getting player files..."
    cwd = os.cwd()
    playersWithFile = []
    
    #Iterates over user directories
    for userDir in os.listdir('/home'):
        fpath = '/home/' + str(userDir) + '/python/blackjack/blackjack.py'
        #Check to see if the blackjack.py file exits in the theoretical directory
        if os.path.isfile(fpath):
            playersWithFile.append(str(userDir))
            print "Adding file from: " + fpath
            shutil.copy2(fpath, cwd + '/blackjack' +str(iter) + '.py')
        else:
            print "File does not exist in " + fpath
            
    print str(len(playersWithFile)) + " player files were added"
    
def play_hand():
    players = countPlayers()
    print "Starting with " + str(players) + " players"
    
    #Creates the main deck of 8 decks
    deck = [Deck(), Deck(), Deck(), Deck(), Deck(), Deck(), Deck(), Deck(),]
    for subDeck in deck:
        subDeck.deck()
        subDeck.shuffleDeck()
        
    #Creates player and dealer hands
    
    
        
    
#test = Card(2,7) 
#test.printCard()
#test2 = Deck()
#test2.deck()
#test2.shuffleDeck()
#print test2.cards[0].rank
