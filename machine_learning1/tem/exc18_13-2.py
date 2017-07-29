import turtle

def square_draw(a_turtle):

    
   i = 0
   while i < 4:
        a_turtle.forward(100)
        a_turtle.right(90)
        i += 1
        
   
def graph_draw():

    window = turtle.Screen()
    window.bgcolor('blue')

    kapa = turtle.Turtle()
    kapa.shape('turtle')
    kapa.color('red')

    j = 0
    while j < 36:
        square_draw(kapa)
        j += 1
        kapa.right(10)
    window.exitonclick()
    
graph_draw()


