#UN ATRIBUTO PUBLICO SE ESCRIBE NORMALMENTE COMO self.nombre
class Estudiante:
    def __init__(self,nombre):
        self.nombre=nombre

estudiante1=Estudiante("Susana Alcantara")
print(estudiante1.nombre)

#TAMBIEN PODEMOS MODIFICARLO
estudiante1.nombre="Susana Chavez"
print(estudiante1.nombre)