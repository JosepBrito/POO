#PERMITE CONTROLAR EL ACCESO A LOS DATOS INTERNOS DE UN OBJETO
class Empleado:
    def __init__(self,nombre,cargo,salario):
        self.nombre=nombre
        self.cargo=cargo
        #EL DOBLE GUION BAJO INDICA UN 
        #ATRIBUTO ENCAPSULADO
        self.__salario=salario
    #METODO PARA CONSULTAR EL SALARIO
    def obtener_salario(self):
        return self.__salario
    
    #METODO PARA MODIFICAR EL SALARIO 
    # DE MANERA CONTROLADA
    def aumentar_salario(self,porcentaje):
        self.__salario+=self.__salario*porcentaje/100

empleado=Empleado("Chantal","Nutricionista",2300)
print("Salario: ",empleado.obtener_salario())
empleado.aumentar_salario(35)
print("Nuevo salario: ",empleado.obtener_salario())