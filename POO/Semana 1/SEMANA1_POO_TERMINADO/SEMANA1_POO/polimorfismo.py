#PERMITE UTILIZAR UN MISMO METODO CON DIFERENTE OBJETOS
#PERO CADA CLASE PUEDE PROPORCIONAR SU PROPIA
#IMPLEMENTACION

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
    #SOBREESCRIBIR EL METODO DE LA CLASE PADRE
    def mostrar_datos(self):
        print("Tecnico: ",self.nombre)  
        print("Especialidad: ",self.especialidad) 
        print("Salario: ",self.salario)  

#OTRA CLASE HIJA
class Gerente(Empleado):
    def __init__(self, nombre, salario,bono):
        super().__init__(nombre, salario)
        self.bono=bono
    #CADA CLASE PRESENTA LA INF. DE MANERA DIFERENTE
    def mostrar_datos(self):
        print("Gerente: ",self.nombre) 
        print("Salario: ",self.salario) 
        print("Bono: ",self.bono) 

#CREAMOS DIFERENTES OBJETOS
empleados=[
    EmpleadoTecnico("Carlos Igor",1750,"SGBD"),
    Gerente("Lucia",15000,6800)
]
#POLIMORFISMO
#TEN PRESENTE QUE TODOS UTILIZAN mostrar_datos(), pero
#CADA OBJETO EJECUTA SU PROPIA VERSION DEL METODO
for empleado in empleados:
    empleado.mostrar_datos()