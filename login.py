from tkinter import *
from tkinter import messagebox
from pymongo import MongoClient
import uuid
from tkinter import ttk
import tkinter.font as tkFont
import easygui as eg
from PIL import Image, ImageTk
import numpy as np
import cv2
import tkinter as tk
from tkinter import filedialog

#estoy probando el git de escritorio
mongoClient = MongoClient('localhost',27017)
db = mongoClient.softmaiznew
collection = db 

#Validaciones del login
def validar():
    user=db.Usuarios.find_one({"tipo":entrada1.get(),"password":entrada2.get()})
    
    if entrada1.get()=='admin':
        if user:
            abrirmenu()
        else:
            messagebox.showwarning("Cuidado","Dato incorrecto")
    elif entrada1.get()=='user':
        if user:
            abrirmenuoperario()
        else:
            messagebox.showwarning("Cuidado","Dato incorrecto")
    else:
        messagebox.showwarning("Cuidado","Dato incorrecto")

#Validaciones del registro
def coni():
    cadena=Nombres.get()
    patron="([A-Za-z])"
    cadena1=Correo.get()
    patron1="[A-Za-z]+((.+|_+)([a-z]+|(\d+)))?@[A-Za-z]+.com$"
    cadena2=Edad.get()
    patron2="\d{2}$"
    cadena3=Identificaion.get()
    patron3="\d{10}$"
    cadena4=Apellidos.get()
    if(re.match(patron,cadena)):
        if(re.match(patron1,cadena1)):
            if(re.match(patron2,cadena2)):
                if(re.match(patron3,cadena3)):
                    if(re.match(patron,cadena4)):
                        print("formulario de registro correcto")
                        messagebox.showinfo("Registro","Formulario realizado correctamente")
                        database()
                    else:
                        messagebox.showwarning("Cuidado","Apellidos no valido ")
                else:
                    messagebox.showwarning("Cuidado","Identificación no valido ")
            else:
                messagebox.showwarning("Cuidado","Edad no valido")
        else:
            messagebox.showwarning("Cuidado","Correo no valido")
    else:
        messagebox.showwarning("Cuidado","Nombre no valido")

def limpiar():
    Fecha_produccion.set("")
    Identificaion.set("")
    Mazorcas.set("")
    Mazorcasnocomercial.set("")
    Mazorcascomercial.set("")
    Nombres.set("")
    Apellidos.set("")
    Edad.set("")
    Correo.set("")
    Password.set("")

def database():
    identificaion=Identificaion.get()
    nombres=Nombres.get()
    apellidos=Apellidos.get()
    edad=Edad.get()
    correo=Correo.get()
    tipo=Tipo.get()
    password=Password.get()
    estado=Estado.get()
    db.Usuarios.insert_one({"identificaion": identificaion,"nombres": nombres, "apellidos": apellidos,"edad": edad,
                                "correo": correo,"tipo": tipo,"password": password,"estado": estado})

def registrarusu():
    ventana.deiconify()
    new = tk.Toplevel()
    new.geometry("450x550+700+5")
    new.configure(background='sea green')
    new.title("Registrar Usuario")
    
    Label(new,text="Digite el siguiente formulario").pack(padx=5,pady=5,ipadx=5,ipady=5)

    Label(new,text="Identificacion: ", font=("Agency FB",14)).place(x=10,y=45)
    entry_1 = tk.Entry(new,textvar=Identificaion)
    entry_1.pack(padx=5,pady=5,ipadx=5,ipady=5)

    Label(new,text="Nombre: ", font=("Agency FB",14)).place(x=10,y=85)
    entry_11 = tk.Entry(new,textvar=Nombres)
    entry_11.pack(padx=5,pady=5,ipadx=5,ipady=5)

    Label(new,text="Apellido: ", font=("Agency FB",14)).place(x=10,y=125)
    entry_4 = tk.Entry(new,textvar=Apellidos)
    entry_4.pack(padx=5,pady=5,ipadx=5,ipady=5)

    Label(new,text="Edad: ", font=("Agency FB",14)).place(x=10,y=165)
    entry_5= tk.Entry(new,textvar=Edad)
    entry_5.pack(padx=5,pady=5,ipadx=5,ipady=5)

    Label(new,text="Correo: ", font=("Agency FB",14)).place(x=10,y=205)
    entry_2= tk.Entry(new,textvar=Correo)
    entry_2.pack(padx=5,pady=5,ipadx=5,ipady=5)

    Label(new,text="Password: ", font=("Agency FB",14)).place(x=10,y=245)
    entry_6= tk.Entry(new,textvar=Password, show="*")
    entry_6.pack(padx=5,pady=5,ipadx=5,ipady=5)

    Label(new,text="Rol: ", font=("Agency FB",14)).place(x=10,y=295)

    Radiobutton(new, text="User",padx = 5, variable=Tipo, value="user").pack(padx=4,pady=4,ipadx=4,ipady=4)
    Radiobutton(new, text="Admin",padx = 20, variable=Tipo, value="admin").pack(padx=4,pady=4,ipadx=4,ipady=4)

    Label(new,text="Estado: ", font=("Agency FB",14)).place(x=10,y=365)
    list1 = [True,False]

    droplist=OptionMenu(new,Estado, *list1)
    droplist.config(width=15)
    Estado.set(value=1) 
    droplist.pack(padx=4,pady=4,ipadx=4,ipady=4)

    Button(new,text="Registrar",bg='brown', font=("black",12),command=coni).place(x=10,y=445)
    Button(new,text="Buscar",bg='brown', font=("black",12),command=traer).place(x=92,y=445)
    Button(new,text="Actualizar",bg='brown', font=("black",12),command=actualizarusu).place(x=160,y=445)
    Button(new,text="Borrar",bg='brown', font=("black",12),command=limpiar).place(x=245,y=445)

    Button(new,text="Cerrar",bg='orange', font=("black",12),command=new.destroy).place(x=100,y=490)
#-----------------ventana-de-produccion------------------------------

def ValidarProduccion():
    cadena5=Fecha_produccion.get()
    patron5="(0[1-9]|[1-2][0-9]|3[0-1])\/(0[1-9]|1[0-12])\/(19|20)\d\d$"
    cadena6=Identificaion.get()
    patron6="\d{10}$"
    cadena7=Nombres.get()
    patron7="([A-Za-z])"
    cadena8=Mazorcas.get()
    patron8="(-|\+)?([0-9]{1,4})+.?[0-9]{1,4}"
    cadena9=Mazorcascomercial.get()
    patron9="(-|\+)?([0-9]{1,4})+.?[0-9]{1,4}"
    cadena10=Mazorcasnocomercial.get()
    patron10="(-|\+)?([0-9]{1,4})+.?[0-9]{1,4}"
    if(re.match(patron5,cadena5)):
        if(re.match(patron6,cadena6)):
            if(re.match(patron7,cadena7)):
                if(re.match(patron8,cadena8)):
                    if(re.match(patron9,cadena9)):
                        if(re.match(patron10,cadena10)):
                            print("formulario de producción correcto")
                            messagebox.showinfo("Producción","Formulario realizado correctamente")
                            database_produc()
                        else:
                            messagebox.showwarning("Cuidado","valor de mazorcas no comerciales no valido ")
                    else:
                        messagebox.showwarning("Cuidado","valor de mazorcas comerciales no valido ")
                else:
                    messagebox.showwarning("Cuidado","total de mazorcas no valido ")
            else:
                messagebox.showwarning("Cuidado","Nombres no valido")
        else:
            messagebox.showwarning("Cuidado","indetificación incorrecta")
    else:
        messagebox.showwarning("Cuidado","Fecha de produccion incorrecta")

def RegistrarProduccion():
    
    ventana.deiconify()
    new = tk.Toplevel()
    new.geometry("500x500+700+5")
    new.configure(background='sea green')
    new.title("Registrar Produccion")
    Label(new,text="Digite el siguiente formulario").pack(padx=5,pady=5,ipadx=5,ipady=5)

    Label(new,text="Fecha de produccion: ", font=("Agency FB",14)).place(x=10,y=45)
    entry_17 = tk.Entry(new,textvar=Fecha_produccion)
    entry_17.pack(padx=5,pady=5,ipadx=5,ipady=5)

    Label(new,text="Identificacion: ", font=("Agency FB",14)).place(x=10,y=85)
    entry_1  = tk.Entry(new,textvar=Identificaion)
    entry_1 .pack(padx=5,pady=5,ipadx=5,ipady=5)

    Label(new,text="Nombre: ", font=("Agency FB",14)).place(x=10,y=125)
    entry_11= tk.Entry(new,textvar=Nombres)
    entry_11.pack(padx=5,pady=5,ipadx=5,ipady=5)

    label_4 = Label(new, text="------------Conteo de mazorcas------------",fg="black" )
    label_4.pack(padx=4,pady=4,ipadx=4,ipady=4)

    Label(new,text="Total Mazorcas: ", font=("Agency FB",14)).place(x=10,y=200)
    entry_5= tk.Entry(new,textvar=Mazorcas)
    entry_5.pack(padx=5,pady=5,ipadx=5,ipady=5)

    label_4 = Label(new, text="------------Verificacion de calidad------------",fg="black")
    label_4.pack(padx=4,pady=4,ipadx=4,ipady=4)    

    Label(new,text="Mazorcas comerciales: ", font=("Agency FB",14)).place(x=10,y=275)
    entry_2= tk.Entry(new,textvar=Mazorcascomercial)
    entry_2.pack(padx=5,pady=5,ipadx=5,ipady=5)

    Label(new,text="Mazorcas no comerciales: ", font=("Agency FB",14)).place(x=10,y=315)
    entry_3= tk.Entry(new,textvar=Mazorcasnocomercial,)
    entry_3.pack(padx=5,pady=5,ipadx=5,ipady=5)


    Button(new, text='Guardar',width=10,bg='brown',fg='white',command=ValidarProduccion).pack(padx=4,pady=4,ipadx=4,ipady=4)
    Button(new, text='Borrar',width=10,bg='brown',fg='white',command=limpiar).pack(padx=4,pady=4,ipadx=4,ipady=4)
    boton20 = tk.Button(new,text='cerrar',bg="orange", command=new.destroy)
    boton20.pack(side=tk.TOP,padx=5,pady=5,ipadx=5,ipady=5)


def database_produc():
    fecha_produccion=Fecha_produccion.get()
    identificaion=Identificaion.get()
    nombres=Nombres.get()
    mazorcas=Mazorcas.get()
    mazorcascomercial=Mazorcascomercial.get()
    mazorcasnocomercial=Mazorcasnocomercial.get()

    db.Produccion.insert_one({"fecha_produccion": fecha_produccion,"identificaion": identificaion,"nombres": nombres,
                            "mazorcas": mazorcas,"mazorcascomercial": mazorcascomercial,"mazorcasnocomercial": mazorcasnocomercial})

def traer():
    user=db.Usuarios.find_one({"identificaion":Identificaion.get()})
    if user:
        consulta()
    else:
        messagebox.showwarning("Cuidado","Id no registrado")

def actualizarusu():
    identificaion=Identificaion.get()
    nombres=Nombres.get()
    apellidos=Apellidos.get()
    edad=Edad.get()
    correo=Correo.get()
    tipo=Tipo.get()
    password=Password.get()
    estado=Estado.get()
    db.Usuarios.update_one({"identificaion": identificaion,"nombres": nombres, "apellidos": apellidos,
    "edad": edad,"correo": correo,"tipo": tipo,"password": password,"estado": estado})


def abrirmenu():
    ventana.deiconify()
    win = tk.Toplevel()
    win.geometry("450x300+700+20")
    win.configure(background='sea green')
    win.title("Menu")
    e3 = tk.Label(win,text="Opciones Admin ",fg="black")
    e3.pack(padx=5,pady=5,ipadx=5,ipady=5,fill=tk.X)
    boton4 = tk.Button(win,text="Registro ",bg="orange", fg="black", command=registrarusu)
    boton4.pack(side=tk.TOP,padx=5,pady=5,ipadx=5,ipady=5) 
    boton2 = tk.Button(win,text='cerrar',bg="orange", command=win.destroy)
    boton2.pack(side=tk.TOP,padx=5,pady=5,ipadx=5,ipady=5)

def abrirmenuoperario():
    ventana.deiconify()
    win = tk.Toplevel()
    win.geometry("450x300+700+20")
    win.configure(background='sea green')
    win.title("Menu Operario")
    e3 = tk.Label(win,text="Opciones User ",fg="black")
    e3.pack(padx=5,pady=5,ipadx=5,ipady=5,fill=tk.X)
    boton9 = tk.Button(win,text="Contar Mazorcas",bg="orange", fg="black", command=conteo)
    boton9.pack(side=tk.TOP,padx=5,pady=5,ipadx=5,ipady=5)
    boton5 = tk.Button(win,text="Producción",bg="orange", fg="black", command=RegistrarProduccion)
    boton5.pack(side=tk.TOP,padx=5,pady=5,ipadx=5,ipady=5)
    boton11 = tk.Button(win,text='Cerrar',bg="orange", command=win.destroy)
    boton11.pack(side=tk.TOP,padx=5,pady=5,ipadx=5,ipady=5)

def tomarfoto():
    cap = cv2.VideoCapture(0)
    leido, frame = cap.read()
    if leido == True:
        nombre_foto = str(uuid.uuid4()) + ".png" # uuid4 regresa un objeto, no una cadena. Por eso lo convertimos
        cv2.imwrite(nombre_foto, frame)
        print("Foto tomada correctamente con el nombre {}".format(nombre_foto))
    else:
        print("Error al acceder a la cámara")
    cap.release()

def abre():
    
    pic = filedialog.askopenfilename ()
    #fuente de letra
    font = cv2.FONT_HERSHEY_SIMPLEX
    #Cargar la imagen
    imagen = cv2.imread(pic)
    if(imagen is None):
        print("Error: no se ha podido encontrar la imagen")
        quit()

    #convertir la imagen a hsv
    hsv = cv2.cvtColor(imagen, cv2.COLOR_BGR2HSV)
    #Rangos del color que debe quitar (blanco)
    rango_bajo = np.array([0,0,200])
    rango_alto = np.array([255, 50, 255])
    fondo = cv2.inRange(hsv, rango_bajo, rango_alto)

    mazorcas = cv2.bitwise_not(fondo)

    kernel = np.ones((3,3),np.uint8)
    mazorcas = cv2.morphologyEx(mazorcas,cv2.MORPH_OPEN,kernel)
    mazorcas = cv2.morphologyEx(mazorcas,cv2.MORPH_CLOSE,kernel)

    #contorno de los objetos que esten sobre el fondo blanco
    contours,_ = cv2.findContours(mazorcas, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(imagen, contours, -1, (0,255,0), 2)
    #mostrar el numero de objetos contornados
    print(len(contours),' Mazorcas ' )

    cv2.imshow('Final', imagen)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


def conteo():
    ventana.deiconify()
    new = tk.Toplevel()
    new.geometry("500x300+700+20")
    new.configure(background='sea green')
    new.title("Registrar Usuario")
    Label(new,text="Busqueda y Conteo",fg="black").pack(padx=5,pady=5,ipadx=5,ipady=5,fill=tk.X)
    Button(new,text="Tomar foto",bg="orange", fg="black", command= tomarfoto).pack(side=tk.TOP,padx=5,pady=5,ipadx=5,ipady=5)
    Button(new,text="Conteo",bg="orange", fg="black", command=abre).pack(side=tk.TOP,padx=5,pady=5,ipadx=5,ipady=5)
    
    boton2 = tk.Button(new,text='cerrar',bg="orange", command=new.destroy)
    boton2.pack(side=tk.TOP,padx=5,pady=5,ipadx=5,ipady=5)

def cerrarventana():
    ventana.destroy()


ventana = tk.Tk()
ventana.title("Login -- Softmaiz")
ventana.geometry("350x260+300+20")
ventana.configure(background='sea green')
load = Image.open("maiz.png")
render = ImageTk.PhotoImage(load)
img =tk.Label(ventana, image=render)
img.image = render
img.place(x=0, y=0)

es=tk.Label(ventana,text="" , fg="black").pack(padx=5,pady=5,ipadx=5,ipady=5)

e1=tk.Label(ventana,text="Tipo: ", font=("Agency FB",14)).place(x=10,y=45)
entrada1 = tk.Entry(ventana)
entrada1.pack(padx=5,pady=5,ipadx=5,ipady=5)

e2=tk.Label(ventana,text="Password: ", font=("Agency FB",14)).place(x=10,y=85)
entrada2 = tk.Entry(ventana, show = "*")
entrada2.pack(padx=5,pady=5,ipadx=5,ipady=5)

boton3 = tk.Button(ventana,text="Ingresar",bg="orange", font=("black",12),command=validar).place(x=60,y=120)

boton5 = tk.Button(ventana,text='cerrar',bg="orange", font=("black",12),command=ventana.destroy).place(x=150,y=120)

#------------Declarar variables de usuario----------------------
Identificaion=StringVar() 
Nombres=StringVar()
Apellidos=StringVar()
Edad=StringVar() 
Correo=StringVar()
Tipo = StringVar()
Password=StringVar()
Estado= BooleanVar()
#------------Declarar variables de produccion----------------------
Fecha_produccion=StringVar() 
Mazorcas=StringVar() 
Mazorcascomercial=StringVar() 
Mazorcasnocomercial=StringVar() 

ventana.mainloop()
