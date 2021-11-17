from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import time

class HomeScreen:
    def __init__(self, toplevel):
        self.x = 0
        self.y = 0

        self.toplevel = toplevel
        self.toplevel.title('Draw Tool')

        self.canvas = Canvas(toplevel, width=600, height=100)
        self.canvas.pack()

        self.frame1 = Frame(toplevel)
        self.frame1.pack()

        # Draw select button
        self.select = Button(self.frame1, text='select', command=self.Select)
        self.select['padx'], self.select['pady'] = 10, 5
        self.select.pack(side=LEFT)

        # Draw delete button
        self.delete = Button(self.frame1, text='delete', command=self.Delete)
        self.delete['padx'], self.delete['pady'] = 10, 5
        self.delete.pack(side=LEFT)

        # Draw rectangle button
        self.triang = Button(self.frame1, text='Triang', command=self.DrawTriang)
        self.triang['padx'], self.triang['pady'] = 10, 5
        self.triang.pack(side=LEFT)

        # Draw rectangle button
        self.rect = Button(self.frame1, text='Rect', command=self.DrawRect)
        self.rect['padx'], self.rect['pady'] = 10, 5
        self.rect.pack(side=LEFT)

        # Draw Poligons n-sides
        self.poligonsnsides = Button(self.frame1, text='Free', command=self.FreeDraw)
        self.poligonsnsides['padx'], self.poligonsnsides['pady'] = 10, 5
        self.poligonsnsides.pack(side=LEFT)




    def Select(self):
        pass

    def Delete(self):
        pass

    def DrawTriang(self):
        pass

    def DrawRect(self):
        self.canvas.create_rectangle(30, 10, 120, 80)
        #self.canvas.pack()

    def FreeDraw(self):
        time.sleep(2)
        self.canvas.bind("<Button-1>", self.click)
        self.canvas.create_line(0, 0, self.x, self.y)


    def click(self, event):
        print('Event')
        self.x, self.y = event.x, event.y
