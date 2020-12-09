import random
from tkinter import Button,Tk,Label
def fun():
    maintk=Tk()
    maintk.config(bg='green')
    value=Label(maintk,text=' ',bg='green',font='arial 40 bold',height=1,width=2)
    value.grid(row=1,column=1)
    roll=Button(maintk,text='Roll the Dice',height=1,width=17,bg='powder blue',command=lambda:mainfun(value))
    roll.grid(row=2,column=1)
def mainfun(label):
    s=str(random.choice([1,2,3,4,5,6]))
    label['text']=s
fun()
