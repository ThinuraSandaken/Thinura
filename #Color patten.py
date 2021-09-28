import turtle

turtle.bgcolor("black")
turtle.pensize(2)
turtle.speed(0)

for i in range(50):
    for colors in ["red", "magenta", "blue", "cyan", "green", "yellow", "white"]:
        turtle.color(colors)
        turtle.circle(150)
        turtle.left(50)

turtle.hideturtle()        