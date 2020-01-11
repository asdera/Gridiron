from tkinter import *
from time import *
from math import *
from time import *
from random import *
tk = Tk()
s = Canvas(tk, width=800,height=600, background="lightslategrey")
s.pack()

def mouseClickDetector( event ):
   xMouse = event.x
   yMouse = event.y

   print("You clicked at (" + str( xMouse ) + ", " + str( yMouse ) + ")")

   screen.create_oval( xMouse - 10, yMouse - 10, xMouse + 10, yMouse + 10, fill = "tomato")


#---------------------Football Procedures-----------------------------------#
s.create_rectangle(0,0,800,265, fill="cornflowerblue",outline="cornflowerblue")
#Goal Post
s.create_rectangle(0,400,800,800, fill="seagreen", outline="seagreen")
s.create_rectangle(375,400,425,300, fill="slategrey", outline="slategrey")
s.create_rectangle(390,300,410,200, fill="khaki", outline="khaki")
s.create_rectangle(100,190,700,210, fill="khaki", outline="khaki")
s.create_rectangle(100,190,120,-100, fill="khaki", outline="khaki")
s.create_rectangle(700,190,680,-100, fill="khaki", outline="khaki")

#Football
s.create_oval(425,380,475,400, fill="peru", outline="peru")
s.create_rectangle(435,381,436,390, fill="darkgrey", outline="darkgrey")
s.create_rectangle(465,381,464,390, fill="darkgrey", outline="darkgrey")
s.create_rectangle(450,380,451,385, fill="lightgrey", outline="lightgrey")
s.create_rectangle(445,380,446,385, fill="lightgrey", outline="lightgrey")
s.create_rectangle(455,380,456,385, fill="lightgrey", outline="lightgrey")
s.create_rectangle(460,381,461,385, fill="lightgrey", outline="lightgrey")
s.create_rectangle(440,381,441,385, fill="lightgrey", outline="lightgrey")

#Text
s.create_text(400, 415, fill="white", font="Times 20 bold", text="GRIDIRON")
s.create_text(400, 445, fill="white", font="Times 12 bold", text="Start")
s.create_text(400, 470, fill="white", font="Times 12 bold", text="Settings")
s.create_text(400, 495, fill="white", font="Times 12 bold", text="Credits")
s.create_text(400, 520, fill="white", font="Times 12 bold", text="Help")

#Rain Intro
x = []
y = []
RainDrawings = []
numRain = 50

for i in range(numRain):
    x.append( randint(0,700))
    y.append( randint(0,800 ))
    RainDrawings.append( 0 )


for f in range(5000000):


    for i in range(numRain):
        RainDrawings[i] = s.create_line(x[i], y[i], x[i]+8, y[i]+25, fill="blue")
        y[i] = y[i] + 5
        x[i] = x[i] + 2
        if y[i] > 800:
            y[i] = -10
            x[i] = randint(-20,700)
    s.update()


    for i in range(numRain):
        s.delete( RainDrawings[i] )


#CLICKING ANIMATION
def mouseClickDetector( event ):
   xMouse = event.x
   yMouse = event.y

   print("You clicked at (" + str( xMouse ) + ", " + str( yMouse ) + ")")

   screen.create_oval( xMouse - 10, yMouse - 10, xMouse + 10, yMouse + 10, fill = "tomato")

s.bind( "<Button-1>", mouseClickDetector )                                                

s.bind( "<Key>", keyPressDetector )                                          

s.bind( "<Motion>", mouseMotionDetector)                                               

s.focus_set() 
s.pack()
root.mainloop()
