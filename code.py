from turtle import *
import time as t

cr = 0

speed('fastest')
bgcolor('#bd3e91')
pencolor('white')
pensize('4')

for i in range(100):
    circle(100)
    right(70)
    left(35)
    cr = cr + 1
    print('circle ', cr)

pencolor('#bd3e91')
dot(55)
hideturtle()

t.sleep(10)
