#Game for moving Bubbles
#Here Two Bubbles available Blue and Red.
#start with Blue Bubble.
#it try to touch Red Bubble if it successful then Red Bubble is out and Blue Bubble is win.
#change the position of Bubble Automatically.now Red Bubble try to Blue Bubble out.
#Use up,down,left,right and A,W,S,D key for moving bubble
import simplegui
import math
x1=20
y1=20
x2=50
y2=100
x11=0
y11=0
x22=0
y22=0
B1="Blue"
B2="Red"
c1=B1
c2=B2
b1=[x1,y1]
b2=[x2,y2]

def Up(up):
    global x11,x22,y11,y22
    if up==simplegui.KEY_MAP['up']:
        y11=0
    if up==simplegui.KEY_MAP['down']:
        y11=0
    if up==simplegui.KEY_MAP['left']:
        x11=0
    if up==simplegui.KEY_MAP['right']:
        x11=0 
    if up==simplegui.KEY_MAP['w']:
        y22=0
    if up==simplegui.KEY_MAP['s']:
        y22=0
    if up==simplegui.KEY_MAP['a']:
        x22=0
    if up==simplegui.KEY_MAP['d']: 
        x22=0 
    
def Down(down):
    global x11,x22,y11,y22
    if down==simplegui.KEY_MAP['up']:
        if b1[1]>=16:
            y11=-4
    if down==simplegui.KEY_MAP['down']:
        if b1[1]<=584:
            y11=4
    if down==simplegui.KEY_MAP['left']:
        if b1[0]>=16:
            x11=-4
    if down==simplegui.KEY_MAP['right']:
        if b1[0]<=584:
            x11=4
    if down==simplegui.KEY_MAP['w']:
        if b2[1]>=16:
            y22=-4
    if down==simplegui.KEY_MAP['s']:
        if b2[1]<=584:
            y22=4
    if down==simplegui.KEY_MAP['a']:
        if b2[0]>=16:
            x22=-4
    if down==simplegui.KEY_MAP['d']:
        if b2[0]<=584:
            x22=4
        
def dist(b1,b2):
    return math.sqrt((b1[0]-b2[0])**2+(b1[1]-b2[1])**2)

def draw(canvas):
    global x11,x22,y11,y22,c1,c2,b1,b2
    canvas.draw_circle(b1,15,1,"Black",c1)
    canvas.draw_circle(b2,15,1,"Black",c2)
    b1[0]+=x11
    b1[1]+=y11
    b2[0]+=x22
    b2[1]+=y22
    if b1[0]<=15 or b1[0]>=585:
        x11=0
    if b2[0]<=15 or b2[0]>=585:
        x22=0
    if b1[1]<=15 or b1[1]>=585:
        y11=0
    if b2[1]<=15 or b2[1]>=585:
        y22=0
        
    #when touch the bubble to each other then this code is Run
    if dist(b1,b2)<30:
        x1=20
        y1=20
        x2=50
        y2=100
        c2=c1
        
        #Change the Bubble color
        if c2==B1:
            c1=B2 
        if c2==B2:
            c1=B1
        
        #Set at the start position
        b1=[x1,y1]
        b2=[x2,y2]
        
frame=simplegui.create_frame("Game",600,600)
frame.set_draw_handler(draw)
frame.set_keyup_handler(Up)
frame.set_keydown_handler(Down)

frame.start()