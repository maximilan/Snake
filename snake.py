Width = 400
snakethick = 8
rows = Width / snakethick
current_key = "Right"
game = True
running = True
start = True
current_direction = None


class Point():
    def __init__(self, x, y, fill = 'green'):
        self.x = x
        self.y = y
        self.fill = fill
        self.counter = 1

    def draw(self):
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
        global current_direction
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
        current_direction = current_key
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
import tkinter as tk
from time import sleep
from random import randint
def close_window():
    global running
    running = False
    global game
    game = False
    root.destroy()

root = Tk()
root.title = "Snake"
root.protocol("WM_DELETE_WINDOW", close_window)
c = Canvas(width = Width, height = Width, bg = 'white')
c.pack()
snake = Snake()
item = Item()

def movement(event):
    global current_key
    if str(event.keysym) in ("Right", "Left", "Up", "Down"):
        if current_direction == "Right" and str(event.keysym) == "Left" or current_direction == "Left" and str(event.keysym) == "Right":
            None
        elif current_direction == "Up" and str(event.keysym) == "Down" or current_direction == "Down" and str(event.keysym) == "Up":
            None
        else:
            current_key = str(event.keysym)
c.bind_all('<Key>', movement)

def show():
    global Width
    c.delete("all")
    c.create_rectangle(0, 0, Width + 100, Width + 100, fill = 'black', outline = 'black')
    snake.update()
    item.show()
    root.update()
    sleep(0.1)

def start_game():
    global start
    start = False

def init():
    global start
    start = True
    c.create_rectangle(0, 0, Width + 100, Width + 100, fill = 'black', outline = 'black')
    c.create_text(Width/2, Width/2 - 50, text = "Snake", font=('Lato Black', 50), fill = 'white')
    c.create_text(Width/2, Width/2 + 20, text = "A production of HERFARTH Enterprises", font=('Lato Black', 10), fill = 'white')
    B = tk.Button(root, text="Neues Spiel", command = start_game)
    B.pack(side = LEFT)
    while start:
        if running = False:
            break
        root.update()
    B.destroy()
    start = True

def gameover():
    c.create_text(Width/2, Width/2 -50, text = "Game over", font=('Lato Black', 60), fill = 'white')
    c.create_text(Width/2, Width/2+30, text = "Points: " + str(len(snake.return_body())), font=('Lato Black', 30), fill = 'white')
    root.update()
    sleep(5)
    if running = False:
        break
    c.delete("all")


while running:
    init()

    while game:
        show()

    gameover()
