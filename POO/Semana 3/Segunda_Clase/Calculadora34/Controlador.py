class CalculadoraControlador:

    def __init__(self, modelo):

        self.modelo = modelo
        self.vista = None

        # Variables para guardar los datos de la operación
        self.numero1 = None
        self.numero2 = None
        self.numero_actual = None
        self.operador = None

        # Para controlar los números decimales
        self.tiene_punto = False

        # Para saber si se debe comenzar un número nuevo
        self.nuevo_numero = True

    # ---------------------------------------------------------
    # NÚMEROS
    # ---------------------------------------------------------

    def click_0(self):
        self.agregar_numero(0)

    def click_1(self):
        self.agregar_numero(1)

    def click_2(self):
        self.agregar_numero(2)

    def click_3(self):
        self.agregar_numero(3)

    def click_4(self):
        self.agregar_numero(4)

    def click_5(self):
        self.agregar_numero(5)

    def click_6(self):
        self.agregar_numero(6)

    def click_7(self):
        self.agregar_numero(7)

    def click_8(self):
        self.agregar_numero(8)

    def click_9(self):
        self.agregar_numero(9)

    # ---------------------------------------------------------
    # MÉTODO PARA AGREGAR NÚMEROS
    # ---------------------------------------------------------

    def agregar_numero(self, numero):

        if self.nuevo_numero:

            self.numero_actual = numero
            self.nuevo_numero = False

        else:

            if self.tiene_punto:

                self.numero_actual = float(
                    str(self.numero_actual) + str(numero)
                )

            else:

                self.numero_actual = (
                    self.numero_actual * 10 + numero
                )

        self.vista.insertar_texto(str(numero))

    # ---------------------------------------------------------
    # PUNTO DECIMAL
    # ---------------------------------------------------------

    def click_punto(self):

        if not self.tiene_punto:

            if self.numero_actual is None:

                self.numero_actual = 0
                self.vista.insertar_texto("0")

            self.tiene_punto = True
            self.vista.insertar_texto(".")

    # ---------------------------------------------------------
    # OPERADORES
    # ---------------------------------------------------------

    def click_sumar(self):
        self.seleccionar_operador(self.modelo.sumar, "+")

    def click_restar(self):
        self.seleccionar_operador(self.modelo.restar, "-")

    def click_multiplicar(self):
        self.seleccionar_operador(self.modelo.multiplicar, "*")

    def click_dividir(self):
        self.seleccionar_operador(self.modelo.dividir, "/")

    def click_residuo(self):
        self.seleccionar_operador(self.modelo.residuo, "%")

    def click_potencia(self):
        self.seleccionar_operador(self.modelo.potencia, "**")

    # ---------------------------------------------------------
    # GUARDAR OPERADOR
    # ---------------------------------------------------------

    def seleccionar_operador(self, operador, simbolo):

        if self.numero_actual is None:

            self.vista.mostrar_error("Falta el número")
            return

        # Si ya existe una operación pendiente,
        # primero calculamos el resultado
        if self.numero1 is not None and self.operador is not None:

            self.numero2 = self.numero_actual

            try:

                resultado = self.operador(
                    self.numero1,
                    self.numero2
                )

                self.numero1 = resultado
                self.numero2 = None

            except Exception as error:

                self.vista.mostrar_error(str(error))
                return

        else:

            self.numero1 = self.numero_actual

        # Guardamos el nuevo operador
        self.operador = operador

        # Preparamos el siguiente número
        self.numero_actual = None
        self.tiene_punto = False
        self.nuevo_numero = True

        # Mostramos el resultado y el nuevo operador
        self.vista.mostrar_entrada(
            str(self.numero1) + " " + simbolo + " "
        )

    # ---------------------------------------------------------
    # CALCULAR
    # ---------------------------------------------------------

    def calcular(self):

        if self.numero1 is None:

            self.vista.mostrar_error("Falta el primer número")
            return

        if self.operador is None:

            self.vista.mostrar_error("Falta el operador")
            return

        if self.numero_actual is None:

            self.vista.mostrar_error("Falta el segundo número")
            return

        self.numero2 = self.numero_actual

        try:

            resultado = self.operador(
                self.numero1,
                self.numero2
            )

            self.vista.mostrar_resultado(str(resultado))

            # El resultado se convierte en el nuevo primer número
            self.numero1 = resultado
            self.numero2 = None
            self.numero_actual = resultado
            self.operador = None

            self.tiene_punto = False
            self.nuevo_numero = True

            # Mostramos solamente el resultado
            self.vista.mostrar_entrada(str(resultado))

        except Exception as error:

            self.vista.mostrar_error(str(error))

    # ---------------------------------------------------------
    # LIMPIAR
    # ---------------------------------------------------------

    def limpiar(self):

        self.numero1 = None
        self.numero2 = None
        self.numero_actual = None
        self.operador = None

        self.tiene_punto = False
        self.nuevo_numero = True

        self.vista.limpiar_entrada()
        self.vista.mostrar_resultado("")

    # ---------------------------------------------------------
    # BORRAR
    # ---------------------------------------------------------

    def borrar(self):

        if self.numero_actual is None:
            return

        texto = str(self.numero_actual)

        # Si solamente queda un número
        if len(texto) == 1:

            self.numero_actual = None
            self.nuevo_numero = True
            self.tiene_punto = False

            self.vista.mostrar_entrada("")

            return

        # Eliminar el último carácter
        texto = texto[:-1]

        # Si queda un punto al final
        if texto.endswith("."):

            texto = texto[:-1]
            self.tiene_punto = False

        # Convertir nuevamente a número
        if texto == "":

            self.numero_actual = None
            self.nuevo_numero = True

            self.vista.mostrar_entrada("")

        elif "." in texto:

            self.numero_actual = float(texto)

            self.vista.mostrar_entrada(texto)

        else:

            self.numero_actual = int(texto)

            self.vista.mostrar_entrada(texto)