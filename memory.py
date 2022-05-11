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
num_resultos=0 #Esto se debe llenar hasta 32 que es el maximo de numero segun los tiles que utilizaremos

car = path('car.gif')
tiles = list(range(32)) * 2
state = {'mark': None}
hide = [True] * 64
# Tap counter
taps = {"number_taps":0}


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
    global num_resultos

    if mark is None or mark == spot or tiles[mark] != tiles[spot]:
        state['mark'] = spot
    else:
        hide[spot] = False
        hide[mark] = False
        state['mark'] = None
        num_resultos=num_resultos+1 #Esto actualizará a nuestro contador de parejas cada vez que se volteen los tiles de la imagen


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
        """Aqui estamos modificando, goto, color y añadimos align"""
        goto(x+11, y+12) #Jugamos con la suma de los numeros para poder alinear correctamente su posicion
        color('Blue') #Cambiamos el color del texto 
        write(tiles[mark],align="center", font=('Times new roman', 25, 'normal')) #Se utilizo la funcion de turtle en la caracteristica align para centrar mejor el texto
    """Este if esta verificando el contador de parejas encontradas para mostrar el Game over una vez se encuentren todas las parejas por eso esta dentro del draw para que se actualice"""
    if num_resultos==32:
        goto(0,70) #Esto nos coloca el texto en la imagen en la posicion 0, 70
        color("Red") #Color del texto
        write("Game_Over",align="center", font=('Times new roman', 30, 'normal'))
    update()
    ontimer(draw, 100)

# Function that counts the number of taps and displays it on the window
def tap_counter(x, y):
    taps["number_taps"] += 1
    print(taps["number_taps"])

shuffle(tiles)
setup(420, 420, 370, 0)
addshape(car)
hideturtle()
tracer(False)
onscreenclick(tap)
onscreenclick(tap_counter)
draw()
done()
