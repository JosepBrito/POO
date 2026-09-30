class CalculadoraControlador:

    def __init__(self, modelo):

        self.modelo = modelo
        self.vista = None

        # Los números se guardan como números
        self.numero1 = None
        self.numero2 = None

        # El operador será una función del Modelo
        self.operador = None

        # Control del número que se está escribiendo
        self.numero_actual = None
        self.tiene_punto = False
        self.cantidad_decimales = 0

        # Sirve para saber si acabamos de obtener un resultado
        self.nuevo_numero = False

    # ---------------------------------------------------------
    # TECLAS NUMÉRICAS
    # ---------------------------------------------------------

    def click_0(self):
        self._agregar_numero(0)

    def click_1(self):
        self._agregar_numero(1)

    def click_2(self):
        self._agregar_numero(2)

    def click_3(self):
        self._agregar_numero(3)

    def click_4(self):
        self._agregar_numero(4)

    def click_5(self):
        self._agregar_numero(5)

    def click_6(self):
        self._agregar_numero(6)

    def click_7(self):
        self._agregar_numero(7)

    def click_8(self):
        self._agregar_numero(8)

    def click_9(self):
        self._agregar_numero(9)

    # ---------------------------------------------------------
    # AGREGAR NÚMEROS
    # ---------------------------------------------------------

    def _agregar_numero(self, numero):

        # Si acabamos de obtener un resultado,
        # empezamos una nueva operación
        if self.nuevo_numero:

            self.numero1 = None
            self.numero2 = None
            self.operador = None

            self.numero_actual = None
            self.tiene_punto = False
            self.cantidad_decimales = 0

            self.nuevo_numero = False

            self.vista.limpiar_entrada()

        # Si todavía no estamos escribiendo ningún número
        if self.numero_actual is None:

            self.numero_actual = numero

        # Si estamos escribiendo la parte decimal
        elif self.tiene_punto:

            self.cantidad_decimales += 1

            self.numero_actual = (
                self.numero_actual
                + numero / (10 ** self.cantidad_decimales)
            )

            self.numero_actual = round(
                self.numero_actual,
                self.cantidad_decimales
            )

        # Si estamos escribiendo la parte entera
        else:

            self.numero_actual = (
                self.numero_actual * 10
            ) + numero

        self._mostrar_operacion()

    # ---------------------------------------------------------
    # PUNTO DECIMAL
    # ---------------------------------------------------------

    def click_punto(self):

        if self.numero_actual is None:

            self.numero_actual = 0

        if not self.tiene_punto:

            self.tiene_punto = True
            self.cantidad_decimales = 0

        self._mostrar_operacion()

    # ---------------------------------------------------------
    # OPERADORES
    # ---------------------------------------------------------

    def click_sumar(self):
        self._seleccionar_operador(self.modelo.sumar)

    def click_restar(self):
        self._seleccionar_operador(self.modelo.restar)

    def click_multiplicar(self):
        self._seleccionar_operador(self.modelo.multiplicar)

    def click_dividir(self):
        self._seleccionar_operador(self.modelo.dividir)

    def click_residuo(self):
        self._seleccionar_operador(self.modelo.residuo)

    def click_potencia(self):
        self._seleccionar_operador(self.modelo.potencia)

    # ---------------------------------------------------------
    # SELECCIONAR OPERADOR
    # ---------------------------------------------------------

    def _seleccionar_operador(self, operador):

        # No se puede colocar operador sin número
        if self.numero_actual is None:
            self.vista.mostrar_error("Primero ingrese un número")
            return

        # Guardamos el número que acabamos de escribir
        if self.numero1 is None:

            self.numero1 = self.numero_actual

        # Si ya había una operación pendiente,
        # primero calculamos la anterior
        elif self.operador is not None:

            self.numero2 = self.numero_actual

            try:

                self.numero1 = self.operador(
                    self.numero1,
                    self.numero2
                )

            except Exception as error:

                self.vista.mostrar_error(str(error))
                return

        # Guardamos la nueva operación
        self.operador = operador

        # Preparamos el segundo número
        self.numero_actual = None
        self.numero2 = None
        self.tiene_punto = False
        self.cantidad_decimales = 0

        self._mostrar_operacion()

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
            self.cantidad_decimales = 0

            self.nuevo_numero = True

        except Exception as error:

            self.vista.mostrar_error(str(error))

    # ---------------------------------------------------------
    # MOSTRAR OPERACIÓN
    # ---------------------------------------------------------

    def _mostrar_operacion(self):

        texto = ""

        if self.numero1 is not None:

            texto = self._formatear_numero(self.numero1)

            if self.operador is not None:

                texto += " "
                texto += self._obtener_simbolo_operador()
                texto += " "

        if self.numero_actual is not None:

            texto += self._formatear_numero_actual()

        self.vista.mostrar_entrada(texto)

    # ---------------------------------------------------------
    # OBTENER SÍMBOLO DEL OPERADOR
    # ---------------------------------------------------------

    def _obtener_simbolo_operador(self):

        if self.operador == self.modelo.sumar:
            return "+"

        elif self.operador == self.modelo.restar:
            return "-"

        elif self.operador == self.modelo.multiplicar:
            return "*"

        elif self.operador == self.modelo.dividir:
            return "/"

        elif self.operador == self.modelo.residuo:
            return "%"

        elif self.operador == self.modelo.potencia:
            return "**"

        return ""

    # ---------------------------------------------------------
    # FORMATEAR NÚMERO
    # ---------------------------------------------------------

    def _formatear_numero(self, numero):

        if isinstance(numero, float) and numero.is_integer():

            return str(int(numero))

        return str(numero)

    # ---------------------------------------------------------
    # FORMATEAR NÚMERO ACTUAL
    # ---------------------------------------------------------

    def _formatear_numero_actual(self):

        if self.tiene_punto:

            if self.cantidad_decimales == 0:

                return str(int(self.numero_actual)) + "."

            return (
                f"{self.numero_actual:.{self.cantidad_decimales}f}"
            )

        return self._formatear_numero(self.numero_actual)

    # ---------------------------------------------------------
    # BORRAR
    # ---------------------------------------------------------

    def borrar(self):

        if self.numero_actual is None:
            return

        # Si estamos borrando decimales
        if self.tiene_punto and self.cantidad_decimales > 0:

            numero = int(
                self.numero_actual *
                (10 ** self.cantidad_decimales)
            )

            numero = numero // 10

            self.cantidad_decimales -= 1

            if self.cantidad_decimales == 0:

                self.numero_actual = numero
                self.tiene_punto = False

            else:

                self.numero_actual = (
                    numero / (10 ** self.cantidad_decimales)
                )

        # Si solo queda el punto
        elif self.tiene_punto:

            self.tiene_punto = False

        # Borrar un número entero
        else:

            numero = int(self.numero_actual)

            numero = numero // 10

            self.numero_actual = numero

        self._mostrar_operacion()

    # ---------------------------------------------------------
    # LIMPIAR
    # ---------------------------------------------------------

    def limpiar(self):

        self.numero1 = None
        self.numero2 = None
        self.operador = None

        self.numero_actual = None

        self.tiene_punto = False
        self.cantidad_decimales = 0

        self.nuevo_numero = False

        self.vista.limpiar_entrada()
        self.vista.mostrar_resultado("")