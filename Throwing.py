from tkinter import *
from time import *
from math import *
from time import *
from random import *
tk = Tk()
s = Canvas(tk, width=800,height=600, background="seagreen")
s.pack()

#Background

Footballplayer=PhotoImage(file="footballplayer.gif")
s.create_image(300,300, image = Footballplayer)

