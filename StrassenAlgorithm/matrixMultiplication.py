from tkinter import *
from tkinter import filedialog
from tkinter import messagebox

def actionButton():
    multiplications()
    closeWindow()

def multiplications():
    file1 = filedialog.askopenfilename(filetypes=(("Text files", "*.txt"), ("all files", "*.*")))
    file2 = filedialog.askopenfilename(filetypes=(("Text files","*.txt"),("all files","*.*")))
    messagebox.showinfo("Resultado", "El resultado se muestra en consola")
    file1Ready = open(file1).read()
    file2Ready = open(file2).read()



def closeWindow():
    ventana.destroy()

ventana = Tk()
ventana.title("Multiplicación de matrices")
ventana.geometry('725x600')
etiqueta1 = Label(ventana,text="Algoritmos de multiplicación de matrices", font=("Arial",30))
etiqueta2 = Label(ventana,text="Desarrollado por Jordan Gonzalez y Eduardo Gallegos", font=("Arial",20))
etiqueta3 = Label(ventana,text="Dale click al botón para comenzar", font=("Arial",15))
etiqueta4 = Label(ventana,text="Escoge las dos matrices a multiplicar en formato .txt", font=("Arial", 15))
etiqueta5 = Label(ventana,text="Y deja que el programa haga el resto", font=("Arial", 15))
#btn1 = Button(ventana, text="Escoge la primer matriz", command=chooseFile1)
#btn2 = Button(ventana, text="Escoge la segunda matriz ", command=chooseFile2)
btn3 = Button(ventana, text="Hacer las multiplicaciones", command=actionButton)
etiqueta1.grid(column=0, row=0)
etiqueta2.grid(column=0,row=1)
etiqueta3.grid(column=0, row=2)
etiqueta4.grid(column=0, row=3)
etiqueta5.grid(column=0, row=4)
#btn1.grid(column=0, row = 3)
#btn2.grid(column=0, row=4)
btn3.grid(column=0, row=5)
ventana.mainloop()