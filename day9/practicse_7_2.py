class Rectangle:

    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def getwidth(self):
        return self.width


if __name__ == "__main__":
    box = Rectangle(100, 100, 50, 30)
    print(box.getwidth())