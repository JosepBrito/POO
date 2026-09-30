class Persona:
    #CONSTRUCTOR
    def __init__(self,nombre, edad, dni):
        self.nombre=nombre
        self._edad=edad
        self.__dni=dni
    #METODO MOSTRAR DATOS
    def mostrar_datos(self):
        print("Nombre: ",self.nombre)
        print("Edad: ",self._edad)
        print("DNI: ",self.__dni)
#CREAR EL OBJETO
persona1=Persona("Carlos",35,"45335985")
#RESULTADOS
print("ATRIBUTO PUBLICO")
print(persona1.nombre)
print()
print("ATRIBUTO PROTEGIDO")
print(persona1._edad)
print()
print("ATRIBUTO PRIVADO")
persona1.mostrar_datos()