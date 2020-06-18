class Circle:
    # Constructor
    def __init__(self,x=0,y=0,radius=50,color="transparent",
                 outline="black",edgeWidth=1):
        self.x = x
        self.y = y
        self.color = color
        self.outline = outline
        self.edgeWidth = edgeWidth
        self.radius = radius


    def getradius(self):
        return self.radius


# Python allocates memory themself


if __name__ == "__main__":
    x = 10
    y = 10
    radius = 40
    shape = Circle(x, y, radius, edgeWidth=3,
                   color="red", outline="gray")
    print(shape.getradius())

