from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import time

class HomeScreen:
    def __init__(self, toplevel):
        self.x = []
        self.y = []

        self.toplevel = toplevel
        self.toplevel.title('Draw Tool')
        self.toplevel.geometry("800x600")
        self.toplevel.configure(background="green")

        self.frame1 = Frame(toplevel, bg="#000", width=150, height=600)
        self.frame1.pack(side=LEFT, fill='y')

        self.frame2 = Frame(toplevel, bg="#fff", width=650, height=600)
        self.frame2.pack(side=RIGHT)

        self.canvas = Canvas(self.frame2, width=650, height=600, bg="white")
        self.canvas.pack()

        # Draw select button
        self.selectbt = Button(self.frame1, text='select', command=self.Select)
        self.selectbt['padx'], self.selectbt['pady'] = 10, 5
        self.selectbt.place(x = 10, y = 10)

        # Draw delete button
        self.deletebt = Button(self.frame1, text='delete', command=self.Delete)
        self.deletebt['padx'], self.deletebt['pady'] = 10, 5
        self.deletebt.place(x = 80, y = 10)

        # Draw triangle button
        self.triangbt = Button(self.frame1, text='Triang', command=self.DrawTriang)
        self.triangbt['padx'], self.triangbt['pady'] = 10, 5
        self.triangbt.place(x = 10, y = 50)

        # Draw rectangle button
        self.rectbt = Button(self.frame1, text='Rect', command=self.DrawRect)
        self.rectbt['padx'], self.rectbt['pady'] = 10, 5
        self.rectbt.place(x = 80, y = 50)

        # Draw Poligons n-sides
        self.poligonsnsidesbt = Button(self.frame1, text='Free', command=self.FreeDraw)
        self.poligonsnsidesbt['padx'], self.poligonsnsidesbt['pady'] = 10, 5
        self.poligonsnsidesbt.place(x = 10, y = 90)


    def Select(self):
        pass

    def Delete(self):
        pass

    def DrawTriang(self):
        pass

    def DrawRect(self):
        self.canvas.create_rectangle(30, 10, 120, 80)
        #self.canvas.pack()


    def Switch(self):
        print('Draw State: {}'.format(self.poligonsnsidesbt["state"]))
        '''
        if self.poligonsnsidesbt["state"] == NORMAL:
            print('Here')
            self.poligonsnsidesbt["state"] = ACTIVE
            self.poligonsnsidesbt.config(relief=SUNKEN)
            print('Draw State: {}'.format(self.poligonsnsidesbt["state"]))
        elif self.poligonsnsidesbt["state"] == ACTIVE:
            self.poligonsnsidesbt["state"] = NORMAL
            self.poligonsnsidesbt.config(relief=RAISED)
        '''
        if self.poligonsnsidesbt["relief"] == RAISED:
            self.poligonsnsidesbt.config(relief=SUNKEN)

        elif self.poligonsnsidesbt["relief"] == SUNKEN:
            self.poligonsnsidesbt.config(relief=RAISED)


    def FreeDraw(self):
        x, y = 0, 0

        self.Switch()


        time.sleep(2)

        print('RELIEF: {}'.format(self.poligonsnsidesbt["relief"]))

        self.canvas.bind("<Button-1>", self.click)

        '''if count == 0:
            x, y = self.x, self.y
            count += 1
        elif count == 1:
        if len(self.x) == 2 and len(self.y) == 2:
            print('entrou no draw')
            print('x[0]: {}'.format(self.x[0]))
            print('y[0]: {}'.format(self.y[0]))
            print('x[1]: {}'.format(self.x[1]))
            print('y[1]: {}'.format(self.y[1]))
            self.canvas.create_line(self.x[0], self.y[0], self.x[1], self.y[1])
            x = self.x[1]
            y = self.y[1]
            self.x = []
            self.y = []
            self.x.append(x)
            self.y.append(y)'''


    def click(self, event):
        print('Event')
        x, y = 0, 0

        if self.x == []:
            self.x.append(event.x)
            self.y.append(event.y)
        else:
            self.x.append(event.x)
            self.y.append(event.y)
            self.canvas.create_line(self.x[0], self.y[0], self.x[1], self.y[1])
            x = self.x[1]
            y = self.y[1]
            self.x = []
            self.y = []
            self.x.append(x)
            self.y.append(y)
