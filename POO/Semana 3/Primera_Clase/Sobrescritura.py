# LA SOBREESCRITURA OCURRE CUANDO UNA CLASE HIJA MODIFICA EL
# COMPORTAMIENTO DE METODO HEREDADO
class Animal:
    def hacer_ruido(self):
        print("El animal hacer un sonido: ")
        
class Perro(Animal):
    def hacer_ruido(self):
        print("El perro dice: 🌭🌭🌭 ¡Guau! 🌭🌭🌭")

class Gato(Animal):
    def hacer_ruido(self):
        print("El gato dice : 🙀🙀🙀 ¡Miau! 🙀🙀🙀")

animal = Animal()
perro = Perro()
gato = Gato()

animal.hacer_ruido()
perro.hacer_ruido()
gato.hacer_ruido()





