#AHORA PODEMOS COMBINAR AMBOS CONCEPTOS
class Estudiante:
    #CREAR EL CONSTRUCTOR
    def __init__(self,nombre,edad):
        self.nombre=nombre
        self.edad=edad
    #CREAR LOS METODOS
    def estudiar(self):
        print(self.nombre,"está estudiando")
    def presentarse(self):
        print("Hola, soy ",self.nombre)
        print("Tengo ",self.edad, "años")

estudiante1=Estudiante("Ines",19)
#LLAMAR A LOS METODOS
estudiante1.presentarse()
estudiante1.estudiar()

