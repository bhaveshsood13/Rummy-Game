from enum import Enum
import random
fulldeck=[]
class Suit(Enum):
	Spades="spades"
	Hearts="hearts"
	Clubs="clubs"
	Diamonds="diamonds"
	def __str__(self):
		return str(self.name[0])
	def __eq__(self,other):
		return self.value==other.value

class Card(Enum):
	ONE=1
	TWO=2
	THREE=3
	FOUR=4
	FIVE=5
	SIX=6
	SEVEN=7
	EIGHT=8
	NINE=9
	TEN=10
	JACK=11
	QUEEN=12
	KING=13
	# ACE=14
	def __lt__(self,other):
		return self.value>other.value
	def __str__(self):
		return str(self.value)
	def __eq__(self,other):
		return self.value==other.value
	def __add__(self,other):
		return self.value+ other.value
alpha=Card(1)

class PlayingCard:
	def __init__(self,c_value,c_suit,image=-1,posx=1,posy=1,clicked=0):
		self.cardv=c_value
		self.cards=c_suit
		self.image=image
		self.posx=posx
		self.posy=posy
		self.clicked=clicked
	def __str__(self):
		return  str(self.cardv)+"_"+str(self.cards)
	def __lt__(self,other):
		return self.cardv>other.cardv
def create_deck():
	for i in Suit:
		for j in Card:
			fulldeck.append(PlayingCard(Card(j),Suit(i)))
	return fulldeck
print(len(create_deck()))

for i in range(len(fulldeck)):
	print(fulldeck[i])



class Player:
	def __init__(self,hand):
		self.hand=hand

playingdeck=fulldeck[:]
random.shuffle(playingdeck)
random.shuffle(playingdeck)
print('JOKL',len(playingdeck),len(fulldeck))
for i in range(52):
	print(playingdeck[i])
h=[]
h1=[]
player1=Player(h)
player2=Player(h1)
for i in range(13):
	player1.hand.append(playingdeck[i])
	playingdeck.pop(i)
player1.hand.sort()
print("PLAyer1 HAND sorted")
for i in range(len(player1.hand)):
	print(player1.hand[i])
print("now deck",len(playingdeck))
for i in range(len(playingdeck)):
	print(playingdeck[i])
for i in range(13):
	player2.hand.append(playingdeck[i])
	playingdeck.pop(i)

print("PLAyer HAND")
for i in range(len(player1.hand)):
	print(player1.hand[i])

# for i in range(13):
player2.hand.sort()
print("PLAyer2 HAND sorted",len(player2.hand))
for i in range(len(player2.hand)):
	print(player2.hand[i])


# print(playingdeck)