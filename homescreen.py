from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import time
from node import *
from edge import *
from polygon import *

class HomeScreen:
    def __init__(self, toplevel):
        self.x = []
        self.y = []
        self.n1 = Node()
        self.n2 = Node()
        self.pol = Polygon()
        self.count = 0
        self.close = False

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

        self.Switch()

        #time.sleep(2)

        print('RELIEF: {}'.format(self.poligonsnsidesbt["relief"]))

        self.canvas.bind("<Button-1>", self.click)


    def click(self, event):
        #print('Event')

        if self.count == 0:
            #self.x.append(event.x)
            #self.y.append(event.y)
            self.n1 = Node(event.x, event.y)
            self.count += 1
            print('n1.X: {}'.format(self.n1.getX()))
            print('n1.Y: {}'.format(self.n1.getY()))
        else:
            self.x.append(event.x)
            self.y.append(event.y)
            self.n2 = Node(event.x, event.y)
            if self.count > 1:
                aux = self.pol.getEdge()
                print('N2: {}'.format(self.n2.getX()))
                print('Auxiliar: {}, Tam: {}'.format(aux, len(aux)))
                print('Aux: {}'.format(aux[0].getNode1().getX()))
                print('Aux: {}'.format(aux[0].getNode1().getY()))
                if (abs(self.n2.getX() - aux[0].getNode1().getX()) <= 5) and (abs(self.n2.getY() - aux[0].getNode1().getY()) <= 5):
                    self.n2.setX(aux[0].getNode1().getX())
                    self.n2.setY(aux[0].getNode1().getY())
                    self.close = True


            #print('n2.X: {}'.format(self.n2.getX()))
            #print('n2.Y: {}'.format(self.n2.getY()))
            ed = Edge(self.n1, self.n2)
            self.canvas.create_line(ed.getNode1().getX(), ed.getNode1().getY(), ed.getNode2().getX(), ed.getNode2().getY())
            self.pol.setEdge(ed)
            self.n1 = self.n2
            self.count += 1
