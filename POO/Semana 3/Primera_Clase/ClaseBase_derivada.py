# EN PYTHON, UNA CLASE DERIVADA SE CREA COLOCANDO LA CLASE BASE
# ENTRE PARENTESIS
class Animal: # Clase base o padre
    def comer(self): # Metodo heredado
        print("El animal esta comiendo")
        
class Perro(Animal): # Clase derivada o hija
    def ladra(self): # Metodo propio del Perro
        print("El perro esta ladrando")
        
perro1 = Perro()

perro1.comer() # Metodo heredado
perro1.ladra() # Metodo propio





