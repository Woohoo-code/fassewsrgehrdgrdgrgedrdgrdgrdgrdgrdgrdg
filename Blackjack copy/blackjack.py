from blackjackcards import Deck
decks = Deck()
decks.shuffle()
player_hand = []
dealer_hand = []
player_hand.append(decks.draw())
player_hand.append(decks.draw())
dealer_hand.append(decks.draw())
dealer_hand.append(decks.draw())
pscore = 0
dscore = 0
game = True
turn = True
dealer = True
def calculatescore(person):
    score = 0
    for i in range(len(person)):
            handsplit = person[i].split(" ")
            if handsplit[0] == "Jack" or handsplit[0] == "Queen"  or handsplit[0] == "King":
                score += 10
            elif handsplit[0] == "Ace":
                score += 11
                aces = 0
                for k in range(len(person)):
                    j = person[k].split(" ")
                    if j[0] == "Ace":
                        aces +=1
                if score > 21 and aces > 0:
                    score -= 10
                    aces -= 1

            else:
                score += int(handsplit[0])
    return score


while game:
    if pscore > dscore and pscore < 22:
        print("Player Won")
        game = False
    elif dscore > pscore and dscore < 22:
        print("Dealer Won")
        game = False
    print("Player hand :    " + str(player_hand), " Dealer hand :    " + str(dealer_hand[1]))
    pscore = calculatescore(player_hand)
    dscore = calculatescore(dealer_hand)
    while turn:
        
        if pscore == 21:
            turn = False
            game = False
            print("Blackjack")
        if not pscore == 21:
            inp = input("Hit or Stand (h or s)").lower() == "h"
        if inp == "h":
            player_hand.append(decks.draw())
            pscore = calculatescore(player_hand)
            print(player_hand)
            print(pscore)
            if pscore > 21:
                print("Player Bust, Score: ", pscore)
                game = False
                turn = False
        elif inp == "s":
            turn = False
        
    while dealer:
        if dscore < 17:
            dealer_hand.append(decks.draw())
            dscore = calculatescore(dealer_hand)
            dealer = False
        else:
            dscore = calculatescore(dealer_hand)
            dealer = False
    if dscore == pscore and dscore < 22 and pscore < 22:
        print("Push")
        print("Dealer's hand: " + str(dealer_hand), "Dealer score: " + str(dscore))
        game = False
    elif pscore > dscore and pscore < 22:
        print("Player Won")
        print("Dealer's hand: " + str(dealer_hand), "Dealer score: " + str(dscore))
        game = False
    elif dscore > pscore and dscore < 22:
        print("Dealer Won")
        print("Dealer's hand: " + str(dealer_hand), "Dealer score: " + str(dscore))
        game = False
    
    