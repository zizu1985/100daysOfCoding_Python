import sys
import tkinter
import tkinter.messagebox

# All childs of mainFrame have to have the same layout


def main():
    root = tkinter.Tk()
    root.title("Reminder!")
    root.resizable(width=False,height=False)

    def quit():
        root.destroy()

    def help():
        print("About was Selected")

    def obutton():
        print("Oh, now you've done it!")
        tkinter.messagebox.showinfo("He wants...", noteTitle.get())

    bar = tkinter.Menu(root)

    fileMenu = tkinter.Menu(bar, tearoff=0)
    fileMenu.add_command(label="Exit",command=quit)
    helpMenu = tkinter.Menu(bar, tearoff=0)
    helpMenu.add_command(label="About",command=help)

    bar.add_cascade(label="File",menu=fileMenu)
    bar.add_cascade(label="Help",menu=helpMenu)
    root.config(menu=bar)

    mainFrame = tkinter.Frame(root, borderwidth=1, padx=5, pady=5)
    mainFrame.pack()

    note = tkinter.Text(mainFrame,bg="yellow",width=30,height=15)
    note.grid(row=1,column=1,columnspan=3)
    note.insert(tkinter.END, "This is example text")

    noteTitle = tkinter.StringVar()

    okbutton = tkinter.Button(mainFrame,text="Now!",command=obutton).grid(row=2, column=1, sticky=tkinter.E)
    anotherLabel = tkinter.Label(mainFrame,text="What do you want?").grid(row=2, column=2, sticky=tkinter.W)
    titleText = tkinter.Entry(mainFrame,textvariable=noteTitle)
    titleText.grid(row=2,column=3)

    tkinter.mainloop()


if __name__ == "__main__":
    main()