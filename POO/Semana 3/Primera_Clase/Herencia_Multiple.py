# PYTHON SI PERMITE QE UNA CLASE HEREDE DE MAS DE UNA CLASE
class Volador:
    def Volar(self):
        print("Puede Volar Igor?")
        

class Nadador:
    def Nadar(self):
        print("Puede Nadar Rabir?")

class Pato(Volador,Nadador):
    def caminar(self):
        print("Puede caminar Donal")
        
        
pato1 = Pato()

pato1.Volar()
pato1.Nadar()
pato1.caminar()











