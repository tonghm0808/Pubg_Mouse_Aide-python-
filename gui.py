# -*- coding: UTF-8 -*-
import Tkinter as tk
import os


class App(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.overrideredirect(True)
        self.attributes('-alpha', 0.8)
        self.attributes('-transparentcolor', 'blue')
        self.attributes('-topmost', 1)
        self.geometry('200x20+900+0')
        self.canvas = tk.Canvas(self, width=200, height=20, bg='blue')
        self.canvas.bind('<Double-Button-1>', self.Quit)
        self.canvas.pack()

    def Quit(self, event):
        command = 'taskkill /F /IM aider.exe'
        os.system(command)

    def Update(self, tab1=0, tab2=0):
        self.canvas.delete("TAB1")
        self.canvas.delete("TAB2")
        if tab1 == 0:
            self.canvas.create_text(35, 10, text='OFF', font=(
                'Calibri', 12, 'bold'), fill='red', anchor='w', tag='TAB1')
        else:
            self.canvas.create_text(35, 10, text='ON', font=(
                'Calibri', 12, 'bold'), fill='green', anchor='w', tag='TAB1')
        self.canvas.create_text(85, 10, text='OFFSET:%d' % tab2, font=(
            'Calibri', 12, 'bold'), fill='yellow', anchor='w', tag='TAB2')
        self.update()
