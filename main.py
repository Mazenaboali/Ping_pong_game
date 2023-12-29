# import modules
import turtle
# initialize window
wind = turtle.Screen()
# set the title of the window
wind.title("Ping pong game")
# set the background color of the window
wind.bgcolor("black")
# set the width and the height of the window
wind.setup(height=600,width=800)
# stops the window from updating automatically
wind.tracer(0)

#madrap1
madrap1=turtle.Turtle()
# set the speed of the animation
madrap1.speed(0)
#set the shape of the object
madrap1.shape("square")
# set the color of the shape
madrap1.color("blue")
#stretch the shape
madrap1.shapesize(stretch_wid=5,stretch_len=1)
# stops the object from drawing Lines
madrap1.penup()
# set the position of the madrap
madrap1.goto(-350,0)

#score
score1=0
score2=0
score=turtle.Turtle()
score.speed(0)
score.color("white")
score.penup()
score.hideturtle()
score.goto(0,260)
score.write("player 1:0 player 2:0",font=("Courier",24,"normal"),align="center")

#madrap2
madrap2=turtle.Turtle()
# set the speed of the animation
madrap2.speed(0)
#set the shape of the object
madrap2.shape("square")
# set the color of the shape
madrap2.color("red")
#stretch the shape
madrap2.shapesize(stretch_wid=5,stretch_len=1)
# stops the object from drawing Lines
madrap2.penup()
# set the position of the madrap
madrap2.goto(350,0)

# ball
ball=turtle.Turtle()
# set the speed of the animation
ball.speed(0)
#set the shape of the object
ball.shape("square")
# set the color of the shape
ball.color("white")
# stops the object from drawing Lines
ball.penup()
# set the position of the madrap
ball.goto(0,0)
ball.dx=0.3
ball.dy=0.3

# functions
def madrap1_up() :
    y= madrap1.ycor()
    y+=20
    madrap1.sety(y)
def madrap1_down() :
    y= madrap1.ycor()
    y-=20
    madrap1.sety(y)

def madrap2_up() :
    y= madrap2.ycor()
    y+=20
    madrap2.sety(y)
def madrap2_down() :
    y= madrap2.ycor()
    y-=20
    madrap2.sety(y)

# keyboard bindings
wind.listen()
wind.onkeypress(madrap1_up,"w")
wind.onkeypress(madrap1_down,"s")
wind.onkeypress(madrap2_up,"Up")
wind.onkeypress(madrap2_down,"Down")


# main game loop
while True:
# updates the screen everytime the loop run
    wind.update()
#move the ball
    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)
#border check
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *=-1

    if ball.ycor() <-290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() >390:
        ball.goto(0,0)
        ball.dx *=-1
        score2 += 1
        score.clear()
        score.write("player 1: {} player 2: {}".format(score1, score2), font=("Courier", 24, "normal"), align="center")
    if ball.xcor() <-390:
        ball.goto(0, 0)
        ball.dx *= -1
        score1 += 1
        score.clear()
        score.write("player 1: {} player 2: {}".format(score1, score2), font=("Courier", 24, "normal"), align="center")

    if( (ball.xcor() > -350 and ball.xcor() < -340 ) and (ball.ycor() < (madrap1.ycor()+40) and ball.ycor() >(madrap1.ycor()-40)) ) :
        ball.setx(-340)
        ball.dx *=-1
    if ((ball.xcor() <  350 and ball.xcor() > 340) and (
        ball.ycor() < (madrap2.ycor() + 40) and ball.ycor() > (madrap2.ycor() - 40))):
        ball.setx(340)
        ball.dx *= -1








