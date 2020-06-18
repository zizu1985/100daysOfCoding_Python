import turtle


class Rectangle:

    def __init__(self, x=100, y=100, width=50, height=30, outline="black", color="transparent"):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.outline = outline
        self.color = color

    def getwidth(self):
        return self.width

    def draw(self, t):
        t.speed(1)
        t.penup()
        t.width(10)
        t.goto(self.x, self.y)

        t.color(self.outline)
        t.setheading(0)

        # Fillcolor has to be called just before begin_fill method
        if self.color != "transparent":
            t.fillcolor(self.color)
            t.begin_fill()

        t.pendown()
        t.forward(self.width)
        t.right(90)
        t.forward(self.height)
        t.right(90)
        t.forward(self.width)
        t.right(90)
        t.forward(self.height)

        if self.color != "transparent":
            t.end_fill()
        t.penup()
        t.goto(self.x, self.y)


if __name__ == "__main__":

    t = turtle.Turtle()

    box = Rectangle(100, 100, 200, 120, outline="black", color="red")
    print(box.getwidth())

    box.draw(t)