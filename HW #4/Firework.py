from turtle import *
import random

speed(0)
delay(0)
tracer(False)
bgcolor('black')

def rightLine():
    for i in range(1,10):
        pensize((i/2) * scale)
        pencolor(red_amount, green_amount-(i/20), blue_amount)
        pendown()
        forward(random.randint(1,12) * scale)
        right(2)
        penup()
        forward(random.randint(1,8) * scale)
        right(3)

def leftLine():
    for i in range(1,10):
        pensize((i/2) * scale)
        pencolor(red_amount, green_amount-(i/20), blue_amount)
        pendown()
        forward(random.randint(2,12) * scale)
        left(2)
        penup()
        forward(random.randint(2,8) * scale)
        left(3)

def firework():
    origin = pos()
    global scale
    scale = random.randint(50,250) / 100.0
    x = random.randint(0,15)
    r = random.randint(70,100) / 100.0
    g = random.randint(60,90) / 100.0
    b = random.randint(1,50) / 100.0
    for n in range(50):
        global red_amount
        global green_amount
        global blue_amount
        red_amount = r
        green_amount = g
        blue_amount = b
        pencolor(red_amount, green_amount, blue_amount)
        setheading(x)
        if(0 <= x <= 90):
            rightLine()
            setpos(origin)
            x += random.randint(5,18)
        elif(90 < x <= 255):
            leftLine()
            setpos(origin)
            x += random.randint(5,18)
        elif(255 < x <= 285):
            x += 10
        elif(285 < x <= 360):
            rightLine()
            setpos(origin)
            x += random.randint(5,18)

def fxn(a,b):
    penup()
    goto(a,b)
    pendown()
    firework()

onscreenclick(fxn)

