from tkinter import *
from tkinter import filedialog
from tkinter import ttk
from tkinter import messagebox

from conf import SAMPLE_INPUTS, SAMPLE_OUTPUTS
import tkinter as tk
import os
from creadorDeImg import imagen_1, imagen_2, imagen_3, imagen_4, imagen_5


root = tk.Tk()

dia = ""
dirSave=""
dirFile=""
num = 0

def center(toplevel):
       toplevel.update_idletasks()
       w = toplevel.winfo_screenwidth()
       h = toplevel.winfo_screenheight()
       size = tuple(int(_) for _ in toplevel.geometry().split('+')[0].split('x'))
       x = w/2 - size[0]/2
       y = h/2 - size[1]/1.5
       toplevel.geometry("%dx%d+%d+%d" % (size + (x, y)))
     
if __name__ == '__main__':
       root.geometry('500x300')
       root.title("Capsulador")
       center(root)


def refresh():
    if  dirSave != "":
        button3 = Button(root,text="Ejecutar",state=NORMAL, command=ejecutarPrograma)
        button3.grid(row=11,column=2)

def openFile():
    global dirFile
    dirFile = filedialog.askopenfilename(title="Abrir")
    refresh()

def saveIn():
    global dirSave 
    dirSave = filedialog.askdirectory(title="Guardar")
    refresh()

def ejecutarPrograma():
    global dirSave, dirFile, png_1, png_2, png_3, png_4, png_5
    titulo = box.get()
    dia = cb.get()
    num = boxNum.get()
    png_1 = imagen_1(dia,titulo,num)
    png_2 = imagen_2(dia,titulo,num)
    png_3 = imagen_3(dia,titulo,num)
    png_4 = imagen_4(dia,titulo,num)
    png_5 = imagen_5(dia,titulo,num)
    x = messagebox.askyesno(message="¿Desea continuar?", title="")
    if x:
        png_1.save(os.path.join(dirSave,'Capsula_'+num+'_1.png'))
        png_2.save(os.path.join(dirSave,'Capsula_'+num+'_2.png'))
        png_3.save(os.path.join(dirSave,'Capsula_'+num+'_3.png'))
        png_4.save(os.path.join(dirSave,'Capsula_'+num+'_4.png'))
        png_5.save(os.path.join(dirSave,'Capsula_'+num+'_5.png'))


cb = ttk.Combobox(root,state='readonly')
cb['values'] = ('Lunes-Jueves','Martes-Viernes','Miercoles-Sábado')
cb.current(0)

box = Entry(root)
boxNum = Entry(root)

lbl = Label(root, text="CAPSULADOR APOSTÓLICO BY DIEGO MARTÍNEZ")
lblV1 = Label(root, text="                        ")

lblV4 = Label(root, text="¿Dónde desea guardarlo?")
lblV5 = Label(root, text="¿Qué día de la semana?")
lblV6 = Label(root, text="Nombre de la capsula:")
lblV7 = Label(root, text="Número de la capsula:")
lblV9 = Label(root, text="")


button2 = Button(root,text="Guardar en", command=saveIn)
button3 = Button(root,text="Ejecutar",state=DISABLED,command=ejecutarPrograma)

lblV1.grid(row=0,column=0)
lbl.grid(row=0,column=1)
lblV4.grid(row=4,column=1)
button2.grid(row=5,column=1)
lblV5.grid(row=6,column=1)
cb.grid(row=7,column=1)
lblV6.grid(row=8,column=1)
box.grid(row=9,column=1)
lblV7.grid(row=10,column=1)
button3.grid(row=11,column=2)
boxNum.grid(row=11,column=1)

root.mainloop()
