#RiceRocks Game

#import the Modules

import simplegui
import random
import math

#Globals for User Interface

WIDTH=800
HEIGHT=600
lives=3
time=0
tim=0
expos=[WIDTH/2,HEIGHT/2]
score=0
expl=False
started=False
rock_group=set([])
missile_group=set([])
rmst=set([])


#Create a class

class ImageInfo:
    def __init__(self,center,size,radius=0,lifespan=None,animated=None):
        self.center=center
        self.size=size
        self.radius=radius
        if lifespan:
            self.lifespan = lifespan
        else:
            self.lifespan = float("inf")
            
        self.animated=animated

    def get_center(self):
        return self.center
    
    def get_size(self):
        return self.size
    
    def get_radius(self):
        return self.radius
    
    def get_lifespan(self):
        return self.lifespan
    
    def get_animated(self):
        return self.animated
    
    
#All images are displayed in canvas
#Please Put The All Images Path

#Debris Image
debris_info=ImageInfo([320,240],[640,480])
debris_image=simplegui.load_image("F:\debris2_blue.png")


#nebula Images
#nebula2=simplegui.load_image('F:/nebula_blue.png')
nebula_info=ImageInfo([400,300],[800,600])
nebula_image=simplegui.load_image("F:\nebula_blue.png")

#splash Image
splash_info=ImageInfo([200,150],[400,300])
splash_image=simplegui.load_image("F:\python\Game\Ricerocks\splash.png")
                        
            
#ship Image
ship_info=ImageInfo([45,45],[90,90],35)
ship_image=simplegui.load_image("F:\python\Game\Ricerocks\double_ship.png")

#missile Image
missile_info=ImageInfo([5,5],[10,10],3,50)
missile_image=simplegui.load_image("F:\python\Game\Ricerocks\shot2.png")

#asteroid Image
asteroid_info=ImageInfo([45,45],[90,90],40)
asteroid_image=simplegui.load_image("F:\python\Game\Ricerocks\asteroid_blue.png")


#sounds
soundtrack=simplegui.load_sound("F:\python\Game\Ricerocks\soundtrack.mp3")
missile_sound=simplegui.load_sound("F:\python\Game\Ricerocks\missile.mp3")
missile_sound.set_volume(1)
ship_thrust_sound=simplegui.load_sound("F:\python\Game\Ricerocks\thrust.mp3")


#helper functions for handle the transformations
def angle_to_vector(ang):
    return[math.cos(ang),math.sin(ang)]



#Ship Class
class Ship:
    def __init__(self,pos,vel,angle,image,info):
        self.pos=[pos[0],pos[1]]
        self.vel=[vel[0],vel[1]]
        self.thrust=False
        self.angle=angle
        self.angle_vel=0
        self.image=image
        self.image_center=info.get_center()
        self.image_size=info.get_size()
        self.radius=info.get_radius()
        
        
    def draw(self,canvas):
        if self.thrust:
            canvas.draw_image(self.image,[self.image_center[0]+self.image_size[0],self.image_center[1]],
                             self.image_size,self.pos,self.image_size,self.angle)
            
        else:
            canvas.draw_image(self.image,self.image_center,self.image_size,
                              self.pos,self.image_size,self.angle)
     
    def update(self):
        # Update Angle
        self.angle +=self.angle_vel
        
        #Update Position
        self.pos[0]=(self.pos[0]+self.vel[0]) % WIDTH
        self.pos[1]=(self.pos[1]+self.vel[1]) % HEIGHT
        
        #Update Velocity
        if self.thrust:
            acc=angle_to_vector(self.angle)
            self.vel[0]+=acc[0]*0.25
            self.vel[1]+=acc[1]*0.25
       
        self.vel[0]*=0.96
        self.vel[1]*=0.96
        
    def vel_stop(self):
        self.vel[0]=0
        self.vel[1]=0
        
        
    def set_thrust(self,on):
        self.thrust=on
        if on:
            ship_thrust_sound.rewind()
            ship_thrust_sound.play()
        else:
            ship_thrust_sound.pause()
            
    def get_position(self):
        return self.pos
    
    def increment_angle_vel(self):
        self.angle_vel+=0.05
        
        
    def decrement_angle_vel(self):
        self.angle_vel-=0.05
        
        
    def shoot(self):
        #Global a missile
        global missile_group
        forward=angle_to_vector(self.angle)
        
        missile_pos=[self.pos[0]+self.radius*forward[0],self.pos[1]+self.radius*forward[1]]
        missile_vel=[self.vel[0]+6*forward[0],self.vel[1]+6*forward[1]]
        
        missile_group.add(Sprite(missile_pos,missile_vel,self.angle,0,missile_image,missile_info,missile_sound))
        
#Sprite Class

class Sprite():
    def __init__(self,pos,vel,ang,ang_vel,image,info,sound=None):
        self.pos=[pos[0],pos[1]]
        self.vel=[vel[0],vel[1]]
        self.thrust=False
        self.angle=ang
        self.angle_vel=ang_vel
        self.image=image
        self.image_center=info.get_center()
        self.image_size=info.get_size()
        self.radius=info.get_radius()
        self.lifespan = info.get_lifespan()
        self.animated = info.get_animated()

        self.age=0
        if sound:
            sound.rewind()
            sound.play()
            
            
    def draw(self,canvas):
        canvas.draw_image(self.image,self.image_center,self.image_size,
                              self.pos,self.image_size,self.angle)
        
    
    def get_position(self):
        return self.pos
    
    def update(self):
        # Update Angle
        self.angle +=self.angle_vel
        self.age+=1
        
        #Update Position
        self.pos[0]=(self.pos[0]+self.vel[0]) % WIDTH
        self.pos[1]=(self.pos[1]+self.vel[1]) % HEIGHT
            
        
        
    def collide(self,other_objects):
        global pos
        c1=self.get_position()
        c2=other_objects.get_position()
        if distance(c1,c2)<(self.radius+other_objects.radius):
            expos=c2
            return True
        else:
            return False
        

def gr_group_collide():
    global score
    remove_set=set([])
    rsm=set([])
    for ms in missile_group:
        for rck in rock_group:
            if rck.collide(ms):
                score+=10
                remove_set.add(rck)
                rsm.add(ms)
     
    
    if len(remove_set)>0:
        rock_group.difference_update(remove_set)
     
    if len(rsm)>0:
        missile_group.difference_update(rsm)

        
def group_collide():
    global lives,started,expl,expos,soundtrack
    remove_set = set([])
    for rck in rock_group:
        if rck.collide(my_ship):
            lives-=1
            expl=True
            if lives==0:
                started=False
                soundtrack.pause()
                remove_set=rock_group.copy()
            remove_set.add(rck)
    rock_group.difference_update(remove_set)
    
    
def distance(point1,point2):
    return math.sqrt((point1[0]-point2[0])**2+(point1[1]-point2[1])**2)


def keydown(key):
    if key == simplegui.KEY_MAP['left']:
        my_ship.decrement_angle_vel()
    elif key == simplegui.KEY_MAP['right']:
        my_ship.increment_angle_vel()
    elif key == simplegui.KEY_MAP['up']:
        my_ship.set_thrust(True)
    elif key == simplegui.KEY_MAP['down']:
        my_ship.vel_stop()
    elif key == simplegui.KEY_MAP['space']:
            my_ship.shoot()
    
    
            
def keyup(key):
    if key == simplegui.KEY_MAP['left']:
        my_ship.increment_angle_vel()
    elif key == simplegui.KEY_MAP['right']:
        my_ship.decrement_angle_vel()
    elif key == simplegui.KEY_MAP['up']:
        my_ship.set_thrust(False)

        

def click(pos):
    global started,lives,score
    lives=3
    score=0
    center=[WIDTH/2,HEIGHT/2]
    size=splash_info.get_size()
    inwidth=(center[0]-size[0]/2)< pos[0] < (center[0]+size[0]/2)
    inheight=(center[1]-size[1]/2)< pos[1] < (center[1]+size[1]/2)
    if (not started) and inwidth and inheight:
        started=True
        soundtrack.rewind()
        soundtrack.play()
    

def draw(canvas):
    global time,started,tim,expos,WIDTH,HEIGHT
    group_collide()
    gr_group_collide()
    #animated background
    time += 1
    wtime=(time/4) % WIDTH
    center = debris_info.get_center()
    size =debris_info.get_size()
    
#    canvas.draw_text("Helllo",[200,200],26,"Red","red")
    canvas.draw_image(nebula_image,nebula_info.get_center(),nebula_info.get_size(),[WIDTH/2,HEIGHT/2],[WIDTH,HEIGHT])
    canvas.draw_image(debris_image,center,size,(wtime-WIDTH/2,HEIGHT/2),(WIDTH, HEIGHT))
    canvas.draw_image(debris_image,center,size,(wtime+WIDTH/2,HEIGHT/2),(WIDTH, HEIGHT))
    
    #UI
    canvas.draw_text("Lives",[50,50],22,"White")
    canvas.draw_text("Score",[680,50],22,"White")
    canvas.draw_text(str(lives),[50,80],22,"White")
    canvas.draw_text(str(score),[680,80],22,"White")
    
    
    #Ship 
    my_ship.draw(canvas)
    
    #Rock
    for r in rock_group:
        r.draw(canvas)
        
    #missile
    for m in missile_group:
        remove_set = set([])
        m.draw(canvas)
        if m.age>m.lifespan:
            remove_set.add(m)
            missile_group.difference_update(rmst)
            missile_group.difference_update(remove_set)
    
    #update ship
    my_ship.update()
    
    #Update Rock
    for r in rock_group:
        r.update()
        
    #Update Missile
    for m in missile_group:
        m.update()
            
    #Splash Image
    if not started:
        canvas.draw_image(splash_image, splash_info.get_center(), 
                          splash_info.get_size(), [WIDTH / 2, HEIGHT / 2], 
                          splash_info.get_size())
        
def rock_spawner():
    global rock_group, started, score
    if started:
        rock_pos = [random.randrange(0, WIDTH), random.randrange(0, HEIGHT)]
        
        rock_vel = [random.randrange(-4,4) * .6 - .3, random.randrange(-4,4) * .6 - .3]
        
        if score>250:
            rock_vel[0]*=2
            rock_vel[1]*=2
            
        rock_avel = random.random() * .2 - .1
        
        if len(rock_group)<12:
            if distance(rock_pos,my_ship.pos)>100:
                rock_group.add(Sprite(rock_pos, rock_vel, 0, rock_avel, asteroid_image, asteroid_info))
                
                
frame = simplegui.create_frame("RICEROCKS", WIDTH, HEIGHT)


my_ship = Ship([WIDTH/2,HEIGHT/2],[0,0],0,ship_image,ship_info)
a_rock = Sprite([WIDTH/3,HEIGHT/3],[1,1],0,.1, asteroid_image,asteroid_info)
a_missile = Sprite([2*WIDTH/3,2*HEIGHT/3],[-1,1],0,0,missile_image, missile_info,missile_sound)


soundtrack.play()

frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.set_mouseclick_handler(click)

timer = simplegui.create_timer(1000, rock_spawner)

frame.start()
timer.start()
