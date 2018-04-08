#owl Design

import simplegui
import math
Blue=False
Teal=False
Navy=False
White=False
Black=False
Yellow=False
Blink_Eyes=False
Blink_Eyes1=False

def Toggle_blue():
    global Blue
    Blue=not Blue

def Toggle_teal():
    global Teal
    Teal=not Teal
    
def Toggle_navy():
    global Navy
    Navy=not Navy
    
def Toggle_white():
    global White
    White=not White
    
def Toggle_black():
    global Black
    Black=not Black
    
def Toggle_yellow():
    global Yellow
    Yellow=not Yellow
    
def tick():
    global Blink_Eyes,Blink_Eyes1,Black,White
    if Blink_Eyes:
        Black=not Black
        
    if Blink_Eyes1:
        White=not White
        Black=not Black
        
def BLINK_EYES():
    global Blink_Eyes,Black
    Blink_Eyes=not Blink_Eyes
    Black=not Black
    timer.start()
    
def BLINK_EYES1():
    global Blink_Eyes1,White,Black
    Blink_Eyes1=not Blink_Eyes1
    White=not White
    Black=not Black
    timer.start()
    
def draw(canvas):
    if Navy:
        #left_Ear
        canvas.draw_polygon([[225,121],[260,96],[220,50]],1,"Navy","Navy")
        #Right_Ear
        canvas.draw_polygon([[340,96],[375,121],[385,50]],1,"Navy","Navy")
        
        #left_Hand
        canvas.draw_circle([60,310],30,1,"Navy","Navy")
        canvas.draw_circle([60,350],30,1,"Navy","Navy")
        canvas.draw_circle([60,390],30,1,"Navy","Navy")
        canvas.draw_polygon([[75,283],[75,417],[350,340]],1,"Navy","Navy")
        
        #Right_Hand
        canvas.draw_circle([540,310],30,1,"Navy","Navy")
        canvas.draw_circle([540,350],30,1,"Navy","Navy")
        canvas.draw_circle([540,390],30,1,"Navy","Navy")
        canvas.draw_polygon([[525,283],[525,417],[250,340]],1,"Navy","Navy")
    if Blue:
        #Body
        canvas.draw_circle([300,350],150,2,"blue","blue")
        canvas.draw_circle([300,190],100,2,"blue","blue")
    if Teal:
        #Stomach
        canvas.draw_circle([300,350],100,2,"teal","teal")
    if White:
        #Eyes
        canvas.draw_circle([265,175],20,2,"white","white")
        canvas.draw_circle([335,175],20,2,"white","white")
    if Black:
        #pupil
        canvas.draw_circle([265,183],10,2,"black","black")
        canvas.draw_circle([335,183],10,2,"black","black")
    if Yellow:
        #Nose
        canvas.draw_polygon([[300,220],[290,190],[310,190]],1,"yellow","yellow")
        #Left_leg
        canvas.draw_polygon([[244,490],[230,510],[235,510]],1,"yellow","yellow")
        canvas.draw_polygon([[246,491],[240,510],[245,510]],1,"yellow","yellow")
        canvas.draw_polygon([[248,492],[250,510],[255,510]],1,"yellow","yellow")
        #Right_leg
        canvas.draw_polygon([[366,486],[384,506],[378,506]],1,"yellow","yellow")
        canvas.draw_polygon([[364,487],[373,506],[368,506]],1,"yellow","yellow")
        canvas.draw_polygon([[362,488],[363,506],[358,506]],1,"yellow","yellow")
        
frame=simplegui.create_frame("OWL",600,600)
timer=simplegui.create_timer(500,tick)
frame.set_draw_handler(draw)
frame.add_button("Blue",Toggle_blue)
frame.add_button("Teal",Toggle_teal)
frame.add_button("Navy",Toggle_navy)
frame.add_button("White",Toggle_white)
frame.add_button("Black",Toggle_black)
frame.add_button("Yellow",Toggle_yellow)
frame.add_label("\n\n")
frame.add_button("Blink_Pupil",BLINK_EYES)
frame.add_button("Blink_Eyes",BLINK_EYES1)

frame.start()