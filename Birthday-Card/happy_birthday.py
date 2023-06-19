from turtle import *
import turtle
from random import randint
import random


pen = turtle.Turtle()
pen.speed("fastest")
s = turtle.Screen()
s.setup(width=1000, height=700)

colormode(255)

global colors

colors = ["red", "blue", "yellow", "green", "lightgreen", "purple", "pink"]

global rand_colors

def text():

    pen.penup()

    pen.home()

    pen.color('black')

    pen.pendown()


    style = ('Courier', 20, 'normal')
    pen.write('Happy Birthday!', font=style, align='center')
    pen.hideturtle()

def cake():

    pen.begin_fill()

    pen.fd(100)
    pen.rt(90)
    pen.fd(50)
    pen.rt(90)
    pen.fd(100)
    pen.rt(90)
    pen.fd(50)

    pen.end_fill()

    for i in range(4):

        rand_colors = random.choice(colors)

        pen.color(rand_colors)


        pen.up()

        pen.fd(10)

        pen.down()

        pen.fd(30)

        pen.up()

        pen.fd(5)

        pen.down()

        pen.color("yellow")

        pen.fd(6)

        pen.up()

        pen.back(51)

        pen.rt(90)

        pen.fd(30)

        pen.lt(90)

def party_hat():

    pen.begin_fill()

    for i in range(3):

        pen.fd(100)

        pen.rt(120)

    pen.end_fill()

    rand_colors = random.choice(colors)

    pen.color(rand_colors)

    pen.up()

    pen.rt(90)

    pen.fd(6)

    pen.lt(90)

    pen.down()

    pen.begin_fill()

    pen.circle(6)

    pen.end_fill()

for i in range(10):

    pen.color(randint(0, 255),
              randint(0, 255),
              randint(0, 255))

    pen.penup()

    pen.goto(randint(-500, 500), randint(-300, 270))

    pen.pendown()

    cake()

    pen.color(randint(0, 255),
              randint(0, 255),
              randint(0, 255))

    pen.penup()

    pen.goto(randint(-500, 500), randint(-300, 270))

    pen.pendown()

    party_hat()

text()

while True:
    s.update()
