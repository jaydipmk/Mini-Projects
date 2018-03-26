#Run The Program on CodeSkulptor
#CodeSkulptor NOT Run Properly in Internet Explorer Therefor Run in Other Browser like Google Chrome.
#This program is Simple Game 
#When we press the UP Button the circle move down to up and attempt count is Increase
#The score is moving left to right
#If the circle touch the score then score is increase
#Play the Game and enjoy it.

import simplegui
a=0		#Attempt
x=False
y=165
s=0		#Score
p=-19

#UP Button Event Call
def up():
    global x,y,a
    a+=1
    y-=2
    x=True

# Handler to draw on canvas
def draw(canvas):
    global y,x,p,s
    canvas.draw_text(str(s), [p,50], 36, "Red")
    canvas.draw_text(str(a), [145,200], 36, "Red")
    p+=1
    if p==299:
        p=-19
    if p>135 and p<155 and x==True and y<55 and y>25:
        s+=1
        x=False
    if x==True:
        canvas.draw_circle([153,y],10,1, "white", "Red")
        while x:
            if y<165:
                y-=3
                if y<5:
                    y=165
                    x=False
            break
            
#Create a frame and assign callbacks to event handlers
frame = simplegui.create_frame("Home", 300, 200)
frame.add_button("UP", up)							#Add Button on Canvas
frame.set_draw_handler(draw)

# Start the frame animation
frame.start()