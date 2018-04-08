#Example of various Shapes
import simplegui
def color(i):
    frame.set_canvas_background(i)
def draw(canvas):
    canvas.draw_circle([125,125],44,2,"gray","blue")
    canvas.draw_circle([375,375],44,2,"gray","purple")
    canvas.draw_polyline([[125,125],[375,375]],2,"white")
    canvas.draw_circle([375,125],44,2,"gray","orange")
    canvas.draw_circle([125,375],44,2,"gray","green")
    canvas.draw_polyline([[125,375],[375,125]],2,"white")
    canvas.draw_polygon([[200,200],[200,300],[300,300],[300,200]],2,"yellow","red")
frame=simplegui.create_frame("My Shapes",500,500)
frame.add_input("Enter Color",color,50)
frame.set_draw_handler(draw)
frame.start()


