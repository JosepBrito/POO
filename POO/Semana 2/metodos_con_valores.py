#UN METODO TAMBIEN PUEDE DEVOLVER INFORMACION UTILIZANDO EL RETURN
class Calculadora:
    def sumar(self,n1,n2):
        return n1+n2

calculadora=Calculadora()

resultado=calculadora.sumar(26.25,19)

print("Resultado: ",resultado)