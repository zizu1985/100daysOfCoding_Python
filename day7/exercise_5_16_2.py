import turtle
import tkinter
import tkinter.messagebox


def drawTruck(t,**coordinates):
    x = 0
    y = 0
    if "x" in coordinates:
        x = coordinates["x"]
    if "y" in coordinates:
        y = coordinates["y"]
    if "scale" in coordinates:
        scale = coordinates["scale"]
    t.goto(x,y)
    t.pendown()
    t.forward(40 * scale)
    t.left(20 * scale)
    t.forward(20 * scale)
    t.right(45 * scale)
    t.forward(30 * scale)
    t.left(45 * scale)
    t.forward(10 * scale)
    t.right(20 * scale)
    t.right(200 * scale)
    t.penup()


def main():
    x = int(input("Please provide x coordinate"))
    y = int(input("Please provide y coordinate"))

    t = turtle.Turtle()
    screen = t.getscreen()
    drawTruck(t, x=x, y=y,scale=0.1)
    screen.exitonclick()


if __name__ == "__main__":
    main()
