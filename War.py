#  File: War.py
#  Description: Creates a deck of cards, shuffles it, and plays a full game of war
#  Student's Name: Hailey Cassidy
#  Student's UT EID: HAC787
#  Course Name: CS 313E 
#  Unique Number: 51465
#
#  Date Created: 9/25/17
#  Date Last Modified: 9/26/17

import random

class Card():
    def __init__ (self,rank,suit):
        self.suit = suit
        self.rank = rank

    def __str__ (self):
        if int(self.rank) == 11:
            displayRank = "J"
        elif int(self.rank) == 12:
            displayRank = "Q"
        elif int(self.rank) == 13:
            displayRank = "K"
        elif int(self.rank) == 14:
            displayRank = "A"
        else:
            displayRank = self.rank
        return displayRank + self.suit

class Deck():
    def __init__ (self):
        self.cardList = [Card("2","C"),Card("3","C"),Card("4","C"),Card("5","C"),Card("6","C"),Card("7","C"),Card("8","C"),Card("9","C"),Card("10","C"),Card("11","C"),Card("12","C"),Card("13","C"),Card("14","C"),\
                     Card("2","D"),Card("3","D"),Card("4","D"),Card("5","D"),Card("6","D"),Card("7","D"),Card("8","D"),Card("9","D"),Card("10","D"),Card("11","D"),Card("12","D"),Card("13","D"),Card("14","D"),\
                     Card("2","H"),Card("3","H"),Card("4","H"),Card("5","H"),Card("6","H"),Card("7","H"),Card("8","H"),Card("9","H"),Card("10","H"),Card("11","H"),Card("12","H"),Card("13","H"),Card("14","H"),\
                     Card("2","S"),Card("3","S"),Card("4","S"),Card("5","S"),Card("6","S"),Card("7","S"),Card("8","S"),Card("9","S"),Card("10","S"),Card("11","S"),Card("12","S"),Card("13","S"),Card("14","S")]


    def __str__ (self):
        x = 0
        display = " "
        while x <= 12:
            display += str(self.cardList[x]) + " "
            x += 1
        display += "\n" + " "
        while x <= 25:
            display += str(self.cardList[x]) + " "
            x += 1
        display += "\n" + " "
        while x <= 38:
            display += str(self.cardList[x]) + " "
            x += 1
        display += "\n" + " "
        while x <= 51:
            display += str(self.cardList[x]) + " "
            x += 1
        display += "\n"
        return display
            
    def shuffle(self):
        random.shuffle(self.cardList)

    def dealOne(self, player):
        dealtCard = self.cardList[0]
        self.cardList.remove(dealtCard)
        player.hand.append(dealtCard)
        player.handTotal += 1
        

class Player(): 
    def __init__ (self):
        self.hand = []
        self.handTotal = 0

    def __str__ (self):
        x = 0
        display = " "
        try: 
            while x <= 12:
                display += str(self.hand[x]) + " "
                x += 1
            display += "\n" + " "
            while x <= 25:
                display += str(self.hand[x]) + " "
                x += 1
            display += "\n" + " "
            while x <= 38:
                display += str(self.hand[x]) + " "
                x += 1
            display += "\n" + " "
            while x <= 51:
                display += str(self.hand[x]) + " "
                x += 1
            display += "\n"
        except IndexError: #if the player has less than 52 cards this makes it so there is no index error
            pass
        return display

    def handNotEmpty(self):
        if self.handTotal > 0:
            return True
        else:
            return False

def playGame(deck, player1, player2):
    
    # display of initial hands before game starts
    print("Initial Hands:")
    print("Player 1:")
    print(player1)
    print("Player 2:")
    print(player2)

    # intial conditions for game 
    gameRound = 1
    gameOver = False

    #loops for each round until one player has no cards in their hand
    while gameOver == False:
        
        #displays round and cards played
        print("\n\nRound", gameRound)
        print("Player 1 plays:", player1.hand[0])
        print("Player 2 plays:", player2.hand[0])
        
        #if player one wins the round
        if int(player1.hand[0].rank) > int(player2.hand[0].rank):
            print("Player 1 wins round", gameRound, ":", str(player1.hand[0]), ">", str(player2.hand[0]))

            #putting cards into back of player one's hand
            player1Card = player1.hand[0]
            player1.hand.remove(player1Card)
            player1.hand.append(player1Card)

            player2Card = player2.hand[0]
            player2.hand.remove(player2Card)
            player1.hand.append(player2Card)

            #adjust number of cards in hand 
            player1.handTotal += 1
            player2.handTotal -= 1

        #if player two wins the round           
        elif int(player2.hand[0].rank) > int(player1.hand[0].rank):
            print("Player 2 wins round", gameRound, str(player2.hand[0]), ">", str(player1.hand[0]))

            #putting cards into back of player two's hand
            player1Card = player1.hand[0]
            player1.hand.remove(player1Card)
            player2.hand.append(player1Card)

            player2Card = player2.hand[0]
            player2.hand.remove(player2Card)
            player2.hand.append(player2Card)

            #adjusting number of cards in hand 
            player1.handTotal -= 1
            player2.handTotal += 1
            
        #if it is a tie
        elif int(player2.hand[0].rank) == int(player1.hand[0].rank):

            # loop until it is no longer a tie 
            tie = True
            while tie == True: 
                print("War starts:", str(player2.hand[0]), "=", str(player1.hand[0]))

                #playing and displaying all the cards during war 
                player1CardOriginal = player1.hand[0]
                player1.hand.remove(player1CardOriginal)

                player2CardOriginal = player2.hand[0]
                player2.hand.remove(player2CardOriginal)

                player1Card1 = player1.hand[0]
                player1.hand.remove(player1Card1)
                player1Card2 = player1.hand[0]
                player1.hand.remove(player1Card2)
                player1Card3 = player1.hand[0]
                player1.hand.remove(player1Card3)
                player1Card4 = player1.hand[0]

                player2Card1 = player2.hand[0]
                player2.hand.remove(player2Card1)
                player2Card2 = player2.hand[0]
                player2.hand.remove(player2Card2)
                player2Card3 = player2.hand[0]
                player2.hand.remove(player2Card3)
                player2Card4 = player2.hand[0]

                print("Player 1 put", player1Card1, "face down")
                print("Player 2 put", player2Card1, "face down")
                print("Player 1 put", player1Card2, "face down")
                print("Player 2 put", player2Card2, "face down")
                print("Player 1 put", player1Card3, "face down")
                print("Player 2 put", player2Card3, "face down")
                print("Player 1 put", player1Card4, "face up")
                print("Player 2 put", player2Card4, "face up")

                #if player one wins the war
                if int(player1.hand[0].rank) > int(player2.hand[0].rank):
                    print("Player 1 wins round", gameRound, str(player1.hand[0]), ">", str(player2.hand[0]))

                    #adding cards to the back of player one's hand
                    player1.hand.remove(player1Card4)
                    player1.hand.append(player1CardOriginal)
                    player1.hand.append(player1Card1)
                    player1.hand.append(player1Card2)
                    player1.hand.append(player1Card3)
                    player1.hand.append(player1Card4)
                    
                    player2.hand.remove(player2Card4)
                    player1.hand.append(player2CardOriginal)
                    player1.hand.append(player2Card1)
                    player1.hand.append(player2Card2)
                    player1.hand.append(player2Card3)
                    player1.hand.append(player2Card4)

                    #adjusting hand totals
                    player1.handTotal += 5
                    player2.handTotal -= 5

                    tie = False # no longer a tie

                #if player two wins the war
                elif int(player2.hand[0].rank) > int(player1.hand[0].rank):
                    print("Player 2 wins round", gameRound, str(player2.hand[0]), ">", str(player1.hand[0]))

                    #adding cards to the back of player two's hand
                    player1.hand.remove(player1Card4)
                    player2.hand.append(player1CardOriginal)
                    player2.hand.append(player1Card1)
                    player2.hand.append(player1Card2)
                    player2.hand.append(player1Card3)
                    player2.hand.append(player1Card4)

                    player2.hand.remove(player2Card4)
                    player2.hand.append(player2CardOriginal)
                    player2.hand.append(player2Card1)
                    player2.hand.append(player2Card2)
                    player2.hand.append(player2Card3)
                    player2.hand.append(player2Card4)

                    #adjusting hand totals 
                    player1.handTotal -= 5
                    player2.handTotal += 5

                    tie = False #no longer a tie
                    
        #checking to see if the game is over                   
        if player2.handTotal == 0 or player1.handTotal == 0:
            gameOver = True

        #next round 
        gameRound += 1

        #displaying cards in each players hand at the end of each round
        print("\nPlayer 1 now has", player1.handTotal, "card(s) in hand:")
        print(player1)
        print("\nPlayer 2 now has", player2.handTotal, "card(s) in hand:")
        print(player2) 
            
            

def main():

    cardDeck = Deck()               # create a deck of 52 cards called "cardDeck"
    print("Initial deck:")
    print(cardDeck)                 # print the deck so we can see that you built it correctly
    
    random.seed(15)                 # leave this in for grading purposes
    cardDeck.shuffle()              # shuffle the deck
    print("Shuffled deck:")
    print(cardDeck)                 # print the deck so we can see that your shuffle worked
    
    player1 = Player()              # create a player
    player2 = Player()              # create another player

    for i in range(26):             # deal 26 cards to each player, one at 
       cardDeck.dealOne(player1)    #   a time, alternating between players
       cardDeck.dealOne(player2)

    
    playGame(cardDeck,player1,player2)

    if player1.handNotEmpty():
        print("\n\nGame over.  Player 1 wins!")
    else:
        print("\n\nGame over.  Player 2 wins!")

    print ("\n\nFinal hands:")    
    print ("Player 1:   ")
    print (player1)                 # printing a player object should print that player's hand
    print ("\nPlayer 2:")
    print (player2)                 # one of these players will have all of the cards, the other none
    
main()
