from cards import Deck, card
decke = Deck()
decke.shuffle()
p1score = 0
p2score = 0

while (decke.lengthofdeck() > 0):
    play1 = decke.draw()
    play2 = decke.draw()
    play1.split(" ")
    play2.split(" ")
    print("Player #1's card: " +str(play1), "Player #2's card: " + str(play2))
    if play1[0] == "Jack":
        play1[0] = 11
    elif play1[0] == "Queen":
        play1[0] = 12
    elif play1[0] == "King":
        play1[0] = 13
    elif play1[0] == "Ace":
        play1[0] = 14
    if play2[0] == "Jack":
        play2[0] = 11
    elif play2[0] == "Queen":
        play2[0] = 12
    elif play2[0] == "King":
        play2[0] = 13
    elif play2[0] == "Ace":
        play2[0] = 14
    if play1[0] > play2[0]:
        print("Player 1 won this round")
        p1score += 1
    elif play2[0] > play1[0]:
        print("Player 2 won this round")
        p2score += 1
    elif play1[0] == play2[0]:
        print("Tie")
if p1score > p2score:
    print("Player 1 wins with " + str(p1score) + " points", "\nPlayer 2 loses with " + str(p2score) +  " points")
elif p1score > p2score:
    print("Player 2 wins with " + str(p2score) + " points", "\nPlayer 1 loses with " + str(p2score) +  " points")
else:
    print("TIE","\nPlayer 2 scores " + str(p2score) +  " Points ", "\nPlayer 1 Scores " + str(p2score) +  " points")
