from turtle import *
import tkinter
import random

screenMaxX = 300
screenMaxY = 300
screenMinX = -300
screenMinY = -300


# Ball inherits from RawTurtle
class Ball(RawTurtle):

    def __init__(self,cv,dx,dy):
        RawTurtle.__init__(self,cv)

        #Then the rest of the object is initialized
        self.penup()
        self.shape("soccerball.gif")
        self.dx = dx
        self.dy = dy

    # move is mutator object
    def move(self):
        newx = self.xcor() + self.dx
        newy = self.ycor() + self.dy

        # make the ball bounced of the wall
        if newx < screenMinX:
            newx = 2 * screenMinX - newx
            self.dx = -self.dx
        if newy < screenMinY:
            newy = 2 * screenMinY - newy
            self.dy = - self.dy
        if newx > screenMaxX:
            newx = 2 * screenMaxX - newx
            self.dx = - self.dx
        if newy > screenMaxY:
            newy = 2 * screenMaxY - newy
            self.dy = -self.dy
        self.goto(newx,newy)


class GravityBall(Ball):
    def __init__(self, cv, dx, dy):
        super().__init__(cv, dx, dy)

    def move(self):
        # Gravity effect is -1/2g t^2. Time is
        # estimated at 1/100 of a second for each
        # call to move

        if abs(self.dy) < 0.2 and self.ycor() < 5:
            self.dy = 0
        else:
            self.dy = self.dy - 0.195
        if abs(self.dx) < 0.2:
            self.dx = 0
        else:
            self.dx = 0.999 * self.dx

        Ball.move(self)


def main():
    root = tkinter.Tk()
    root.title("Bouncing Balls!")
    cv = ScrolledCanvas(root,600,600,600,600)
    cv.pack(side = tkinter.LEFT)
    t = RawTurtle(cv)
    fram = tkinter.Frame(root)
    fram.pack(side = tkinter.RIGHT, fill=tkinter.BOTH)

    screen = t.getscreen()
    screen.setworldcoordinates(screenMinX,screenMinY,screenMaxX,screenMaxY)
    t.ht()
    screen.tracer(20)
    screen.register_shape("soccerball.gif")

    # List of balls in program
    ballList = []

    # Animation handler. It is called at every timer event.
    def animate():
        # Tell all the balls to move
        for ball in ballList:
            ball.move()
        screen.ontimer(animate,"20")

    # This code creates 10 balls heading in random directions
    for k in range(3):
        dx = random.random() * 3 + 1
        dy = random.random() * 3 + 1
        ball = Ball(cv,dx,dy)
        ballList.append(ball)

    for j in range(3):
        dx = random.random() * 3 + 1
        dy = random.random() * 3 + 1
        ball = GravityBall(cv, dx, dy)
        ballList.append(ball)

    def quitHandler():
        # close the window and quit
        print("Good Bye")
        root.destroy()
        root.quit()

    quitButton = tkinter.Button(fram,text = "Quit",command=quitHandler)
    quitButton.pack()

    t.speed(1)
    screen.ontimer(animate,"20")
    tkinter.mainloop()


if __name__ == "__main__":
    main()



