##class Dog:
##    def __init__(self, canvas):
##        self.canvas = canvas
##        self.images={'left':PhotoImage(file='dogleft.gif'),
##                     'right':PhotoImage(file='dogright.gif')}
##        self.direction='right'
##        self.x = 0
##        self.y = 300
##        self.vx = 0
##        self.vy=0
##        self.canvas_id = canvas.create_image(self.x, self.y, anchor=SW,
##                                             image=self.images[self.direction])
##
##    def move(self):
##        self.canvas.move(self.canvas_id, self.vx, -self.vy)
##        self.y -= self.vy
##        if self.y > 300:
##            self.canvas.move(self.canvas_id, 0, 300 - self.y)
##        if self.y < 300:
##            self.vy -= 1
##        else:
##            self.vy = 0
##            self.y = 300
##
##        self.x += self.vx
##        if self.vx > 0 and self.direction == 'left':
##            self.direction = 'right'
##            self.canvas.itemconfig(self.canvas_id,
##                                   image=self.images[self.direction])
##            elif self.vx < 0 and self.direction == 'right':
##                self.direction = 'left'
##                self.canvas.itemconfig(self.canvas_id,
##                                       image=self.images[self.direction])

##class Dog:
##    def __init__(self, canvas):
##        self.canvas = canvas
##        self.images={'left':PhotoImage(file='dogleft.gif'),
##                     'right':PhotoImage(file='dogright.gif')}
##        self.direction='right'
##        self.x = 0
##        self.y = 300
##        self.vx = 0
##        self.vy=0
##        self.canvas_id = canvas.create_image(self.x, self.y, anchor=SW,
##                                             image=self.images[self.direction]
##
##
##    def move(self):
##        self.canvas.move(self.canvas_id, self.vx, -self.vy)
##        self.y -= self.vy
##        if self.y > 300:
##            self.canvas.move(self.canvas_id, 0, 300 - self.y)
##        if self.y < 300:
##            self.vy -= 1
##        else:
##            self.vy = 0
##            self.y = 300
##
##        self.x += self.vx
##        if self.vx > 0 and self.direction == 'left':
##            self.direction = 'right'
##            self.canvas.itemconfig(self.canvas_id,
##                                   image=self.images[self.direction])
##        elif self.vx < 0 and self.direction == 'right':
##            self.direction = 'left'
##            self.canvas.itemconfig(self.canvas_id,
##                                   image=self.images[self.direction])
##
##dog = Dog(canvas)

class Dog:
    def __init__(self, canvas):
        self.canvas = canvas
        self.image={'left':PhotoImage(file='dogleft.gif')
                    'right':hotoImage(file='dogleft.gif')}
        self.direction='right'
        self.x = 0
        self.y = 300
        self.vx = 0
        self.vy=0
        self.canvas_id = canvas.create_image(self.x,self.y, anchor=SW,
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


while True:
    for sheep in sheeps:
        sheep.move()
    dog.move()
    tk.update()
    time.sleep(0.03)


























                                             
                                             



