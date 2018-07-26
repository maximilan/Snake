Width = 200
snakethick = 4
rows = Width / snakethick
current_key = "Right"
game = True


class Point():
    def __init__(self, x, y, fill = 'green'):
        self.x = x
        self.y = y
        self.fill = fill
        self.counter = 1
    def draw(self):
        '''if self.counter < 6:
            self.counter += 1
            c.create_rectangle(self.x, self.y, self.x + snakethick, self.y + snakethick, fill = 'black', outline = 'black')
        else:'''
        c.create_rectangle(self.x, self.y, self.x + snakethick, self.y + snakethick, fill = self.fill, outline = self.fill)
    def add(self, x, y):
        return Point(self.x + x, self.y + y)
    def return_coords(self):
        return self.x, self.y
    def equals(self, p):
        x, y = p.return_coords()
        if x == self.x and y == self.y:
            return True
        else:
            return False

class Item():
    def __init__(self):
        self.point = Point(randint(1, rows -1 ) * snakethick, randint(1, rows -1) * snakethick, 'red')
    def show(self):
        self.point.draw()
    def return_point(self):
        return self.point

class Snake():
    def __init__(self):
        self.length = 2
        self.counter = 0
        self.body = list()
        self.body.append(Point(snakethick*2, snakethick))
        self.body.append(self.body[0].add(-snakethick, 0))
        self.head = self.body[0]
        self.prevhead = self.body[0]

    def update(self):
        global item
        global current_key
        global game
        global Width
        change = (self.counter % self.length)
        print(change)
        new = self.head
        #print(self.body[change])
        if current_key == "Up":
            self.body[change] = new.add(0, -snakethick)
        elif current_key == "Down":
            self.body[change] = new.add(0, snakethick)
        elif current_key == "Right":
            self.body[change] = new.add(snakethick, 0)
        elif current_key == "Left":
            self.body[change] = new.add(-snakethick, 0)
        self.prevhead = self.head
        self.head = self.body[change]
        self.counter += 1
        #Überprüfen, ob Schlange gegen sich selbst fährt
        for point in self.body:
            if point != None:
                if point == self.head:
                    continue
                else:
                    if point.return_coords() == self.head.return_coords():
                        print(point.return_coords())
                        print(self.head.return_coords())
                        game = False
        #Punkte erscheinen lassen und Gegenstände fressen
        for point in self.body:
            if point != None:
                point.draw()
                if point.equals(item.return_point()):
                    self.grow()
                    item = Item()
                #Überprüfen, ob Schlange den Rand erreicht hat
                x, y = point.return_coords()
                if x <= 0 or x >= Width or y <= 0 or y >= Width:
                    game = False

    def grow(self):
        old = (self.counter % self.length)
        self.length += 1
        self.counter = 1
        while (self.counter % self.length) != old:
            self.counter += 1
        self.body.append(None)
        
    def return_body(self):
        return self.body

from tkinter import *
from time import sleep
from random import randint

root = Tk()
c = Canvas(width = Width, height = Width, bg = 'white')
c.pack()
snake = Snake()
item = Item()

def movement(event):
    global current_key
    current_key = str(event.keysym)
c.bind_all('<Key>', movement)

def show():
    global Width
    c.delete("all")
    c.create_rectangle(0, 0, Width + 100, Width + 100, fill = 'black', outline = 'black')
    #c.create_rectangle(snakethick, snakethick, Width - snakethick, Width - snakethick, fill = 'white', outline = 'white')
    snake.update()
    item.show()
    root.update()
    sleep(0.1)

while game:
    show()
