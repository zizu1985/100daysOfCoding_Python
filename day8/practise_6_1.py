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


    bar = tkinter.Menu(root)
    fileMenu = tkinter.Menu(bar, tearoff=0)
    fileMenu.add_command(label="Exit",command=quit)
    helpMenu = tkinter.Menu(bar, tearoff=0)
    helpMenu.add_command(label="About",command=help)
    bar.add_cascade(label="File",menu=fileMenu)
    bar.add_cascade(label="Help",menu=helpMenu)
    root.config(menu=bar)

    tkinter.mainloop()


if __name__ == "__main__":
    main()