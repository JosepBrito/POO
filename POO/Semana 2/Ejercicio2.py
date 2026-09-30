#VAMOS A CREAR CLASE CON ATRIBUTOS
class Estudiante:
    def __init__(self,nombre,edad,carrera):
        self.nombre=nombre
        self.edad=edad
        self.carrera=carrera
        
estudiante1=Estudiante(
    "IGOR",
    35,
    "Ingenieria Civil"
)

print("Nombre: ",estudiante1.nombre)
print("Edad: ",estudiante1.edad)
print("Carrera: ",estudiante1.carrera)