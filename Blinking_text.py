#Example of Blinking Line
import simplegui
m="Write Text in Textbox"	
y=True

def tick():
    global y
    y=not y 

#Create function for Change the text
def text(u):
    global m
    m=u

def draw(canvas): 
    if y:
        canvas.draw_text(m,[280,112],36,"blue")
    
#Create Frame               
frame=simplegui.create_frame("Blinking Text",800,200)
frame.set_draw_handler(draw)
frame.add_input("Enter The Text",text,100)
timer=simplegui.create_timer(500,tick)
frame.start()
timer.start()