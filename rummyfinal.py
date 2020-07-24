import pygame
import sys
import time
from deck import *
import random
#Gradiant Code from Net , Pygame recipe: http://www.pygame.org/wiki/GradientCode

pygame.init()

global x,y,i,qq,l1,z1,z2
global discardclick
global purpelclick,extracard
global u1,u2,u3,u4,u5,u6,u7,u8,u9,u10
u1,u2,u3,u4,u5,u6,u7,u8,u9,u10=0,0,0,0,0,0,0,0,0,0
extracard=0
discardclick,purpelclick=0,0
l1=[]
x,y,i,qq,z1,z2=0,0,0,0,0,0
win=pygame.display.set_mode((900,720))
pygame.display.set_caption("Rummy")
run=True
# win.fill((255,0,0))
upd=pygame.display.update
a=pygame.image.load(r"t\2_C.png")


discardedpile=[]


def loagimg(player):
	for card in player.hand:
		card.image=pygame.image.load("t/"+str(card)+".png").convert()
		# card.image=pygame.transform.scale(card.image,(80,100))



def producecentreimg(playingdeck):
	for card in playingdeck:
		card.image=pygame.image.load("t/"+str(card)+".png")
z=0
# def producedeck(playingdeck):
# 	global qq,l1
# 	for card,i in zip(playingdeck,range(len(playingdeck))):
		
# 		card.image=pygame.image.load("t/"+"purple_back"+".png")
# 		z=clickondeck(card)
# 		if z==1:
# 			card.clicked=1
# 			l1.append(card)
# 			# producediscardedpile()

# 		if z==1 or qq==1 or card.clicked:
# 			card.image=pygame.image.load("t/"+str(card)+".png")
# 			win.blit(card.image,(550,300))
# 			qq=1
# 		card.image=pygame.image.load("t/"+"purple_back"+".png")
# 		win.blit(card.image,(250,290))
# 		discardedpile.append(playingdeck.pop(i))


# def producediscardedpile():
# 	global l1
# 	print(l1)
# 	for jj in l1:
# 				if jj.clicked:
# 					jj.image=pygame.image.load("t/"+str(jj)+".png")
# 					win.blit(jj.image,(600,300))
# 					qq=1



def messagedisp(text,x,y):
	text1=pygame.font.Font('freesansbold.ttf',16)
	TextSurf=text1.render(text,True,(255,255,255))
	TextRect=TextSurf.get_rect()
	TextRect.center=(x,y)
	win.blit(TextSurf,TextRect)

def messagedisp2(text,x,y):
	text1=pygame.font.Font('freesansbold.ttf',55)
	TextSurf=text1.render(text,True,(255,255,255))
	TextRect=TextSurf.get_rect()
	TextRect.center=(x,y)
	win.blit(TextSurf,TextRect)

def showimg(player,y4,z):
	global x,y,i

	for card in player.hand:
		card.image=pygame.image.load("t/"+"gray_back"+".png")
	x,y=140,y4
	for card,i in zip(player.hand,range(13)):
			card.posx=x
			card.posy=y
			if u2:
				print("ll",card)
			win.blit(card.image,(card.posx,card.posy))
			x+=40
def touch(player,mouse,y4):
	global x,y,i
	x,y=90,y4
	i=0

	for card,i in zip(player.hand,range(13)):
		card.posx=x
		card.posy=y
		
		if card.clicked==1:
			clicker(card)
				
		elif clicked(card,i)[0]:
			win.blit(card.image,(card.posx,card.posy-20))
			x+=40
			i+=1
			
				# pygame.time.delay(500)
			
		elif hover(card,i)[0]:
			win.blit(card.image,(card.posx,card.posy-18))
			x+=40
			i+=1
			
		else:
			win.blit(card.image,(card.posx,card.posy))
			x+=40
			i+=1
		if i==4:
			x+=30
		if i==7:
			x+=30
		if i==10:
			x+=30

		
	return x,y

def hover(card,i):
	if card.posx<mouse[0]<card.posx+64 and card.posy<mouse[1]<card.posy+95 and (i==3 or i==6 or i==9 or i==12):
		
		return True,i
	if card.posx<mouse[0]<card.posx+41 and card.posy<mouse[1]<card.posy+95:
		
		return True,i
	else :
		return False,i

def clicked(card,i):
	if card.posx<mouse[0]<card.posx+64 and card.posy<mouse[1]<card.posy+95 and click[0]==1 and (i==3 or i==6 or i==9 or i==12):
		card.clicked=1
		return True,i
	if card.posx<mouse[0]<card.posx+41 and card.posy<mouse[1]<card.posy+95 and click[0]==1:
		card.clicked=1
		return True,i
	else :
		card.clicked=0
		return False,i


def clicker(card):
	global x,y,i
	win.blit(card.image,(card.posx,card.posy-20))
	x+=40
	i+=1

	if card.posx<mouse[0]<card.posx+50 and card.posy<mouse[1]<card.posy+95 and click[0]==1:
		card.clicked=0
		time.sleep(0.01)
		# pygame.time.delay(400)


def swap():
	for i in range(13):

		for j in range(13):
			if i!=j and player1.hand[i].clicked==1 and player1.hand[j].clicked==1:
				pygame.time.delay(250)
				player1.hand[i],player1.hand[j]=player1.hand[j],player1.hand[i]
				player1.hand[i].clicked=0
				player1.hand[j].clicked=0

# def swap2():
# 	l1=player1.hand+[extracard]
# 	for i in range(14):

# 		for j in range(14):
# 			if i!=j and l1[i].clicked==1 and l1[j].clicked==1:
# 				l1[i],l1[j]=l1[j],l1[i]
# 				l1[i].clicked=0
# 				l1[j].clicked=0

def clickondeck(card):
	if 250<mouse[0]<250+50 and 300<mouse[1]<300+95 and click[0]==1 :
		card.clicked=1
		return card.clicked



def game_intro():
	intro=True
	while intro:
		for event in pygame.event.get():
			if event.type==pygame.QUIT:
				intro=False
		win.fill((20,20,150))			
		messagedisp("YOU LOST",400,360)
		upd()		


loagimg(player1)

joker=playingdeck.pop(0)
joker.image=pygame.image.load("t/"+str(joker)+".png")
joker.image=pygame.transform.rotate(joker.image,20)
mouse=pygame.mouse.get_pos()
global d1
d1=0
discard1=playingdeck.pop(0)
discardedpile.append(discard1)
discard1.image=pygame.image.load("t/"+str(discard1)+".png")

purplecard=pygame.image.load("t/"+"purple_back"+".png")


def clickondiscard():
	global discardclick
	if 520<mouse[0]<520+64 and 300<mouse[1]<300+95 and click[0]==1 :
		discardclick=1

		print(discardclick,purpelclick)
		return True
	else :
		return False

def checkmove(t1,t2):
	global z1,z2,extracard,u1

	if t1:
		z1=1
		extracard=playingdeck.pop(0)
		extracard.posx=800
		extracard.posy=540
		print(extracard)
		u1=1
		t1=0
	if t2:
		z2=1
		extracard=discardedpile.pop(-1)
		extracard.posx=800
		extracard.posy=540
		print(extracard)
		u1=1
		t2=0
	
def showextra(z1,z2):
	
	if z1:

		extracard.image=pygame.image.load("t/"+str(extracard)+".png")			
		win.blit(extracard.image,(780,540))
	elif z2:
		extracard.image=pygame.image.load("t/"+str(extracard)+".png")			
		win.blit(extracard.image,(780,540))
		


def clickonpurple():
	global purpelclick
	if 250<mouse[0]<250+64 and 290<mouse[1]<290+95 and click[0]==1 :
		purpelclick=1

		print(discardclick,purpelclick)
		return True
	else :
		return False

def discardacard():
	l1=player1.hand+[extracard]
	global d1,u1,u2
	for card in l1:
		if card.posx<mouse[0]<card.posx+40 and card.posy<mouse[1]<card.posy+95 and click[0]==1:		
			discardedpile.append(card)
			print(discardedpile)
			if card!=extracard:
				player1.hand.append(extracard)
				i=player1.hand.index(card)
				player1.hand[i]=extracard
				d1=0
				u1=0
				u2=1


			else:
				d1=0
				u1=0
			
				u2=1
				

				
	for card in player1.hand:
		card.clicked=0





def show_disca():
	if len(discardedpile)!=0:
		discardedpile[-1].image=pygame.image.load("t/"+str(discardedpile[-1])+".png")			
		win.blit(discardedpile[-1].image,(520,300))


def compturn():
	global u2,u6
	v12=[]
	
	for i in player2.hand:
		v12.append(i.cardv.value)
	
	if v12.count(discardedpile[-1].cardv.value)==2:
		player2.hand.append(discardedpile.pop(-1))
		print("herer2j23e43")


		discardedpile.append(player2.hand.pop(random.randint(0,8)))
	else:
		print("2j23e43",player2.hand)
		player2.hand.append(playingdeck.pop(-1))
		discardedpile.append(player2.hand.pop(random.randint(0,8)))
	# pygame.time.delay(2000)
	u2=0	
	u6+=1		
def button(text,x,y):
	if x<mouse[0]<x+70 and y<mouse[1]<y+50 and click[0]==1:
		pygame.draw.rect(win,(255,0,0),(x,y,70,50))
		print("here")
		checkwin()
	elif x<mouse[0]<x+70 and y<mouse[1]<y+50:
		pygame.draw.rect(win,(250,0,0),(x,y,70,50))
		print(click)
	
	else:
		pygame.draw.rect(win,(160,0,0),(x,y,70,50))
	text1=pygame.font.Font('freesansbold.ttf',14)
	TextSurf=text1.render(text,True,(255,255,255))
	TextRect=TextSurf.get_rect()
	TextRect=(x+10,y+15)
	win.blit(TextSurf,TextRect)
			
def checkwin():
	global u7,u8,u9,u10
	v1=[]

	for i in player1.hand:
		v1.append(i.cardv.value)
	
	for card,i in zip(player1.hand,range(13)):
		if i==3:
			for j in range(3):
				# if player1.hand[j].cards!=player1.hand[j+1].cards:
				u7=1
				if v1[j]!=v1[j+1]+1 :
					u8=1
	if (u7 and u8)==1:
		u9=1
	else:
		u10=1


def fill_gradient(surface, color, gradient, rect=None, vertical=True, forward=True):
    """fill a surface with a gradient pattern
    Parameters:
    color -> starting color
    gradient -> final color
    rect -> area to fill; default is surface's rect
    vertical -> True=vertical; False=horizontal
    forward -> True=forward; False=reverse
    
    Pygame recipe: http://www.pygame.org/wiki/GradientCode
    """
    if rect is None: rect = surface.get_rect()
    x1,x2 = rect.left, rect.right
    y1,y2 = rect.top, rect.bottom
    if vertical: h = y2-y1
    else:        h = x2-x1
    if forward: a, b = color, gradient
    else:       b, a = color, gradient
    rate = (
        float(b[0]-a[0])/h,
        float(b[1]-a[1])/h,
        float(b[2]-a[2])/h
    )
    fn_line = pygame.draw.line
    if vertical:
        for line in range(y1,y2):
            color = (
                min(max(a[0]+(rate[0]*(line-y1)),0),255),
                min(max(a[1]+(rate[1]*(line-y1)),0),255),
                min(max(a[2]+(rate[2]*(line-y1)),0),255)
            )
            fn_line(surface, color, (x1,line), (x2,line))
    else:
        for col in range(x1,x2):
            color = (
                min(max(a[0]+(rate[0]*(col-x1)),0),255),
                min(max(a[1]+(rate[1]*(col-x1)),0),255),
                min(max(a[2]+(rate[2]*(col-x1)),0),255)
            )
            fn_line(surface, color, (col,y1), (col,y2))


while run:
	if u6==15 or u9==1:
		win.fill((0,0,0))
		messagedisp2("Sorry!! YOU LOST",400,350)
		for event in pygame.event.get():
			if event.type==pygame.QUIT :
				run=False
		upd()
	elif u10==1:
		win.fill((0,0,0))
		messagedisp2("YOU WON",400,350)
		for event in pygame.event.get():
			if event.type==pygame.QUIT :
				run=False
		upd()
	else:
		# clock=pygame.time.Clock()
		# clock.tick(30)
		# pygame.time.delay(10)
		fill_gradient(win,(16,125,18),(0,3,0))
		# win.fill((16,75,18))
		# bg=pygame.image.load("t/rummy.png")
		# bg=pygame.transform.scale(bg,(900,720))
		# win.blit(bg,(0,0))

		# win.blit(a,(70,70))
		mouse=pygame.mouse.get_pos()
		# click=pygame.mouse.get_pressed()
		click=(0,0)
		for event in pygame.event.get():
			if event.type==pygame.QUIT :
				run=False
			if event.type==pygame.MOUSEBUTTONDOWN:
				click=pygame.mouse.get_pressed()
				print("click")

		


		messagedisp("First Life",120,660)
		messagedisp("Second Life",320,660)
		messagedisp("Run/Set",460,660)
		messagedisp("Run/Set",620,660)
		x,y=60,400
		showimg(player2,30,True)
		
		swap()
		win.blit(joker.image,(200,290))
		
		win.blit(purplecard,(250,290))
		# producedeck(playingdeck)
		if u2==0:
			messagedisp("Your Turn",600,180)
		else:
			for card in player1.hand:
				card.clicked=0

			messagedisp("Computers's Turn",600,180)
			u3=1

		z=touch(player1,mouse,540)
			

		t2=clickondiscard()
		t1=clickonpurple()

		if t1!=t2:
			checkmove(t1,t2)
			d1=1
		
		if d1:
			messagedisp("Discard a Card",400,200)
			discardacard()
			

			

		button("Declare",80,460)
			
		show_disca()
		if u1:
			showextra(z1,z2)
		# print(t1,t2,d1)
		
		upd()
		if u3:
			pygame.time.delay(3000)
			compturn()
			u3=0



