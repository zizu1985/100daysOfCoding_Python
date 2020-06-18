import sys
import tkinter
import tkinter.messagebox
import os


class Reminder:
    def __init__(self, x, y, text):
        self.x = x
        self.y = y
        self.text = text
        notewin = tkinter.Toplevel()
        notewin.geometry("+"+str(self.x)+"+"+str(self.y))
        reminder = tkinter.Text(notewin, bg="yellow", width=50,
                                height=30)
        reminder.insert(tkinter.END, text)
        reminder.pack()
        self.reminder = reminder
        self.notewin = notewin

    """ Undraw method """
    def undraw(self):
        self.notewin.withdraw()

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def getText(self):
        return self.text

    def setDeleteHandler(self,comment):
        self.notewin.protocol("WM_DELETE_WINDOW", self.undraw)


def main():

    reminders = []

    def post():
        print("Post")
        reminder = Reminder(root.winfo_rootx()+5, root.winfo_rooty(), "1.0")
        reminders.append(reminder)


    root = tkinter.Tk()
    root.title("Reminder!")
    root.resizable(width=False,height=False)

    bar = tkinter.Menu(root)

    fileMenu = tkinter.Menu(bar,tearoff=0)
    fileMenu.add_command(label="Exit",command=root.quit)
    bar.add_cascade(label="File",menu=fileMenu)
    root.config(menu=bar)

    mainFrame = tkinter.Frame(root,borderwidth=1,padx=5,pady=5)
    mainFrame.pack()

    note = tkinter.Text(mainFrame,bg="yellow",width=30,height=15)
    note.pack()

    tkinter.Button(mainFrame,text="New Reminder!",command=post).pack()

    try:
        print("reading reminders.txt file")
        file = open("reminders.txt","r")
        x = int(file.readline())
        y = int(file.readline())
        root.geometry("+"+str(x)+"+"+str(y))

        line = file.readline()
        while line.strip() != "":
            x = int(line)
            y = int(file.readline())
            text = ""
            line = file.readline()
            while line.strip() != "____****_____*_*_*_":
                text = text + line
                line = file.readline()

            text = text.strip()
            reminder = Reminder(root.winfo_rootx() + 5, root.winfo_rooty(), text)
            reminders.append(reminder)

            line = file.readline()
    except:
        print("reminders.txt not found")


    def appClosing():
        print("Application Closing")
        file = open("reminders.txt","w")

        file.write(str(root.winfo_x()) + "\n")
        file.write(str(root.winfo_y()) + "\n")

        """
        for i in range(len(reminders)):
            print(reminders[i].winfo_rootx())
            print(reminders[i].winfo_rooty())
            print(reminders[i].get("1.0",tkinter.END))

            file.write(str(notes[i].winfo_rootx()+"\n"))
            file.write(str(notes[i].winfo_rooty()+"\n"))
            file.write("____****_____*_*_*_\n")
        """

        file.close()
        root.destroy()
        root.quit()
        sys.exit()

    root.protocol("WM_DELETE_WINDOW",appClosing)

    tkinter.mainloop()


if __name__ == "__main__":
    main()

