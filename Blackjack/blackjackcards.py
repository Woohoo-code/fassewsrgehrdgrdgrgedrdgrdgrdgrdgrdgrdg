import random
class card:
    def __init__(self, number, suit=""):
        self.number = number
        self.suit = suit
        self.numbers = []
    def cardmaker(self):
        result = ""
        if self.number < 11 and self.number != 1:
            self.numbers.append(self.number)
            result = result + str(self.number) + " of " + self.suit+ "s"
        elif self.number == 1: 
            self.numbers.append(1)
            result = result + "Ace" + " of " + self.suit + "s"
        elif self.number == 11: 
            self.numbers.append(11)
            result = result + "Jack" + " of " + self.suit + "s"
        elif self.number == 12: 
            self.numbers.append(12)
            result = result + "Queen" + " of " + self.suit + "s" 
        elif self.number == 13: 
            self.numbers.append(13)
            result = result + "King" + " of " + self.suit + "s"
        else:
            return "Invalid number"
        return result

class Deck:
    def __init__(self):
        self.deck = []
        self.number = 0
        for num in range(1,14):
            for suit in range(0,4):
                if suit == 0:
                    carder = card(num,"Heart")
                    self.deck.append(carder.cardmaker())   
                elif suit == 1:
                    carder = card(num,"Spade")
                    self.deck.append(carder.cardmaker())  
                elif suit == 2:
                    carder = card(num,"Diamond")
                    self.deck.append(carder.cardmaker()) 
                elif suit == 3:
                    carder = card(num,"Club")
                    self.deck.append(carder.cardmaker()) 
                else:
                    print("For loop error")
    
    def shuffle(self):
        for num in range(len((self.deck))-1):
            tempnum = random.randint(0,len(self.deck)-1)
            temp = self.deck[tempnum]
            tempnum2 = random.randint(0,len(self.deck)-1)
            temp2 = self.deck[tempnum2]
            self.deck[tempnum] = temp2
            self.deck[tempnum2] = temp
    def draw(self):
        return self.deck.pop()
    def lengthofdeck(self):
        return len(self.deck)
    


