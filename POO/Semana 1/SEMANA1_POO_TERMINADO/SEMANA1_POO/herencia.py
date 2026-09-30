#PERMITE CREAR NUEVAS CLASES A PARTIR DE UNA CLASE
#EXISTENTE. LA CLASE HIJA PUEDE HEREDAR O REUTILIZAR
#ATRIBUTOS Y METODOS DE LA CLASE PADRE

#CLASE PADRE
class Empleado:
    def __init__(self,nombre,salario):
        self.nombre=nombre
        self.salario=salario
        
    def mostrar_datos(self):
        print("Empleado: ",self.nombre)
        print("Salario: ",self.salario)
    
#CLASE HIJA QUE HEREDA DE EMPLEADO
class EmpleadoTecnico(Empleado):
    def __init__(self, nombre, salario,especialidad):
        #super() permite utilizar el constructor
        #de la clase padre
        super().__init__(nombre, salario)
        self.especialidad=especialidad

#OTRA CLASE HIJA
class Gerente(Empleado):
    def __init__(self, nombre, salario,bono):
        super().__init__(nombre, salario)
        self.bono=bono
        
tecnico=EmpleadoTecnico(
    "Carlos",1800,"Soporte de TI"
)

gerente=Gerente(
    "Ana Lucia",15000,3900
)