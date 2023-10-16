from tkinter import Tk , BOTH
from tkinter.ttk import Frame, Label, Entry, Notebook, Button
from PIL import Image
from tkinter import *


class Example(Frame):
    def __init__(self, parent):
        self.__init__(self, parent)
        self.parent = parent
        self.parent.title('Grade_score')
        self.A = 5
        self.B = 4
        self.C = 3
        self.D = 2
        self.E = 1
        self.F = 0
        self.initUI()




    def initUI(self):
        
        welcome = Label(self, text='Hi welcome to grade score program, please answer the following question')
        welcome.grid(row=0, column=0, columnspan=2)
        name = Label(self, text="What is your Name:")
        name.grid(row=1, column=0)
        names = Entry(self)
        names.grid(row=1, column=1, padx=2, pady=3,)
        surname = Label(self, text='surname:')
        surname.grid(row=2, column=0)
        sn = Entry(self)
        sn.grid(row=2,column=1, padx=2, pady=3,)
        othername= Label(self, text='Other name')
        othername.grid(row=3, column=0)
        on =Entry(self)
        on.grid(row=3, column=1, padx=2, pady=3,)
        regnumber = Label(self, text="What is your matric number")
        regnumber.grid(row=4, column=0)
        Rn = Entry(self)
        Rn.grid(row=4, column=1, padx=2, pady=3,)
        faculty = Label(self, text="What's faculty:")
        faculty.grid(row=5, column=0)
        fa = Entry(self)
        fa.grid(row=5, column=1, padx=2, pady=3,)
        dp= Label(self, text='Which department of science:')
        dp.grid(row=6, column=0)
        department = Entry(self)
        department.grid(row=6, column=1, padx=2, pady=3,)
        option = Label(self, text="What is your discipline:")
        option.grid(row=7, column=0)
        discipline = Entry(self)
        discipline.grid(row=7, column=1, padx=2, pady=3,)
        botton = Button(self, text='submit', )
        botton.grid(row=8, column=0, columnspan=2)


'''
    def submit(self):
        n = names.__getattribute__()
        print(n)'''


def main():
    root = Tk()
    ex = Example(root)
    root.mainloop()
    root.geometry("860x750")

if __name__ == '__main__':
    main()