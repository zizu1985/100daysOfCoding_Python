class Shape:
    def __init__(self,x=0,y=0,color="transparent",
                 outline="black", width=1):
        self.x = x
        self.y = y
        self.color = color
        self.outline = outline
        self.width = width


    def setWidth(self,width):
        self.width = width


    def setFill(self,color):
        self.color = color


    def setOutline(self,color):
        self.outline = color


    def getX(self):
        return self.x


    def getY(self):
        return self.y