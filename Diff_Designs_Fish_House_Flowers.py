#Example OF Differnt Design 

import simplegui
import math
Fish=False
House=False
Flower=False
Dipper=False
c1=400
c2=390
c3=385
a=415
b=100
w=80
k=False
z=False
r=2
x=150
l=135
def fish():
    global Fish
    Fish=not Fish
def house():
    global House
    House=not House
def flower():
    global Flower
    Flower=not Flower
def dipper():
    global Dipper
    Dipper=not Dipper
def Lfish():
    global k
    k=not k
def Grow_Flower():
    global z
    z=not z
def draw(canvas):
    if Fish:
        global a,c1,c2,c3,k,y
        if k==True:
            a-=2
            c1-=2
            c2-=2
            c3-=2
            if c1==-80:
                a=600
                c1=584
                c2=576
                c3=572
        canvas.draw_circle([c1,100],30,2,"orange","orange")
        canvas.draw_circle([c2,100],10,2,"white","white")
        canvas.draw_circle([c3,103],5,1,"black","black")
        canvas.draw_polygon([[a,b],[a+w/2/math.tan(math.pi/6),b-w/2],[a+w/2/math.tan(math.pi/6),b+w/2]],2,"orange","orange")
        
                    
    if House:
        #terrase
        canvas.draw_polygon([[445,300],[300,400],[600,400]],2,"black","gray")
        #base
        canvas.draw_polygon([[325,400],[325,590],[575,590],[575,400]],1,"green","green")
        #windows
        canvas.draw_polygon([[350,420],[350,480],[400,480],[400,420]],1,"black","blue")
        canvas.draw_polygon([[550,420],[550,480],[500,480],[500,420]],1,"black","blue")
        #door
        canvas.draw_polygon([[425,500],[425,588],[475,588],[475,500]],1,"black","gray")
        canvas.draw_circle([435,545],5,1,"black","black")
    if Flower:
        global z,r,x,l
        if z:
            r+=0.5
            x-=0.8
            l-=0.2
            if r>=34:
                z=False
                x=100
                l=135
        #first top Circle
        canvas.draw_circle([125,370],r,2,"red","white")
        #Rectangle and circle
        canvas.draw_circle([x,520],30,2,"red","green")
        canvas.draw_polygon([[115,405],[115,590],[l,590],[l,405]],2,"red","green")        
        #bottom circle
        canvas.draw_circle([125,445],r,2,"red","white")
        #left circle
        canvas.draw_circle([90,410],r,2,"red","white")
        #Right circle
        canvas.draw_circle([158,410],r,2,"red","white")
        #center circle
        canvas.draw_circle([125,405],30,2,"white","green")
    if Dipper:
        d1=[50,80]
        d2=[75,100]
        d3=[85,75]
        d4=[100,90]
        d5=[115,125]
        d6=[125,100]
        d7=[140,160]
        d8=[165,140]
        canvas.draw_polyline([d1,d2,d3,d4,d5,d6,d7,d8],2,"white")
        canvas.draw_circle(d1,2,2,"white","black")
        canvas.draw_circle(d2,2,2,"white","black")
        canvas.draw_circle(d3,2,2,"white","black")
        canvas.draw_circle(d4,2,2,"white","black")
        canvas.draw_circle(d5,2,2,"white","black")
        canvas.draw_circle(d6,2,2,"white","black")
        canvas.draw_circle(d7,2,2,"white","black")
        canvas.draw_circle(d8,2,2,"white","black")
        
frame=simplegui.create_frame("Design",600,600)
l1=frame.add_label("click to button Show Design and click again to Remove Design")
l2=frame.add_label("\n")
l3=frame.add_label("<<Toggle Buttons>>")
l4=frame.add_label("\n")
frame.add_button("Fish",fish)
frame.add_button("House",house)
frame.add_button("Flower",flower)
frame.add_button("Dipper",dipper)

#Buttons for Moving The Object
frame.add_label("\n")
frame.add_label("Buttons for moving the object:")
frame.add_label("\n")
frame.add_button("Left Side Scroll Fish",Lfish)
frame.add_button("Grow Flower",Grow_Flower)

frame.set_draw_handler(draw)
frame.start()
