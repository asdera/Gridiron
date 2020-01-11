from tkinter import *
from time import *
from math import *
from time import *
from random import *
tk = Tk()
s = Canvas(tk, width=800,height=600, background="seagreen")
s.pack()

         #USER INPUT#  
##############################
colour="cornflowerblue"      #
colour2="white"              #
teamName="Baltimore Ravens"  #
##############################

#stands
s.create_rectangle(0,1,810,450, fill="grey", outline="grey")
s.create_polygon(85,400,95,400,-10,150,-14,150)
s.create_polygon(350,400,360,400,360,150,352,150)
s.create_polygon(650,400,660,400,660,150,652,150)

s.create_rectangle(95,400,812,470, fill="slategrey", outline="slategrey")
s.create_polygon(100,435,-10,480, fill="slategrey", outline="slategrey", width=70)
s.create_rectangle(95,410,812,460,fill=colour, outline=colour)
#s.create_text(220, 435, fill="black", font="helvetica 20 bold", text=teamName)


s.create_rectangle(0,0,800,100,fill=colour, outline=colour)

##Lines
#Vertical Lines
s.create_rectangle(0,700,812,710, fill="white", outline="white")
s.create_rectangle(200,500,812,502, fill="white", outline="white")
#Horizontal Lines
s.create_polygon(700,700,710,700,682,500,680,500, fill="white", outline="white")
s.create_polygon(-50,700,-60,700,200,500,200,502, fill="white", outline="white")
s.create_polygon(900,700,900,700,798,500,795,500, fill="white", outline="white")
#Orange Cones
s.create_rectangle(706,698,690,648, fill="sandybrown",outline="sandybrown")
s.create_rectangle(706,700,692,650, fill="darkorange",outline="darkorange")

s.create_rectangle(680,484,674,504, fill="darkorange",outline="darkorange")
s.create_rectangle(680,485,675,505, fill="darkorange",outline="darkorange")


s.create_rectangle(680,484,674,504, fill="darkorange",outline="darkorange")
s.create_rectangle(200,485,206,505, fill="darkorange",outline="darkorange")


#Uprights
s.create_rectangle(50,580,100,470, fill="grey", outline="grey")
s.create_oval(50,460,100,480,fill="grey")
s.create_oval(50,590,100,570, fill="grey",outline="grey")

s.create_rectangle(68,470,83,400,fill="khaki", outline="khaki")
s.create_polygon(10,450,150,350, fill="khaki",outline="khaki", width=15)
s.create_polygon(150,350,150,220, fill="khaki",outline="khaki",width=15)
s.create_polygon(10,450,10,320, fill="khaki",outline="khaki",width=15)


 



