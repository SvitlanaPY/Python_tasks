import turtle
import tkinter

def move(length):
    turtle.forward(length)   # length - storona kvadrata
    turtle.left(90)   # kyt

def drawSquare(length):
    for i in range(4):
        move(length)


turtle.speed(1)
drawSquare(60)
turtle.goto(100, 100)
drawSquare(120)

