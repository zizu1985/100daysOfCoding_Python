import math
import turtle

# Przechowywanie zolwia jako atrybut
# Kwestia uznania.


class Circle:
    # This is constructor
    def __init__(self,x=0,y=0,radius=50,color="transparent",
                 outline="black", edgeWidth=1, t=None):
        self.x = x
        self.y = y
        self.color = color
        self.outline = outline
        self.edgeWidth = edgeWidth
        self.radius = radius
        self.turtle = t

    # draw is mutator object
    def draw(self):
        t.penup()
        t.goto(self.x, self.y)
        t.width(self.edgeWidth)
        if self.color != "transparent":
            t.fillcolor(self.color)
        t.color(self.outline)
        t.setheading(0)
        t.forward(self.radius)
        if self.color != "transparent":
            t.begin_fill()
        t.pendown()
        for k in range(500):
            radians = (2*math.pi)*(k/500.0)
            t.goto(math.cos(radians)*self.radius + self.x,
                        math.sin(radians)*self.radius + self.y)
        if self.color != "transparent":
            t.end_fill()
        t.penup()
        t.goto(self.x, self.y)

    # The following three methods are mutator methods
    def setEdgeWidt(self,width):
        self.edgeWidth = width

    def setFill(self, color):
        self.color = color

    def setOutline(self,color):
        self.outline = color

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def getRadius(self):
        return self.radius

    def getTurtle(self):
        return self.t

    def setTurtle(self, t):
        self.t = t


if __name__ == "__main__":
    t = turtle.Turtle()
    circle = Circle(t=t)
    circle.draw()