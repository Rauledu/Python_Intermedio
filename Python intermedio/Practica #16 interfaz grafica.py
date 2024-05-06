import tkinter
import tkinter.messagebox
from tkinter import *
from PIL import ImageTk, Image
import ModuloTest
#-------------------------------Ventana-------------------

ventana = tkinter.Tk()
ventana.title("Practica inventario")
ventana.geometry("500x500")
ventana.resizable(0,0)

#--------------------------Etiqueta-----------------------

cabecera = tkinter.Label(ventana, text = "           Bienvenidos").pack()

#----------------------------Boton-------------------------{{Practica 17}}

def saludo():
    tkinter.Label(ventana, text = "Hola mundo").pack()

def salir():
    ventana.destroy()
    

btn = tkinter.Button(ventana, text = "Invoca un saludo", command = saludo, fg="red")
btn.pack()
btn.place(x=180, y=200, height=75, width= 150)

btn_2 = tkinter.Button(ventana, text = "Salir", command = salir, fg="red")
btn.pack()
btn_2.place(x=180, y=350, height=75, width= 150)



#------------------------------Cuadro de mensaje----------{{Practica 18}}-----------------------#

#tkinter.messagebox.showinfo("Test", "Normal Message")

# respuesta = tkinter.messagebox.askquestion("Eres nuevo?","Te gusta Python?")

# if respuesta == "yes":
#     tkinter.messagebox.showinfo("","Felicidades has dado el primer paso, tu puedes")
# else:
#     tkinter.messagebox.showinfo("","Espero consigas un lenguaje de programacion que te guste de verdad.")


#Practica 19--------------------Insertar imagen-----------------------------#

# img = tkinter.PhotoImage(file="python.png")
# lbl_img = tkinter.Label(ventana, image = img)
# lbl_img.pack()

#Practica 20----------------------REDIMENSIONAR una IMAGEN con TKINTER y PILLOW

# imagen = Image.open("python.png")
# imagen = imagen.resize((80, 100),Image.ANTIALIAS)

# img = ImageTk.PhotoImage(imagen)
# lbl_img = Label(ventana, image = img)
# lbl_img.pack()

#Practica {{21}} LISTBOX con TKINTER Conectado a SQL#

lista = tkinter.Listbox(ventana)

product = ModuloTest.consulta(ModuloTest.connection)
# index= 0

# for Prod in product:
#     lista.insert(index, Prod)
#     index = index +1

for index, prod in enumerate(product):
    lista.insert(index,prod[1])


#Practica {{22}} Seleccionado en un LISTBOX con TKINTER#

def itemseleccionado():
    for item in lista.curselection():
        lb = tkinter.Label(ventana, text = lista.get(item)).pack()
        
btnselected = tkinter.Button(ventana, text = "Item seleccionado", command = itemseleccionado)
btnselected.pack()
lista.pack()


#Practica {{23}}INGRESAR DATOS DEL USUARIO CON ENTRY-Ultima practica#

lbltxt = Label(ventana, text = "Nombre a buscar ").pack()
Txtbox = Entry(ventana, fg = "Blue" , show ="*")
Txtbox.pack()

def buscar():
    flag = 0
    
    for prod in product:
        if prod[1] == Txtbox.get():
            flag = flag +1
            LB =Label(ventana, text = prod).pack()
    if flag == 0:
        tkinter.messagebox.showinfo("", "No se encontro el nombre: "+ Txtbox.get())

btn_ = Button(ventana, text = "Buscar", command= buscar).pack()

ventana.mainloop()