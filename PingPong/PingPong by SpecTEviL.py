# Author - Vishal Patil
# Description - A simple ping pong multiplayer game.
# Controls - Player Blue : Up -> Up arrow
#		                   Down -> Down arrow
#          - Player Red :  Up -> w
#		                   Down -> s

import turtle

wn = turtle.Screen()
wn.title('Ping Pong ')
wn.bgcolor('black')
wn.setup(width=800, height=600)
wn.tracer(0)

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape('square')
paddle_a.color('red')
paddle_a.penup()
paddle_a.goto(-350, 0)
paddle_a.shapesize(5, 0.5)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape('square')
paddle_b.color('blue')
paddle_b.penup()
paddle_b.goto(350, 0)
paddle_b.shapesize(5, 0.5)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape('circle')
ball.color('yellow')
ball.penup()
ball.dx = 0.5
ball.dy = 0.5

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color('green')
pen.penup()
pen.goto(0, 230)
pen.write("Red - 0 vs Blue - 0", align='center', font=('Courier', 20, 'bold'))
pen.hideturtle()

# Heading
header = turtle.Turtle()
header.speed(0)
header.color('white')
header.penup()
header.goto(0, 260)
header.write("PING PONG by SpecTEviL", align='center', font=('Ayuthaya', 30, 'bold'))
header.hideturtle()

# Score
score_a = 0
score_b = 0

def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y += -20
    paddle_a.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y += -20
    paddle_b.sety(y)

# Keyboard binding
wn.listen()
wn.onkeypress(paddle_a_up, 'w')
wn.onkeypress(paddle_a_down, 's')
wn.onkeypress(paddle_b_up, 'Up')
wn.onkeypress(paddle_b_down, 'Down')


# Main game loop
while True:
    wn.update()

    # Moving Ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking
    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Red - {} vs Blue - {}".format(score_a, score_b), align='center', font=('Courier', 20, 'bold'))

    if ball.xcor() < -390:
        ball.goto(0, 0)

        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Red - {} vs Blue - {}".format(score_a, score_b), align='center', font=('Courier', 20, 'bold'))

    # Paddle and ball collisions
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 60 and ball.ycor() > paddle_b.ycor() -60):
        ball.setx(340)
        ball.dx *= -1

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 60 and ball.ycor() > paddle_a.ycor() -60):
        ball.setx(-340)
        ball.dx *= -1