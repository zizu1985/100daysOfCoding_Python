import turtle


def drawRegularPolygon(t, *args):
    for _ in range(args[0]):
        t.forward(args[1])
        t.right(360 / args[0])


def main():
    t = turtle.Turtle()
    screen = t.getscreen()
    # drawRegularPolygon(t, 3, 100)
    # drawRegularPolygon(t, 4, 200)
    drawRegularPolygon(t, 5, 100)
    screen.exitonclick()


if __name__ == '__main__':
    main()