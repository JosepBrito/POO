#UNA DE LAS VENTAJAS DE LAS CLASES ES QUE PODEMOS CREAR MUCHOS OBJETOS
#SE CREA LA CLASE ESTUDIANTE CON SUS ATRIBUTOS DE name - edad - curso
class Estudiante:
    def __init__(self,name,edad,curso):
        self.name=name
        self.edad=edad
        self.curso=curso

#CREAMOS MULTIPLES OBJETOS
estudiante1=Estudiante("Rabbit",16,"IOT")
estudiante2=Estudiante("Tigger",19,"PYTHON")
estudiante3=Estudiante("Oso",26,"JAVA")

#VISUALIZAR --> CADA OBJETO TIENE SUS PROPIOS DATOS
print(estudiante1.name)
print(estudiante2.edad)
print(estudiante3.curso)