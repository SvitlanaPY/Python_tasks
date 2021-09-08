import turtle
import tkinter

def move(length):
    turtle.forward(length)   # length - storona kvadrata
    turtle.left(90)   # kyt

def drawSquare(length):
    for i in range(4):
        move(length)

def drawSquareColor(length, color):
    turtle.color(color)
    turtle.begin_fill()
    drawSquare(length)
    turtle.end_fill()


turtle.speed(1)
drawSquareColor(60, 'red')
turtle.goto(100, 100)
drawSquareColor(120, 'blue')

