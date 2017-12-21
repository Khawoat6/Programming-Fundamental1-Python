from tkinter import *
import random
import time

class Sheep():
    def __init__(self, canvas, v=3, direction='left'):
        self.point = 2
        self.images={'center': PhotoImage(file='whitesheep.gif'),
                     'left': PhotoImage(file='whitesheepleft.gif'),
                     'right': PhotoImage(file='whitesheepright.gif')}
        self.v = v
        self.direction = direction
        self.canvas = canvas
        self.x = random.randint(0, 400-32)
        self.canvas_id = canvas.create_image(self.x, 300, anchor=SW, image=self.images[self.direction])

    def move(self):
        if self.direction == 'left':
            self.x -= self.v
            self.canvas.move(self.canvas_id, -self.v, 0)
            if self.x <= 0:
                self.direction = 'right'
                self.canvas.itemconfig(self.canvas_id, image=self.images[self.direction])
        elif self.direction == 'right':
            self.x += self.v
            self.canvas.move(self.canvas_id, self.v, 0)
            if self.x >= 400-32:
                self.direction = 'left'
                self.canvas.itemconfig(self.canvas_id, image=self.images[self.direction])

class BlackSheep(Sheep):
    def __init__(self, canvas, v=3, direction='left'):
        Sheep.__init__(self, canvas, v, direction)
        self.point = -10
        self.images={'center': PhotoImage(file='blacksheep.gif'),
                     'left': PhotoImage(file='blacksheepleft.gif'),
                     'right':PhotoImage(file='blacksheepright.gif')}
        self.canvas.itemconfig(self.canvas_id, image=self.images[self.direction])

class Dog:
    def __init__(self, canvas):
        self.canvas = canvas
        self.images={'left':PhotoImage(file='dogleft.gif'),
                     'right':PhotoImage(file='dogright.gif')}
        self.direction='right'
        self.x = 0
        self.y = 300
        self.vx = 0
        self.vy=0
        self.canvas_id = canvas.create_image(self.x, self.y, anchor=SW,
                                             image=self.images[self.direction])

    def move(self):
        self.canvas.move(self.canvas_id, self.vx, -self.vy)
        self.y -= self.vy
        if self.y > 300:
            self.canvas.move(self.canvas_id, 0, 300 - self.y)
        if self.y < 300:
            self.vy -= 1
        else:
            self.vy = 0
            self.y = 300
            
        self.x += self.vx
        if self.vx > 0 and self.direction == 'left':
            self.direction = 'right'
            self.canvas.itemconfig(self.canvas_id,
                                   image=self.images[self.direction])
        elif self.vx < 0 and self.direction == 'right':
            self.direction = 'left'
            self.canvas.itemconfig(self.canvas_id,
                                   image=self.images[self.direction])
        
        

tk = Tk()
canvas = Canvas(tk, width=400, height=400)
canvas.pack()
canvas.create_rectangle(0, 0, 400, 300, fill='blue')
canvas.create_rectangle(0, 300, 400, 400, fill='brown')
##sheeps = []
##for i in range(10):
##    sheeps.append(random.choice([Sheep(canvas),
##                                 Sheep(canvas, 0, 'center'),
##                                 Sheep(canvas, 1, 'right'),
##                                 Sheep(canvas, 2, 'left'),
##                                 Sheep(canvas, 1, 'left'),
##                                 Sheep(canvas, 2, 'right'),
##                                 BlackSheep(canvas),
##                                 BlackSheep(canvas, 0, 'center'),
##                                 BlackSheep(canvas,1,'right')]))
##
dog = Dog(canvas)
def move_dog(event):
    if event.keysym =='Left':
        dog.vx = -3
    elif event.keysym == 'Right':
        dog.vx = 3
    elif event.keysym == 'space':
        dog.vy = 10

canvas.bind_all('<KeyPress-Left>', move_dog)
canvas.bind_all('<KeyPress-Right>', move_dog)
canvas.bind_all('<KeyPress-space>', move_dog)
##score = 0
while True:
    for sheep in sheeps:
        sheep.move()
    dog.move()
    tk.update()
    time.sleep(0.05)
