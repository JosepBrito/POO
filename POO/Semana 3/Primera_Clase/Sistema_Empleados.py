# IMPORTAMOS LAS BIBLIOTECAS A UTILIZAR
import tkinter as tk 
from tkinter import ttk, messagebox

# CLASE BASE
class Empleado:
    def __init__(self, nombre, dni, edad, cargo, salario):
        # PUBLICO
        self.nombre = nombre
        self.cargo = cargo
        self.salario = salario
        # PROTEGIDO
        self._dni = dni
        # PRIVADO
        self.__edad = edad
    
    # METODO PUBLICO
    def mostrar_informacion(self):
        return (
            f"Nombre : {self.nombre}\n"
            f"DNI    : {self._dni}\n"
            f"Edad   : {self.__edad}\n"
            f"Cargo  : {self.cargo}\n"
            f"Salario: S/.{self.salario:.2f}"
        )
        
    # GETTER PARA ACCEDER AL ATRIBUTO PRIVADO
    def get_edad(self):
        return self.__edad

    # SETTER PARA MODIFICAR EL ATRIBUTO PRIVADO
    def set_edad(self,edad):
        if edad > 0:
            self.__edad = edad 
        else:
            raise ValueError("La edad debe ser mayor que 0")
    
# HERENCIA SIMPLE
class Administrativo(Empleado):
    def __init__(self, nombre, dni, edad, cargo, salario, area):
        super().__init__(nombre, dni, edad, cargo, salario)
        
        self.area = area
        
    #SOBREESCRIBIR
    def mostrar_informacion(self):
        informacion = super().mostrar_informacion()
        
        return(
            informacion +
            f"Area: {self.area}"+
            "Tipo: Administrativo"
        )
        
# OTRA CLASE DERIVADAD
class Tecnico(Empleado):
    def __init__(self, nombre, dni, edad, cargo, salario,especialidad):
        super().__init__(nombre, dni, edad, cargo, salario)
        
        self.especialidad = especialidad
        
    # SOBREESCRIBIR
    def mostrar_informacion(self):
        informacion = super().mostrar_informacion()
        
        return(
            informacion +
            f"Especialidad: {self.especialidad}"+
            "Tipo: Tecnico"
        )
                
# CLASE PARA HERENCIA MULTIPLE
class Acceso_Sistema:
    def iniciar_session(self):
        return "El empleado tiene acceso al sistema"
    
    def cerrar_session(self):
        return "Session cerrada correctamente"
    
# HERENCIA MULTIPLE
class AdministrativoTI(Administrativo, Acceso_Sistema):
    def __init__(self, nombre, dni, edad, cargo, salario, area):
        super().__init__(nombre, dni, edad, cargo, salario, area)
        
    # SOBRE ESCRITURA
    def mostrar_informacion(self):
        informacion = super().mostrar_informacion()
        return(informacion+"\nEspecialidad: Soporte Informatico")
    
# FUNCIONES DEL FORMULARIO
def registrar_empleado():
    nombre = entrada_nombre.get()
    dni = entrada_dni.get()
    edad = entrada_edad.get()
    cargo = entrada_cargo.get()
    salario = entrada_salario.get()
    tipo = combo_tipo.get()

    # VALIDACION
    if(
        nombre == "" or
        dni == "" or
        edad == "" or
        cargo == "" or
        salario == ""
    ):
        messagebox.showwarning(
            "Advertencia",
            "Todos los campos son obligatorios"
            )
        return
    try: 
        edad = int(edad)
        salario = float(salario)
        
    except ValueError:
        messagebox.showerror("Error",
                             "Edad y Salario deben ser valores numericos")
        return

    # POLIMORFISMOS
    
# INTERFAZ GRAFICA
ventana = tk.Tk()
ventana.title("Sistema de Registro de Empleados")
ventana.geometry("600x600")
ventana.resizable(False,False)

# TITULO
titulo = tk.Label(
    ventana, text = "Sistema de Registro de Empleados",
    font = ("Arial",16,"bold")
).grid(row = 0, column = 0, padx = 10, pady = 8, sticky = 'e')

# FRAME DEL FORMULARIO
frame_formulario = tk.Frame(ventana)
frame_formulario.grid(row=1, column=0, pady=10)

# NOMBRE
tk.Label(
    frame_formulario, text = "Nombre : "
).grid(row = 0, column = 0, padx = 10)

entrada_nombre = tk.Entry(
    frame_formulario, width = 35
)

entrada_nombre.grid(
    row = 0, column = 1, padx = 10, pady = 8
)

# DNI
tk.Label(frame_formulario, text="DNI : "
         ).grid(row = 1, column = 0, padx = 10, pady = 8, sticky = 'e')

entrada_dni = tk.Entry(
    frame_formulario, width = 35
)

entrada_dni.grid(row = 1, column = 1, padx = 10, pady = 8)

# EDAD
tk.Label(frame_formulario, text="Edad : "
         ).grid(row = 2, column = 0, padx = 10, pady = 8, sticky = 'e')

entrada_edad = tk.Entry(
    frame_formulario, width = 35
)

entrada_edad.grid(row = 2, column = 1, padx = 10, pady = 8)      

# CARGO
tk.Label(frame_formulario, text="Cargo : "
         ).grid(row = 3, column = 0, padx = 10, pady = 8, sticky = 'e')

entrada_cargo = tk.Entry(
    frame_formulario, width = 35
)

entrada_cargo.grid(row = 3, column = 1, padx = 10, pady = 8)      
   
# SALARIO
tk.Label(frame_formulario, text="Salario : "
         ).grid(row = 4, column = 0, padx = 10, pady = 8, sticky = 'e')

entrada_salario = tk.Entry(
    frame_formulario, width = 35
)

entrada_salario.grid(row = 4, column = 1, padx = 10, pady = 8)     

# TIPO
tk.Label(frame_formulario, text="Tipo de Empleado : "
         ).grid(row = 5, column = 0, padx = 10, pady = 8, sticky = 'e')

combo_tipo = ttk.Combobox(
    frame_formulario,
    values = [
        "Administrativo","Tecnico","Administraativo TI"],
    width = 32, state = "readonly"
)

combo_tipo.grid(row = 5, column = 0, padx = 10, pady = 8)
combo_tipo.set("Administrativo") # Primer nombre por defecto
