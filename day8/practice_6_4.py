import sys
import tkinter


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
    note.pack()
    note.insert(tkinter.END, "This is example text")

    okbutton = tkinter.Button(mainFrame,text="Now!",command=obutton).pack()

    tkinter.mainloop()


if __name__ == "__main__":
    main()