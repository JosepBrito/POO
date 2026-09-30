# LA HERENCIA SIMPLE OCURRE CUANDO UNA CLASE DERIVA DE UNA SOLA CLASE
class Vehiculo:
    def arrancar(self):
        print("El vehiculo ha arrancado")
        
class Auto(Vehiculo):
    def conducir(self):
        print("El auto está avanzando")
        
auto1 = Auto()

auto1.arrancar()
auto1.conducir()

















