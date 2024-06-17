from tkinter import *
import tkinter as tk
 

i = tk.Tk()
i.title('My i')
i.geometry('250x250')
 

Nome=Label(i,width=20, text='Você é Maior de Idade? : ')


 
def Checar():
    if (var1.get() == 1) & (var2.get() == 0):
        Nome.config(text='SIM, sou Maior de Idade ')
    elif (var1.get() == 0) & (var2.get() == 1):
        Nome.config(text='NÃO, sou Menor de Idade')
    elif (var1.get() == 0) & (var2.get() == 0):
        Nome.config(text='Voce é Maior de Idade? :')
    else:
        Nome.config(text='Resposta Incoerente:')
 
var1 = tk.IntVar()
var2 = tk.IntVar()

c1 = tk.Checkbutton(i, text='SIM',variable=var1, onvalue=1, offvalue=0, command=Checar)
c1.pack()
c1.place(x='90', y='30')

c2 = tk.Checkbutton(i, text='NAO',variable=var2, onvalue=1, offvalue=0, command=Checar)
c2.pack()
c1.place(x='30', y='30')
 
i.mainloop()