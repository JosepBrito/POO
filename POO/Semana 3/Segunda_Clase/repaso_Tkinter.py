# PRIMER PASO -> IMPORTAR LAS BIBLIOTECAS
# IMPORTAMOS "tkinter" Y LE COLOCAMOS UN ALIAS "tk"

import tkinter as tk

# IMPORTAMOS "messagebox" PARA MOSTRAR MENSAJES EMERGENTES

from tkinter import messagebox

# SEGUNDO PASO -> CREAR LA VENTANA PRINCIPAL
# CREAMOS LA VENTANA PRINCIPAL

ventana = tk.Tk()

# COLOCAMOS UN TITULO
ventana.title("HAKUNA MATATA")

# DEFINIR EL TAMAÑO DE LA VENTANA
ventana.geometry("400x300")

# TERCER PASO -> CREACION DE TEXTOS ('LABEL')

# TEXTO PARA EL NOMBRE
tk.Label(ventana, text = "Nombre : ").pack()

# CAMPO PARA ESCRIBIR EL NOMBRE
entrada_nombre = tk.Entry(ventana)
entrada_nombre.pack()

# TEXTO PARA LA EDAD
tk.Label(ventana, text = "Edad : ").pack()

# CAMPO PARA ESCRIBIR LA EDAD
entrada_edad = tk.Entry(ventana)
entrada_edad.pack()

# TEXTO PARA EL CORREO
tk.Label(ventana, text = "Correo : ").pack()

# CAMPO PARA ESCRIBIR EL CORRE
entrada_correo = tk.Entry(ventana)
entrada_correo.pack()

# CUARTO PASO -> CREAR FUNCION GUARDAR
# ESTA FUNCION SE EJECUTARA CUANDO EL USUARIO PRESIONE EL BOTON GUARDAR
def Guardar ():
    
    # HAY QUE OBTENER EL TEXTO ESCRITO DE LOS CAMPOS (NOMBRE, EDAD Y CORREO)
    Nombre = entrada_nombre.get()
    Edad = entrada_edad.get()
    Correo = entrada_correo.get()
    
    # MOSTRA LOS DATOS EN UNA VENTANA DE MENSAJE
    messagebox.showinfo(
        "Registro",
        "\nNombre : " + Nombre +
        "\nEdad : " + Edad +
        "\nCorreo : " + Correo
        )

# CREAMOS LA FUNCION LIMPIAR
def Limpiar():
    # BORRAMOS EL CONTENIDO DEL CAMPO (NOMBRE, EDAD Y CORREO) 
    entrada_nombre.delete(0,tk.END)
    entrada_edad.delete(0,tk.END)
    entrada_correo.delete(0,tk.END)

# SEXTO PASO - > CREAR LOS BOTONES
# BOTON GUARDAR
Boton_Guardar = tk.Button(
    ventana,  # LLAMA AL FORMULARIO
    text = "Guardar", # INGRESA UN NOMBRE AL BOTON
    command = Guardar # AÑADIR LA FUNCION AL BOTON
    ) 

# VISUALIZAR LE BOTON
Boton_Guardar.pack(pady = 10)

# BOTON LIMPIAR
Boton_Limpiar = tk.Button(
    ventana,  # LLAMA AL FORMULARIO
    text = "Limpiar", # INGRESA UN NOMBRE AL BOTON
    command = Limpiar # AÑADIR LA FUNCION AL BOTON
    ) 

# VISUALIZAR LE BOTON
Boton_Limpiar.pack(pady = 10)

# PASO FINAL -> VISUALIZAR TKINTER
ventana.mainloop()













