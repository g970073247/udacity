import turtle

def square_draw():
    window = turtle.Screen()
    window.bgcolor('red')

    kaka = turtle.Turtle()
    kaka.shape('turtle')
    kaka.color('green')
    j = 0
    while j < 36:
        

        i = 0
        while i < 4:
            kaka.forward(100)
            kaka.right(90)
            i += 1
        j += 1
        kaka.right(10)
    window.exitonclick()
square_draw()
