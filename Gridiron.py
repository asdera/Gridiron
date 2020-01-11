from tkinter import *
from time import *
from math import *
from time import *
from random import *

root = Tk()
s = Canvas(root, width=800,height=600, background="green")
s.pack()


def menu():
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
  s.create_text(400, 100, fill="white", font=('Comic Sans MS', 48), text="GRIDIRON")
  s.create_text(400, 340, fill="white", font=('Comic Sans MS', 24), text="Click up here to start")
  s.create_text(400, 470, fill="white", font=('Comic Sans MS', 24), text="Instructions")
  s.create_text(400, 520, fill="white", font=('Comic Sans MS', 24), text="Credits")


def field():
                #USER INPUT#  
    ##############################
    colour="cornflowerblue"      #
    colour2="white"              #
    teamName="Baltimore Ravens"  #
    ##############################

    stuff = []

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

    instructions()


def mouseDown(event):
    global play
    if play:
        ball[2] = event.x
        ball[3] = event.y
    play = False

def hut():
    a = s.create_text(400, 200, anchor="center", fill="black", text="READY", font = ('Comic Sans MS', 40))
    s.update()
    sleep(1)
    s.delete(a)
    a = s.create_text(400, 200, anchor="center", fill="black", text="SET", font = ('Comic Sans MS', 40))
    s.update()
    sleep(1)
    s.delete(a)
    a = s.create_text(400, 200, anchor="center", fill="black", text="HUT", font = ('Comic Sans MS', 40))
    s.update()
    sleep(1)
    s.delete(a)

def drawObjects():
    global cooldown, arrow, score, downs, ball, velX, velY, players, n, play, tk, reset, run
    tk.append(s.create_text(15, 500, anchor="w", fill="white", text=score, font = ('Comic Sans MS', 12)))

    for i in range(1, 21):
        tk.append(s.create_line(0,  500-i*25,  10,  500-i*25, fill="white"))
        if (score+i) % 5 == 0:
            tk.append(s.create_text(15, 500-i*25, anchor="w", fill="white", text=score+i, font = ('Comic Sans MS', 12)))

    for p in players:
        if p[4] == "wr":
            c = "red"
            tk.append(s.create_line(p[0], p[1], p[2], p[3], fill="#0BA62E"))
        elif p[4] == "lb":
            c = "purple"
        else:
            c = "blue"
    
        tk.append(s.create_oval(p[0]-12,  p[1]-12,  p[0]+12,  p[1]+12, fill=c))
        tk.append(s.create_rectangle(p[0]-3,  p[1]-10,  p[0]+3,  p[1]+10, fill="white", width=0))
        

    tk.append(s.create_oval(ball[0]-5, ball[1]-5, ball[0]+5, ball[1]+5, fill="brown"))
    tk.append(s.create_line(ball[0], ball[1], ball[2], ball[3], fill="white"))

    if ball[1] < -100:
        tk.append(s.create_text(400, 200, anchor="center", fill="black", text="!TOUCHDOWN!", font = ('Comic Sans MS', 40)))

    for i in range(downs):
        tk.append(s.create_oval(790-i*20-5, 500-5, 790-i*20+5, 500+5, fill="brown"))

def updateObjects():
    global cooldown, arrow, score, downs, ball, velX, velY, players, n, play, tk, reset, run
    if run:
        ball[1] -= 2
    else:
        ball[0] = ball[0] + (ball[2] - ball[0]) / 20
        ball[1] = ball[1] + (ball[3] - ball[1]) / 20

    if ball[1] < -100:
        if reset == 0:
            score += int((500-ball[1])/15) 
            reset = 60

    for p in players:
            
        if run and p[4] == "wr":
            p[1] -= 2
        else:
            p[0] = p[0] + (p[2] - p[0]) / 40
            p[1] = p[1] + (p[3] - p[1]) / 40

        if p[4] == "lb":
            p[2] = ball[2]
            p[3] = ball[1]
        elif run and p[4] == "wr":
            p[2] = p[0]
            p[3] = 0
        elif run and p[4] == "db":
            p[2] = ball[2]
            p[3] = ball[1]-60
            
        elif abs(p[2] - p[0]) < 100 and abs(p[3] - p[1]) < 100:
            p[2] = randint(-50, 850)
            p[3] = randint(-50, 540)

        if sqrt((p[0]-ball[0])**2 + (p[1]-ball[1])**2) < 17:
            if p[4] == "wr":
                p[2] = p[0]
                p[3] = p[1]
                ball[0] = p[0]
                ball[1] = p[1]
                ball[2] = p[0]
                ball[3] = p[1]
                run = True
                
            elif reset == 0:
                ball[2] = ball[0]
                ball[3] = ball[1]
                if run:
                    score += int((500-ball[1])/25)
                else:
                    downs -= 1
                    score += min(int((500-ball[1])/25), 0)
                reset = 20


def setInitialValues():
    global cooldown, arrow, score, downs, ball, velX, velY, players, n, play, tk, reset, run

    ball = [400, 550, 400, 550]
    velX = 0
    velY = 0
    players = []
    n = 20
    play = True
    run = False

    for i in range(n):
        x = randint(0, 800)
        x2 = randint(-50, 850)
        y2 = randint(-50, 540)
        if i % 2:
            t = "wr"
            y = 500
        else:
            t = "db"
            y = 450
        players.append([x, y, x2, y2, t])
    
    x = randint(0, 800)
    y = 200
    x2 = randint(-50, 850)
    y2 = randint(-50, 540)
    t = "lb"
    players.append([x, y, x2, y2, t])


def runGame(): 
    global cooldown, arrow, score, downs, ball, velX, velY, players, n, play, tk, reset, run

    score = 0
    downs = 4
    reset = 0

    setInitialValues()

    # field()
    s.create_line(0, 500, 800, 500, fill="pink")
    s.create_oval(ball[0]-12, ball[1]-12, ball[0]+12, ball[1]+12, fill="orange")
    s.create_rectangle(ball[0]-3,  ball[1]-10,  ball[0]+3,  ball[1]+10, fill="white", width=0)
    s.create_text(30, 550, anchor="w", fill="white", text="Yards", font = ('Comic Sans MS', 15))
    s.create_text(770, 550, anchor="e", fill="white", text="Downs", font = ('Comic Sans MS', 15))

    tk = []
    drawObjects()
    hut()
    while True:
        
        if reset > 0:
            if reset == 1:
                if downs == 0:
                  break
                setInitialValues()
                for poo in tk:
                    s.delete( poo )
                del tk[:]
                drawObjects()
                hut()
            reset -= 1
            

        drawObjects()
        
        s.update()
        sleep(0.03)

        updateObjects()

        for poo in tk:
            s.delete( poo )
        del tk[:]
    s.create_text(400, 200, anchor="center", fill="black", text="You ran "+str(score)+" yards!", font = ('Comic Sans MS', 40))
    s.create_text(400, 300, anchor="center", fill="black", text="So Elite!", font = ('Comic Sans MS', 40))
    s.update()
    sleep(6)
    s.delete("all")
    menu()
    s.bind( "<Button-1>", mouseClickDetector )   

#Rain Intro
x = []
y = []
RainDrawings = []
numRain = 50

for i in range(numRain):
    x.append( randint(0,700))
    y.append( randint(0,800 ))
    RainDrawings.append( 0 )

#CLICKING ANIMATION
def mouseClickDetector( event ):
    xMouse = event.x
    yMouse = event.y

    if yMouse < 440:
      s.bind( "<Button-1>", mouseDown )
      s.delete("all")

      runGame()
    else:
      s.delete("all")
      field()
      s.update()
      sleep(6)
      s.delete("all")
      menu()
      s.update()

def instructions():
    s.create_text(400, 50, fill="black", font=('Comic Sans MS', 24), text="Instructions and Credits")
    s.create_text(200, 120, fill="black", font=('Comic Sans MS', 12), text="Click anywhere on the screen to throw the ball")
    s.create_text(200, 150, fill="black", font=('Comic Sans MS', 12), text="You are the quarterback!")
    s.create_text(200, 180, fill="black", font=('Comic Sans MS', 12), text="Pass the ball to the receivers in red")
    s.create_text(200, 210, fill="black", font=('Comic Sans MS', 12), text="Avoid getting intercepted")
    s.create_text(200, 240, fill="black", font=('Comic Sans MS', 12), text="by the defensive backs in blue")
    s.create_text(200, 270, fill="black", font=('Comic Sans MS', 12), text="Throw quickly before you get sacked") 
    s.create_text(200, 300, fill="black", font=('Comic Sans MS', 12), text="by the tackler in purple")
    s.create_text(200, 330, fill="black", font=('Comic Sans MS', 12), text="You have four downs to gain")
    s.create_text(200, 360, fill="black", font=('Comic Sans MS', 12), text="as many yards as you can")
    s.create_text(510, 120, fill="black", font=('Comic Sans MS', 12), text="Big thanks to you for playing")
    s.create_text(510, 150, fill="black", font=('Comic Sans MS', 12), text="Big thanks to my CS teacher")
    s.create_text(510, 180, fill="black", font=('Comic Sans MS', 12), text="Big thanks to my mom and dad")
    s.create_text(510, 210, fill="black", font=('Comic Sans MS', 12), text="Big thanks to Mama Reshma")
    s.create_text(510, 240, fill="black", font=('Comic Sans MS', 12), text="Big thanks to SJAM football")
    s.create_text(510, 270, fill="black", font=('Comic Sans MS', 12), text="Big thanks to the asians")
    s.create_text(510, 300, fill="black", font=('Comic Sans MS', 12), text="Big thanks to my dog")
    s.create_text(510, 330, fill="black", font=('Comic Sans MS', 12), text="Big thanks to my brother")
    s.create_text(510, 360, fill="black", font=('Comic Sans MS', 12), text="Made by the one and only")


def runIntro():
    menu()
    while True:
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


root.after( 0, runIntro )

s.bind( "<Button-1>", mouseClickDetector )                                                
                                          
s.focus_set() 
s.pack()
root.mainloop()
