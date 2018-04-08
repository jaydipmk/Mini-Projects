#program for change the background 
#using button change the size of text and also scroll it left and right.
#stop scroll for using stop scroll button

import simplegui
text="welcome"
s=36
l=50
d=0
def shrink():
    global s
    s-=2
def grow():
    global s
    s+=2
def Leftscroll():
    global d
    d=-2
def Rightscroll():
    global d
    d=2   
def stop():
    global d
    d=0
def color(v):
    frame.set_canvas_background(v)

def draw(canvas):
    global l,d
    canvas.draw_text(text,[l,150],s,"white")
    l+=d
    if l==-128:
        l=300
    elif l==300:
        l=-128
    
frame=simplegui.create_frame("Formatting the text",300,300)
frame.add_button("Shrink",shrink)
frame.add_button("Graw",grow)
frame.add_button("Left scroll",Leftscroll)
frame.add_button("Right Scroll",Rightscroll)
frame.add_button("Stop Scroll",stop)
frame.add_input("change ackground Color",color,100)
frame.set_draw_handler(draw)

frame.start()
