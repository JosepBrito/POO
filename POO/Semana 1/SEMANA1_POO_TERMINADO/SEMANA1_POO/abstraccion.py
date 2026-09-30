#La abstracción permite representar solamente las características 
#y comportamientos relevantes para el problema. En este caso se 
#consideran nombre, cargo y salario.

# Definimos una clase llamada Empleado.
# Una clase funciona como una plantilla para crear objetos.
class Empleado:

    # __init__ es el constructor.
    # Se ejecuta automáticamente cuando creamos un objeto.
    def __init__(self, nombre, cargo, salario):
        # self representa al objeto actual.
        self.nombre = nombre
        self.cargo = cargo
        self.salario = salario

    # Método para mostrar los datos del empleado.
    def mostrar_datos(self):
        print("----- DATOS DEL EMPLEADO -----")
        print("Nombre:", self.nombre)
        print("Cargo:", self.cargo)
        print("Salario:", self.salario)

    # Método para calcular el salario anual.
    def calcular_salario_anual(self):
        return self.salario * 12

    # Método para aumentar el salario.
    def aumentar_salario(self, porcentaje):
        self.salario = self.salario + (
            self.salario * porcentaje / 100
        )


# Creamos el primer objeto.
empleado1 = Empleado("Carlos", "Técnico de Sistemas", 1800)

# Creamos el segundo objeto.
empleado2 = Empleado("María", "Analista", 2500)

# Utilizamos los métodos de los objetos.
empleado1.mostrar_datos()
print("Salario anual:", empleado1.calcular_salario_anual())

empleado1.aumentar_salario(10)

print("Nuevo salario:", empleado1.salario)

