#Card Remember Game
#0 To 9 Number Card available in hide format when you press the card is turn on and show the card number.
#first step is press any card 
#next step is press different card if card number is matches then it doesn't turns off if doesn't match then after pressing the third card first two card is turns off.
#Label turns show that How many steps you take for complete the game. when two card is open then turns count is increase

import simplegui
import random
s1=s2=range(0,10)
s3=s1+s2
t=0
state=0
f=1

#For Reset 
def reset():
    global card,s3,t,state
    t=0
    state=0
    card=[False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False]
    random.shuffle(s3)
    
def new_game():
    global s3,t,card,state
    card=[False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False]
    random.shuffle(s3)
    t=0
    state=0
    label.set_text("Turns = "+ str(t))
    
    
def mouse_click(pos):
    global card,state,t,i,i1,i2,f
    if pos[0]>0 and pos[0]<=49:
        if card[0]==False:
            card[0]=True
            i=0
            f=1
    elif pos[0]>50 and pos[0]<=99:
        if card[1]==False:
            card[1]=True
            i=1
            f=1
    elif pos[0]>100 and pos[0]<=149:
        if card[2]==False:
            card[2]=True
            i=2
            f=1
    elif pos[0]>150 and pos[0]<=199:
        if card[3]==False:
            card[3]=True
            i=3
            f=1
    elif pos[0]>200 and pos[0]<=249:
        if card[4]==False:
            card[4]=True
            i=4
            f=1
    elif pos[0]>250 and pos[0]<=299:
        if card[5]==False:
            card[5]=True
            i=5
            f=1
    elif pos[0]>300 and pos[0]<349:
        if card[6]==False:
            card[6]=True
            i=6
            f=1
    elif pos[0]>350 and pos[0]<=399:
        if card[7]==False:
            card[7]=True
            i=7
            f=1
    elif pos[0]>400 and pos[0]<=449:
        if card[8]==False:
            card[8]=True
            i=8
            f=1
    elif pos[0]>450 and pos[0]<=499:
        if card[9]==False:
            card[9]=True
            i=9
            f=1
    elif pos[0]>500 and pos[0]<=549:
        if card[10]==False:
            card[10]=True
            i=10
            f=1
    elif pos[0]>550 and pos[0]<=599:
        if card[11]==False:
            card[11]=True        
            i=11
            f=1
    elif pos[0]>600 and pos[0]<=649:
        if card[12]==False:
            card[12]=True
            i=12
            f=1
    elif pos[0]>650 and pos[0]<=699:
        if card[13]==False:
            card[13]=True        
            i=13
            f=1
    elif pos[0]>700 and pos[0]<=749:
        if card[14]==False:
            card[14]=True
            i=14
            f=1
    elif pos[0]>750 and pos[0]<=799:
        if card[15]==False:
            card[15]=True
            i=15
            f=1
    elif pos[0]>800 and pos[0]<=849:
        if card[16]==False:
            card[16]=True
            i=16
            f=1
    elif pos[0]>850 and pos[0]<=899:
        if card[17]==False:
            card[17]=True
            i=17
            f=1
    elif pos[0]>900 and pos[0]<=949:
        if card[18]==False:
            card[18]=True
            i=18
            f=1            
    elif pos[0]>950 and pos[0]<=999:
        if card[19]==False:
            card[19]=True
            i=19
            f=1
            
    if f==1:
        if state==0:
            state=1
            i1=i
        elif state==1:
            if i1!=i:
                state=2
                i2=i
                t+=1	
                label.set_text("Turns = "+ str(t))
        else:
            if i2!=i and i1!=i:
                state=1
                if s3[i1]!=s3[i2]:
                    card[i1]=False
                    card[i2]=False
                i1=i
                f=0
def draw(canvas):
    global a,b,c,d,s,card,i,t
    s=8
    a=0
    b=0
    c=50
    d=100
    for i in s3:
        canvas.draw_text(str(i),[s,65],66,"White")
        s+=50
    for j in card:
        if j==False:
            canvas.draw_polygon([[a,b],[a,d],[c,d],[c,b]],1,"Black","yellow")
            
        a+=50
        c+=50
    
frame=simplegui.create_frame("Remember card",1000,100)
#Reset Button
frame.add_button("RESET",reset)
#Count the turns
label=frame.add_label("Turns = "+ str(t))
frame.set_draw_handler(draw)
frame.set_mouseclick_handler(mouse_click)
#start_here
new_game()
frame.start()