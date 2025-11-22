import turtle


turtle.Screen().bgcolor("purple")
pen = turtle.Turtle()


pen.fillcolor("yellow")
pen.begin_fill()

pen.forward(100)
pen.left(120)
pen.forward(100)
pen.left(120)
pen.forward(100)

pen.end_fill()


pen.penup()
pen.right(150)
pen.forward(180)
pen.pendown()


pen.fillcolor("pink")
pen.begin_fill()

pen.forward(120)
pen.left(90)
pen.forward(60)
pen.left(90)
pen.forward(120)
pen.left(90)
pen.forward(60)

pen.end_fill()


pen.penup()
pen.right(90)
pen.forward(200)
pen.pendown()


pen.fillcolor("lightgreen")
pen.begin_fill()

for _ in range(6):
    pen.forward(70)
    pen.left(60)

pen.end_fill()

turtle.done()
