import turtle

def square_draw(a_turtle):
    a_turtle.forward(100)
    a_turtle.right(60) #1
    a_turtle.forward(100)
    a_turtle.right(120) #2
    a_turtle.forward(100)
    a_turtle.right(60) #3
    a_turtle.forward(100)
    a_turtle.right(120) #4

   
def graph_draw():

    window = turtle.Screen()
    window.bgcolor('blue')

    kapa = turtle.Turtle()
    kapa.shape('turtle')
    kapa.color('red')
    kapa.right(60)
    kapa.speed(0)

    j = 0
    while j < 40:
        square_draw(kapa)
        j += 1
        kapa.right(9)
    window.exitonclick()
    
graph_draw()

'''
window = turtle.Screen()
window.bgcolor('blue')

kapa = turtle.Turtle()
kapa.shape('turtle')
kapa.color('red')
kapa.right(60)
square_draw(kapa)
window.exitonclick()
'''