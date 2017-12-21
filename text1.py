import turtle
import os
import math
import random
from tkinter import *




#Move left and right
def m_l():
    x = p.xcor()
    if x < -280:
        x = -280
    x -= pspeed
    p.setx(x)
def m_r():
    x = p.xcor()
    if x > 280:
        x = 280
    x += pspeed
    p.setx(x)
def f_b():
    global bustate
    if bustate == "ready":
        bustate = "fire"
        #move bullet
        x = p.xcor()
        y = p.ycor() +10
        bu.setposition(x,y)
        bu.showturtle()
# bullet att. enemy
def isCollision(t1,t2):
    distance = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2)+math.pow(t1.ycor()-t2.ycor(),2))
    if distance < 15:
        return True
    else:
        return False

    
#Screen
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Sheep Invaders")

#Border
bd_pen = turtle.Turtle()
bd_pen.speed(0)
bd_pen.color("white")
bd_pen.penup()
bd_pen.setposition(-300,-300)
bd_pen.pendown()
bd_pen.pensize(3)
for s in range(4):
    bd_pen.fd(600)
    bd_pen.lt(90)
bd_pen.hideturtle()

#Shooter(player)
p = turtle.Turtle()
p.color("green")
p.shape("triangle")
p.penup()
p.speed(0)
p.setposition(0,-200)
p.setheading(90)

pspeed = 15

#Choose a number of enemies
ne= 5
#Create an empty list of enemies
enemies = []

#Add enemies to the list
for i in range(ne):
    #create enemy
    enemies.append(turtle.Turtle())
    
for e in enemies:
    #Enemy
    e.color("white")
    e.shape("circle")
    e.penup()
    e.speed(0)
    x = random.randint(-200,200)
    y = random.randint(100,250)
    e.setposition(x,y)

espeed = 2

#shooter bullet
bu = turtle.Turtle()
bu.color("yellow")
bu.shape("triangle")
bu.penup()
bu.speed(0)
bu.setheading(90)
bu.shapesize(0.5,0.5)
bu.hideturtle()

buspeed = 20       

#Define bullet state
bustate = "ready"


#keyboard
turtle.listen()
turtle.onkey(m_l,"Left")
turtle.onkey(m_r,"Right")
turtle.onkey(f_b,"space")





#Game loop
while True:
    for e in enemies:
        #Move back and down Enemy
        x = e.xcor()
        x += espeed
        e.setx(x)
        if e.xcor() > 280:
            y = e.ycor()
            y -= 40
            espeed *= -1
            e.sety(y)
            
        if e.xcor() < -280:
            y = e.ycor()
            y -= 40
            espeed *= -1
            e.sety(y)
        #Check for a collision between bullet and enemy
        if isCollision(bu,e):
            #reset bullet
            bu.hideturtle()
            bustate = "ready"
            bu.setposition(0,-400)
            #reset enemy
            x = random.randint(-200,200)
            y = random.randint(100,250)
            e.setposition(x,y)
        #Game end
        if isCollision(p,e):
            p.hideturtle()
            e.hideturtle()
            print("Game Over")
            break


    #Move bullet
    if bustate == "fire":
        y = bu.ycor()
        y += buspeed
        bu.sety(y)

    #Check bullet to top
    if bu.ycor() > 275:
        bu.hideturtle()
        bustate = "ready"




delay = input("Press enter to finish.")
