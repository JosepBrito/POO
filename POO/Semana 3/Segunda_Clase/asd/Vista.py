import tkinter as tk
from tkinter import ttk


class CalculadoraVista:

    def __init__(self, ventana, controlador):

        self.ventana = ventana
        self.controlador = controlador

        self.ventana.title("Calculadora")
        self.ventana.geometry("350x580")
        self.ventana.resizable(False, False)
        self.ventana.configure(bg="#333333")

        self._crear_estilos()
        self._crear_pantalla()

        self.teclas_numericas()
        self.teclas_operadores()
        self.teclas_especiales()

        self._configurar_grid()

    # ---------------------------------------------------------
    # ESTILOS
    # ---------------------------------------------------------

    def _crear_estilos(self):

        estilo = ttk.Style()

        estilo.theme_use("clam")

        estilo.configure(
            "TButton",
            font=("Arial", 16),
            padding=10
        )

        estilo.configure(
            "Operador.TButton",
            font=("Arial", 16, "bold")
        )

        estilo.configure(
            "Igual.TButton",
            font=("Arial", 16, "bold")
        )

    # ---------------------------------------------------------
    # PANTALLA
    # ---------------------------------------------------------

    def _crear_pantalla(self):

        self.entrada = ttk.Entry(
            self.ventana,
            font=("Arial", 24),
            justify="right"
        )

        self.entrada.grid(
            row=0,
            column=0,
            columnspan=4,
            sticky="nsew",
            padx=10,
            pady=(15, 5)
        )

        self.resultado = ttk.Label(
            self.ventana,
            text="",
            font=("Arial", 14),
            anchor="e",
            background="#333333",
            foreground="#cccccc"
        )

        self.resultado.grid(
            row=1,
            column=0,
            columnspan=4,
            sticky="nsew",
            padx=10,
            pady=(0, 10)
        )

    # ---------------------------------------------------------
    # TECLAS NUMÉRICAS
    # ---------------------------------------------------------

    def teclas_numericas(self):

        # 7, 8 y 9
        boton_7 = ttk.Button(
            self.ventana,
            text="7",
            style="TButton",
            command=self.controlador.click_7
        )

        boton_7.grid(
            row=3,
            column=0,
            sticky="nsew",
            padx=5,
            pady=5
        )

        boton_8 = ttk.Button(
            self.ventana,
            text="8",
            style="TButton",
            command=self.controlador.click_8
        )

        boton_8.grid(
            row=3,
            column=1,
            sticky="nsew",
            padx=5,
            pady=5
        )

        boton_9 = ttk.Button(
            self.ventana,
            text="9",
            style="TButton",
            command=self.controlador.click_9
        )

        boton_9.grid(
            row=3,
            column=2,
            sticky="nsew",
            padx=5,
            pady=5
        )

        # 4, 5 y 6
        boton_4 = ttk.Button(
            self.ventana,
            text="4",
            style="TButton",
            command=self.controlador.click_4
        )

        boton_4.grid(
            row=4,
            column=0,
            sticky="nsew",
            padx=5,
            pady=5
        )

        boton_5 = ttk.Button(
            self.ventana,
            text="5",
            style="TButton",
            command=self.controlador.click_5
        )

        boton_5.grid(
            row=4,
            column=1,
            sticky="nsew",
            padx=5,
            pady=5
        )

        boton_6 = ttk.Button(
            self.ventana,
            text="6",
            style="TButton",
            command=self.controlador.click_6
        )

        boton_6.grid(
            row=4,
            column=2,
            sticky="nsew",
            padx=5,
            pady=5
        )

        # 1, 2 y 3
        boton_1 = ttk.Button(
            self.ventana,
            text="1",
            style="TButton",
            command=self.controlador.click_1
        )

        boton_1.grid(
            row=5,
            column=0,
            sticky="nsew",
            padx=5,
            pady=5
        )

        boton_2 = ttk.Button(
            self.ventana,
            text="2",
            style="TButton",
            command=self.controlador.click_2
        )

        boton_2.grid(
            row=5,
            column=1,
            sticky="nsew",
            padx=5,
            pady=5
        )

        boton_3 = ttk.Button(
            self.ventana,
            text="3",
            style="TButton",
            command=self.controlador.click_3
        )

        boton_3.grid(
            row=5,
            column=2,
            sticky="nsew",
            padx=5,
            pady=5
        )

        # 0 y punto
        boton_0 = ttk.Button(
            self.ventana,
            text="0",
            style="TButton",
            command=self.controlador.click_0
        )

        boton_0.grid(
            row=6,
            column=0,
            sticky="nsew",
            padx=5,
            pady=5
        )

        boton_punto = ttk.Button(
            self.ventana,
            text=".",
            style="TButton",
            command=self.controlador.click_punto
        )

        boton_punto.grid(
            row=6,
            column=1,
            sticky="nsew",
            padx=5,
            pady=5
        )

    # ---------------------------------------------------------
    # TECLAS DE OPERADORES
    # ---------------------------------------------------------

    def teclas_operadores(self):

        boton_residuo = ttk.Button(
            self.ventana,
            text="%",
            style="Operador.TButton",
            command=self.controlador.click_residuo
        )

        boton_residuo.grid(
            row=2,
            column=1,
            sticky="nsew",
            padx=5,
            pady=5
        )

        boton_potencia = ttk.Button(
            self.ventana,
            text="**",
            style="Operador.TButton",
            command=self.controlador.click_potencia
        )

        boton_potencia.grid(
            row=2,
            column=2,
            sticky="nsew",
            padx=5,
            pady=5
        )

        boton_dividir = ttk.Button(
            self.ventana,
            text="/",
            style="Operador.TButton",
            command=self.controlador.click_dividir
        )

        boton_dividir.grid(
            row=2,
            column=3,
            sticky="nsew",
            padx=5,
            pady=5
        )

        boton_multiplicar = ttk.Button(
            self.ventana,
            text="*",
            style="Operador.TButton",
            command=self.controlador.click_multiplicar
        )

        boton_multiplicar.grid(
            row=3,
            column=3,
            sticky="nsew",
            padx=5,
            pady=5
        )

        boton_restar = ttk.Button(
            self.ventana,
            text="-",
            style="Operador.TButton",
            command=self.controlador.click_restar
        )

        boton_restar.grid(
            row=4,
            column=3,
            sticky="nsew",
            padx=5,
            pady=5
        )

        boton_sumar = ttk.Button(
            self.ventana,
            text="+",
            style="Operador.TButton",
            command=self.controlador.click_sumar
        )

        boton_sumar.grid(
            row=5,
            column=3,
            sticky="nsew",
            padx=5,
            pady=5
        )

    # ---------------------------------------------------------
    # TECLAS ESPECIALES
    # ---------------------------------------------------------

    def teclas_especiales(self):

        boton_limpiar = ttk.Button(
            self.ventana,
            text="C",
            style="Operador.TButton",
            command=self.controlador.limpiar
        )

        boton_limpiar.grid(
            row=2,
            column=0,
            sticky="nsew",
            padx=5,
            pady=5
        )

        boton_borrar = ttk.Button(
            self.ventana,
            text="⌫",
            style="Operador.TButton",
            command=self.controlador.borrar
        )

        boton_borrar.grid(
            row=6,
            column=2,
            sticky="nsew",
            padx=5,
            pady=5
        )

        boton_igual = ttk.Button(
            self.ventana,
            text="=",
            style="Igual.TButton",
            command=self.controlador.calcular
        )

        boton_igual.grid(
            row=6,
            column=3,
            sticky="nsew",
            padx=5,
            pady=5
        )

    # ---------------------------------------------------------
    # CONFIGURAR GRID
    # ---------------------------------------------------------

    def _configurar_grid(self):

        self.ventana.grid_rowconfigure(0, weight=1)
        self.ventana.grid_rowconfigure(1, weight=1)
        self.ventana.grid_rowconfigure(2, weight=1)
        self.ventana.grid_rowconfigure(3, weight=1)
        self.ventana.grid_rowconfigure(4, weight=1)
        self.ventana.grid_rowconfigure(5, weight=1)
        self.ventana.grid_rowconfigure(6, weight=1)

        self.ventana.grid_columnconfigure(0, weight=1)
        self.ventana.grid_columnconfigure(1, weight=1)
        self.ventana.grid_columnconfigure(2, weight=1)
        self.ventana.grid_columnconfigure(3, weight=1)

    # ---------------------------------------------------------
    # MÉTODOS PARA MOSTRAR INFORMACIÓN
    # ---------------------------------------------------------

    def obtener_entrada(self):

        return self.entrada.get()

    def mostrar_entrada(self, texto):

        self.entrada.delete(0, tk.END)
        self.entrada.insert(0, texto)

    def limpiar_entrada(self):

        self.entrada.delete(0, tk.END)

    def mostrar_resultado(self, texto):

        self.resultado.configure(
            foreground="#cccccc",
            text=texto
        )

    def mostrar_error(self, mensaje):

        self.resultado.configure(
            foreground="#ff6b6b",
            text=mensaje
        )