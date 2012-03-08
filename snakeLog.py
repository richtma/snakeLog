__author__ = 'core'

from Tkinter import *

class Application(Frame):

    def createWidgets(self, master):
        self.menubar = Menu(root)

        self.filemenu = Menu(self.menubar, tearoff=0)

        self.importmenu = Menu(self.filemenu)
        self.importmenu.add_command(label="from ADIF...", command=None)

        self.exportmenu = Menu(self.filemenu)
        self.exportmenu.add_command(label="to ADIF...", command=None)
        self.exportmenu.add_command(label="to Cabrillo...", command=None)

        self.filemenu.add_command(label="Open log...", command=None)
        self.filemenu.add_command(label="Save log as...", command=None)
        self.filemenu.add_separator()
        self.filemenu.add_cascade(label="Export", menu=self.exportmenu)
        self.filemenu.add_cascade(label="Import", menu=self.importmenu)
        self.filemenu.add_separator()
        self.filemenu.add_command(label="Exit", command=None)

        self.menubar.add_cascade(label="File", menu=self.filemenu)

        master.config(menu=self.menubar)

    def __init__(self, master=None):
        Frame.__init__(self, master, height="600", width="800")
        self.pack()
        self.createWidgets(master)


root = Tk()
root.title("snakeLog - by DK2AB")
app = Application(master=root)
app.mainloop()
root.destroy()