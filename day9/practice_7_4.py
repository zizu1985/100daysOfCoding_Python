from turtle import *
from tkinter import *
import math
from day9.rectangle import Rectangle


# Global constants
noselection = 0
# Shape type
circle = 1
rectangle = 2


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
        self.t = t

    # draw is mutator object
    def draw(self):
        self.t.penup()
        self.t.goto(self.x, self.y)
        self.t.width(self.edgeWidth)
        if self.color != "transparent":
            self.t.fillcolor(self.color)
        self.t.color(self.outline)
        self.t.setheading(0)
        self.t.forward(self.radius)
        if self.color != "transparent":
            self.t.begin_fill()
        self.t.pendown()
        for k in range(500):
            radians = (2*math.pi)*(k/500.0)
            self.t.goto(math.cos(radians)*self.radius + self.x,
                        math.sin(radians)*self.radius + self.y)
        if self.color != "transparent":
            self.t.end_fill()
        self.t.penup()
        self.t.goto(self.x, self.y)

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


# The Circle class is ommited here
class DrawApp:
    def __init__(self):
        root = Tk()
        self.shapeSelection = noselection
        cv = ScrolledCanvas(root, 600, 600, 600, 600)
        cv.pack(side = LEFT)
        aTurtle = RawTurtle(cv)
        screen = aTurtle.getscreen()
        aTurtle.ht()
        screen.tracer(0)

        fram = Frame(root)
        fram.pack(side = RIGHT,fill=BOTH)

        def circCommand():
            print("in circCommand")
            self.shapeSelection = circle

        def recCommand():
            print("in recCommand")
            self.shapeSelection = rectangle

        radiusEnt = StringVar()
        radiusLabel = Label(fram,text="Radius/Width:")
        radiusLabel.grid(row=2,column=1,sticky=E)
        radiusEntry = Entry(fram,textvariable=radiusEnt)
        radiusEntry.grid(row=2,column=2,sticky=E+W)

        heightEnt = StringVar()
        heightLabel = Label(fram,text="Height:")
        heightLabel.grid(row=2,column=2,sticky=E)
        hieghtEntry = Entry(fram,textvariable=heightEnt)
        hieghtEntry.grid(row=2,column=3,sticky=E+W)

        circleButton = Button(fram, text = "Circle",
                              command=circCommand)
        circleButton.grid(row=1,column=1,columnspan=2)
        rectangleButton = Button(fram, text="Rectangle",
                              command=recCommand)
        rectangleButton.grid(row=1, column=2, columnspan=1)


        def clickHanlder(x,y):
            print("In clickHandler")
            if self.shapeSelection == circle:
                print("shape selection was circle")
                radius = radiusEnt.get()
                if radius.strip() == "":
                    radius = 50
                else:
                    radius = float(radius)
                shape = Circle(x,y,radius,edgeWidth=3,
                               color="red",outline="gray",t=aTurtle)
                shape.draw()
                screen.update()
            elif self.shapeSelection == rectangle:
                print("shape selection was rectangle")
                width = radiusEnt.get()
                width = float(width)
                height = heightEnt.get()
                height = float(height)
                shape = Rectangle(x, y, width=width, height=height,
                                  outline="yellow", color="red")
                shape.draw(aTurtle)
                screen.update()
            else:
                print("Shape is not known.")

        screen.onclick(clickHanlder)


def main():
    app = DrawApp()
    mainloop()


if __name__ == "__main__":
    main()
