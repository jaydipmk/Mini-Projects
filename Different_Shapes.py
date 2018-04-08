#Example For Differnt Shapes
import simplegui
def draw(canvas):
    canvas.draw_circle([50,50],25,2,"Red","blue")
    canvas.draw_polygon([[70,100],[70,150],[145,125],[85,125]],2,"red","aqua")
    canvas.draw_polygon([[275,275],[250,325],[275,375],[350,375],[375,325],[350,275]],2,"orange","teal")
    canvas.draw_polygon([[250,25],[300,25],[300,125],[250,125]],2,"white","blue")
    canvas.draw_polygon([[25,175],[75,175],[75,225],[25,225]],2,"yellow","green")
    canvas.draw_polygon([[175,25],[150,100],[200,100]],2,"orange","purple")
    canvas.draw_polygon([[100,175],[150,175],[125,250]],2,"yellow","blue")
    canvas.draw_polygon([[170,170],[200,225],[300,225],[263,170]],2,"white","gray")
    canvas.draw_polygon([[105,275],[50,325],[75,375],[150,375],[175,320]],2,"gray","white")
frame=simplegui.create_frame("Differnt_Shapes",375,450)
frame.set_draw_handler(draw)
frame.start()
