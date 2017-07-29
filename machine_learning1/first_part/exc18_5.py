import turtle

def draw_square():
    window = turtle.Screen()
    window.bgcolor('red')

    brad = turtle.Turtle()
    brad.shape('turtle')
    brad.color('yellow')
    brad.speed(1)
    
    brad.forward(100)
    i = 0
    while i < 3:
        brad.right(90)
        brad.forward(100)
        i += 1

    ana = turtle.Turtle()
    ana.shape('turtle')
    ana.color('green')
    ana.circle(100)
    window.exitonclick()
draw_square()
