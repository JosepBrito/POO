#LOS ATRIBUTOS SON LAS CARACTERISTICAS O DATOS QUE PERTENECEN A UN OBJETO
#POR EJEMPLO
#NOMBRE = "ROMULO LEON"
#EDAD = 65
#CARRERA = "INGENIERIA AMBIENTAL"
#TENER PRESENTE -> EN PYTHON NOSOTROS PODEMOS UTILIZAR:  __init__() 
#LO USAMOS PARA INICIALIZAR LOS ATRIBUTOS
#CREAMOS LA CLASE ESTUDIANTE
class Estudiante:
    #¿que significa self? -> representa el objeto actual
    def __init__(self,nombre,edad,carrera):
        self.nombre=nombre
        self.edad=edad
        self.carrera=carrera
#AHORA PODEMOS CREAR UN OBJETO
estudiante1=Estudiante("ROMULO LEON",65,"INGENIERIA AMBIENTAL")
#AHORA DEBEMOS ACCEDER A SUS ATRIBUTOS
print(estudiante1.nombre)
print(estudiante1.edad)
print(estudiante1.carrera)