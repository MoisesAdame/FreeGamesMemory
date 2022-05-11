"""Pacman, classic arcade game.

Autores:
Programador 1: Moisés Adame Aguilar         (A01660927)
Programador 2: Ricardo Campos Luna          (A01656898)
Programador 3: Humberto Ivan Ulloa Cardona  (A01657143)

Fecha: 10 de Mayo del 2022
"""

from random import *
from turtle import *

from freegames import path

car = path('car.gif')
""" Modificación de los dígitos a emojis (se usó unicode)"""
tiles = ["\U0001F600", "\U0001F601", "\U0001F602", "\U0001F607", "\U0001F929", 
         "\U0001F61B", "\U0001F911", "\U0001F917", "\U0001F636", "\U0001F925",
         "\U0001F62A", "\U0001F634", "\U0001F922", "\U0001F92E", "\U0001F975", 
         "\U0001F976", "\U0001F92F", "\U0001F920", "\U0001F973", "\U0001F921", 
         "\U0001F47B", "\U0001F47D", "\U0001F47E", "\U0001F916", "\U0001F648", 
         "\U0001F498", "\U0001F9E1", "\U0001F49B", "\U0001F49A", "\U0001F499", 
         "\U0001F49C", "\U0001F90E", "\U0001F5A4"] * 2
state = {'mark': None}
hide = [True] * 64
# Tap counter
taps = {"number_taps": 0}


def square(x, y):
    """Draw white square with black outline at (x, y)."""
    up()
    goto(x, y)
    down()
    color('black', 'white')
    begin_fill()
    for count in range(4):
        forward(50)
        left(90)
    end_fill()


def index(x, y):
    """Convert (x, y) coordinates to tiles index."""
    return int((x + 200) // 50 + ((y + 200) // 50) * 8)


def xy(count):
    """Convert tiles count to (x, y) coordinates."""
    return (count % 8) * 50 - 200, (count // 8) * 50 - 200


def tap(x, y):
    """Update mark and hidden tiles based on tap."""
    spot = index(x, y)
    mark = state['mark']

    if mark is None or mark == spot or tiles[mark] != tiles[spot]:
        state['mark'] = spot
    else:
        hide[spot] = False
        hide[mark] = False
        state['mark'] = None

    # Counts the number of taps and displays it on the window
    taps["number_taps"] += 1
    print(taps["number_taps"])


def draw():
    """Draw image and tiles."""
    clear()
    goto(0, 0)
    shape(car)
    stamp()

    for count in range(64):
        if hide[count]:
            x, y = xy(count)
            square(x, y)

    mark = state['mark']

    if mark is not None and hide[mark]:
        x, y = xy(mark)
        up()
        goto(x + 2, y)
        color('black')
        write(tiles[mark], font=('Arial', 30, 'normal'))

    update()
    ontimer(draw, 100)
    

shuffle(tiles)
setup(420, 420, 370, 0)
addshape(car)
hideturtle()
tracer(False)
onscreenclick(tap)
draw()
done()
