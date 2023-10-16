from tkinter import *
from PIL import Image, ImageTk
import sys

print(sys.executable)

root = Tk()
root.geometry("1200x750")
root.title('Gradescore')

def submit():
    Name = names.get()

background_pic = PhotoImage(file='top-view-globe-with-academic-cap-laptop.jpg')
My_image = Label(image=background_pic)
My_image.pack()

welcome = Label(root, text='Hi welcome to grade score program, please answer the following question').grid(row=0, column=0, columnspan=2)
name = Label(root, text="What is your Name:").grid(row=1, column=0)
names = Entry(root).grid(row=1, column=1, padx=2, pady=3,)
surname = Label(root, text='surname:').grid(row=2, column=0)
sn = Entry(root).grid(row=2,column=1, padx=2, pady=3,)
othername= Label(root, text='Other name').grid(row=3, column=0)
on =Entry(root).grid(row=3, column=1, padx=2, pady=3,)
regnumber = Label(root, text="What is your matric number").grid(row=4, column=0)
Rn = Entry(root).grid(row=4, column=1, padx=2, pady=3,)
faculty = Label(root, text="What's faculty:").grid(row=5, column=0)
fa = Entry(root).grid(row=5, column=1, padx=2, pady=3,)
dp= Label(root, text='Which department of science:').grid(row=6, column=0)
department = Entry(root).grid(row=6, column=1, padx=2, pady=3,)
option = Label(root, text="What is your discipline:").grid(row=7, column=0)
discipline = Entry(root).grid(row=7, column=1, padx=2, pady=3,)
botton = Button(root, text='submit', command=submit).grid(row=8, column=0, columnspan=2)


root.mainloop()