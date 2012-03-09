__author__ = 'core'

from Tkinter import *
from ttk import Treeview

class SnakeLog(Frame):

    def createMenubar(self, master):
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

    def createQSOView(self, master):
        self.qsoviewScrollbar = Scrollbar(master)
        self.qsoview = Treeview(master, show=('headings'),
                                yscrollcommand=self.qsoviewScrollbar.set)


        self.qsoviewfields = {'day':            {'name': "D", 'width': 10},
                              'month':          {'name': "M", 'width': 10},
                              'year':           {'name': "Y", 'width': 20},
                              'timeon':         {'name': "Time", 'width': 30},
                              'timeoff':        {'name': "Timeoff", 'width': 30},
                              'band':           {'name': "Band", 'width': 20},
                              'freq':           {'name': "Frequency", 'width': 50},
                              'mode':           {'name': "Mode", 'width': 25},
                              'call':           {'name': "Call", 'width': 50},
                              'srst':           {'name': "S RST", 'width': 25},
                              'rrst':           {'name': "R RST",'width': 25},
                              'name':           {'name': "Name",'width': 40},
                              'grid':           {'name': "Gridsquare",'width': 30},
                              'iota':           {'name': "IOTA", 'width': 30},
                              'qsls':           {'name': "Q S",'width': 25},
                              'qsls_date':      {'name': "Q S D",'width': 50},
                              'qslr':           {'name': "Q R",'width': 25},
                              'qslr_date':      {'name': "Q R D",'width': 50},
                              'lotw_qsls':      {'name': "LQ S",'width': 25},
                              'lotw_qsls_date': {'name': "LQ S D",'width': 50},
                              'lotw_qslr':      {'name': "LQ R",'width': 25},
                              'lotw_qslr_date': {'name': "LQ R D",'width': 50}}


        self.qsoviewdisplayesfields = ('day', 'month', 'year', 'timeon',
                                       'band', 'freq', 'mode', 'call',
                                       'srst', 'rrst', 'name', 'grid',
                                       'iota', 'qsls', 'qsls_date', 'qslr',
                                       'qslr_date', 'lotw_qsls', 'lotw_qsls_date', 'lotw_qslr',
                                       'lotw_qslr_date')


        self.qsoview["columns"] = self.qsoviewfields.keys()
        self.qsoview["displaycolumns"] = self.qsoviewdisplayesfields


        self.qsoview.column(0, width=40)
        for columnname, data in self.qsoviewfields.items():
            # set columnwidth for QSOView
            self.qsoview.column(columnname, width=data['width'])
            # set QSOView headers
            self.qsoview.heading(columnname, text=data['name'])

        for i in range(400):
            self.qsoview.insert('', 'end', str(i), values=(str(i), 'bar'+str(i)))

        self.qsoviewScrollbar.config(command=self.qsoview.yview)

        self.qsoviewScrollbar.grid(column=1, row=0, sticky=(N,S))
        self.qsoview.grid(column=0, row=0, sticky=(N,S,E,W))

        master.columnconfigure(0, weight=1)
        master.rowconfigure(0, weight=1)

    def __init__(self, master=None):

        master.columnconfigure(0, weight=1)
        master.rowconfigure(0, weight=1)

        self.mainFrame = Frame.__init__(self, master)

        self.grid(sticky=(N,S,E,W))
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        self.createMenubar(master)

        self.qsoFrame = Frame(self.mainFrame)
        self.createQSOView(self.qsoFrame)
        self.qsoFrame.grid(sticky=(N,S,E,W))


root = Tk()
root.title("snakeLog - by DK2AB")
app = SnakeLog(master=root)
app.mainloop()
root.destroy()
