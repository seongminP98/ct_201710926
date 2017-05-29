import turtle
wn = turtle.Screen()
t1 = turtle.Turtle()

def drawSquare(size):
    for i in range(0,4):
        t1.fd(size)
        t1.right(90)
        
def drawSquareAt(x,y,size):
    t1.penup()
    t1.goto(x,y)
    t1.pendown()
    drawSquare(size)


def drawTriangle(size):
    for i in range(0,3):
        t1.fd(size)
        t1.right(120)
        
def drawTriangleAt(x,y,size):
    t1.penup()
    t1.goto(x,y)
    t1.pendown()
    drawTriangle(size)


def drawStar(size):
    for i in range(0,5):
        t1.fd(size)
        t1.right(144)
        
def drawStarAt(x,y,size):
    t1.penup()
    t1.goto(x,y)
    t1.pendown()
    drawStar(size)

drawSquareAt(-200,-200,100)
drawTriangleAt(0,0,100)
drawStarAt(200,200,100)

wn.exitonclick()