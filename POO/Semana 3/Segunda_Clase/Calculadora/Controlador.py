class CalculadoraControlador:

    def __init__(self, modelo):

        self.modelo = modelo
        self.vista = None

        self.numero_1 = None
        self.numero_2 = None
        self.numero_actual = None
        self.operador = None

        self.tiene_punto = False
        self.nuevo_numero = True


    # Funcion para gregar el numero
    def agregar_numero(self, numero):

        if self.nuevo_numero:

            self.numero_actual = numero
            self.nuevo_numero = False
        else:
            self.numero_actual

        self.vista.insertar_texto(str(numero))


    # Los numeros

    def click_0(self):
        self.agregar_numero(0)
    
    def click_2(self):
        self.agregar_numero(0)
    
    def click_3(self):
        self.agregar_numero(0)
    
    def click_4(self):
        self.agregar_numero(0)

    def click_5(self):
        self.agregar_numero(0)

    def click_6(self):
        self.agregar_numero(0)

    def click_7(self):
        self.agregar_numero(0)

    def click_8(self):
        self.agregar_numero(0)

    def click_9(self):
        self.agregar_numero(0)

    # Del punto

    def click_punto(self):
        self.agregar_numero(".")


    # Funcion para los operadores

    def operacion(self, operador, simbolo):
        
        if self.numero_1 is not None and self.operador is not None:
            self.numero_2 = self.numero_actual

            try:
                resultado = self.operador(
                    self.numero_1,
                    self.numero_2
                )

                self.numero_1 = resultado
                self.numero_2 = None
                self.numero_actual
            
            except Exception as error:
                return self.vista.mostrar_error(str(error))

        else:
            self.numero_1 = self.numero_actual

        self.operador = operador

        self.numero_actual = None
        self.nuevo_numero = True

        self.vista.mostrar_entrada(str(self.numero_1) + " " + simbolo + " ")
        
    # Los operadores

    def click_sumar(self):
        return self.operacion(self.modelo.sumar, "+")

    def click_restar(self):
        return self.operacion(self.modelo.restar, "-")

    def click_multiplicar(self):
        return self.operacion(self.modelo.multiplicar, "*")

    def click_dividir(self):
        return self.operacion(self.modelo.dividir, "/")

    def click_residuo(self):
        return self.operacion(self.modelo.residuo, "%")

    def click_potencia(self):
        return self.operacion(self.modelo.potencia, "**")






    def borrar(self):
    def limpiar(self):
    def calcular(self):