import turtle


def drawTruck(t,**coordinates):
    x = 0
    y = 0
    if "x" in coordinates:
        x = coordinates["x"]
    if "y" in coordinates:
        y = coordinates["y"]
    t.goto(x,y)
    t.pendown()
    t.forward(50)
    t.left(20)
    t.forward(20)
    t.right(45)
    t.forward(30)
    t.left(-45)
    t.forward(10)
    t.right(20)
    t.right(200)
    t.penup()


def main():
    x = int(input("Please provide x coordinate"))
    y = int(input("Please provide y coordinate"))
    t = turtle.Turtle()
    screen = t.getscreen()
    drawTruck(t, x=x, y=y)
    screen.exitonclick()


if __name__ == "__main__":
    main()
