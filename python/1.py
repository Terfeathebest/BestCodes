import turtle

wn = turtle.Screen()
wn.title('Terfea')
wn.bgcolor('black')

pen = turtle.Turtle()
pen.speed(0)
pen.color("gold")
pen.penup()
pen.hideturtle()
pen.goto(-5, 250)
pen.write("Terfea", align="center", font=( 1000000000000000000000000000000000000000000000000 ))
pen.shapesize(stretch_wid=5, stretch_len=5)


pen1 = turtle.Turtle()
pen1.speed(0)
pen1.color("gold")
pen1.penup()
pen1.hideturtle()
pen1.goto(-5, 230)
pen1.write("So I am Terfea and I am The Best P", align="center", font=( 100000000000000000000000000000000000 ))
pen1.shapesize(stretch_wid=5, stretch_len=5)
while True:
    wn.update