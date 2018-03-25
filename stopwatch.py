#Run The Program On CodeSkulptor

#Mini Game For Stop Watch program
#Create Start,Pause,Reset Button when you press the pause button and millisecond is 0 then increase the score
#When press pause Button count how many attempt you have carry out

import simplegui

message = ":"
s=0		#For Seconds
m=0		#For Minute
h=0		#For Hour
A=0		#For Attempts
mm=0		#For milliseconds
p=0		#For points(Score)
a="Attempt:"
w="STOP WATCH"
scr="Score:"
dot="."
pause=True


def tick():
    global s,m,h,mm,pause
    if pause:
        mm+=1
        if mm==10:
            s+=1
            s=s%60
            mm=0
            if s==0:
                m+=1
                if m==60:
                    h+=1
                    m=0
        
#Start Button            
def strt():
    timer.start()


#Pause Button
def stp():
    global s,m,h,mm,pause,p,A
    if pause:
        A+=1
        pause=not pause
        if mm==0:
            p+=1            
    else:
        pause=not pause

#Reset Button
def rst():
    global s,m,h,mm,A,pause,p
    mm=0
    s=0
    m=0
    h=0
    A=0
    p=0
    pause=not pause
    timer.stop()
   

#print all on the canvas using draw function
def draw(canvas):
    global w,a,A,p
    canvas.draw_text(a,[10,20], 18,"Red" )
    canvas.draw_text(str(A),[80,20],18,"white")
    canvas.draw_text(scr,[180,20], 18,"Red" )
    canvas.draw_text(str(p),[230,20], 18,"white" )
    canvas.draw_text(w,[60,75], 24,"Red" )
    canvas.draw_text(str(mm),[220,110],36,"white")
    canvas.draw_text(dot, [195,110], 48,"white" )
    canvas.draw_text(str(s),[160,110],36,"white")
    canvas.draw_text(str(m),[110,110],36,"white")
    canvas.draw_text(message, [90,110], 48,"white" )
    canvas.draw_text(str(h),[60,110],36,"white")
    canvas.draw_text(message, [145,110], 48,"white" )
    
    

# Create a frame and assign callbacks to event handlers
frame = simplegui.create_frame("Home", 300, 200)
timer = simplegui.create_timer(100,tick)
frame.add_button("Start",strt)
frame.add_button("Pause",stp)
frame.add_button("Reset",rst)
frame.set_draw_handler(draw)

# Start the frame animation
frame.start()

