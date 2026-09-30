class Estudiante:
    def __init__(self, nombre, carrera, edad, codigo):
        #ATRIBUTO PUBLICO
        self.nombre = nombre
        #ATRIBUTO PUBLICO
        self.carrera = carrera
        #ATRIBUTO PROTEGIDO
        self._edad = edad
        #ATRIBUTO PRIVADO
        self.__codigo = codigo
        
    # METODO PARA MOSTRAR DATOS
    def mostrar_datos(self):
        print("Nombre del estudiante : ", self.nombre)
        print("Carrera del estudiante : ", self.carrera)
        print("La edad del estudiante : ", self._edad)
        print("El codigo del estudiantes : ", self.__codigo)
    
    # METODO APRA ESTUDIAR
    def estudiar(self, curso):
        print(self.nombre, " esta cumpliendo con el estudio de ", curso)
        
        
    # METODO PARA CAMBIAR CARRERA
    def cambiar_carrera(self, nueva_carrera):
        self.carrera = nueva_carrera
        
    # METODO PARA CONSULTAR CODIGO
    def consultar_codigo(self):
        return self.__codigo
    

# CREAR EL OBJETO
Estudiante1 = Estudiante("Danitza", "Ingenieria de Software", 18, "UA-T202620-001")

# MOSTRAR DATOS
Estudiante1.mostrar_datos()
print()

# EJECUTAR METODO ESTUDIAR
Estudiante1.estudiar("POO")
print()

# CONSULTAR CODIGO
print("Codigo: ",Estudiante1.consultar_codigo())
print()
    
# CAMBIAR CARREAR
Estudiante1.cambiar_carrera("Cote & Confección")    
print("Nueva carrera es: ", Estudiante1.carrera)

    
    
    
    
    
    
    