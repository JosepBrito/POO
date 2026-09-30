import tkinter as tk

class CalculadoraVista:

    def __init__(self, venta, controlador):

        self.ventana = ventana
        self.controlador = controlador

        self.ventana.title("Calculadora")
        self.ventana.geometry("350x580")

        self.pantalla()
        self.teclas_numericas()
        self.teclas_operadores()
        self.teclas_especiales()
        self.configurar_grid()

    
    # Pantalla

    def pantalla(self):

        self.entrada = ttk.Entry(self.ventana)
        self.entrada.grid(row=0, column=0, columnspan=4, sticky="nsew", padx=10, pady=(15,5))
        self.resultado = tkk.Label(self.ventana)
        self.resultado.grid(row=1, column=0, columnspan=4, sticky="nsew", padx=10, pady=(0,10))

    # Teclas Numericas

    def teclas_numericas(self):

        # Del 0 al 3
        boton_0 = ttk.Button(self.ventana, text="0", command=self.controlador.click_0)
        boton_0.grid(row = 6, column = 0, sticky="nsew", padx=5, pady=5)

        boton_1 = ttk.Button(self.ventana, text="1", command=self.controlador.click_1)
        boton_1.grid(row = 5, column = 0, sticky="nsew", padx=5, pady=5)

        boton_2 = ttk.Button(self.ventana, text="2", command=self.controlador.click_2)
        boton_2.grid(row = 5, column = 1, sticky="nsew", padx=5, pady=5)

        boton_3 = ttk.Button(self.ventana, text="3", command=self.controlador.click_3)
        boton_3.grid(row = 5, column = 2, sticky="nsew", padx=5, pady=5)
        
        # Del 4 al 6
        boton_4 = ttk.Button(self.ventana, text="4", command=self.controlador.click_4)
        boton_4.grid(row = 4, column = 0, sticky="nsew", padx=5, pady=5)

        boton_5 = ttk.Button(self.ventana, text="5", command=self.controlador.click_5)
        boton_5.grid(row = 4, column = 1, sticky="nsew", padx=5, pady=5)

        boton_6 = ttk.Button(self.ventana, text="6", command=self.controlador.click_6)
        boton_6.grid(row = 4, column = 2, sticky="nsew", padx=5, pady=5)

        # Del 7 al 9
        boton_7 = ttk.Button(self.ventana, text="3", command=self.controlador.click_3)
        boton_7.grid(row = 3, column = 0, sticky="nsew", padx=5, pady=5)

        boton_8 = ttk.Button(self.ventana, text="3", command=self.controlador.click_3)
        boton_8.grid(row = 3, column = 1, sticky="nsew", padx=5, pady=5)

        boton_9 = ttk.Button(self.ventana, text="3", command=self.controlador.click_3)
        boton_9.grid(row = 3, column = 2, sticky="nsew", padx=5, pady=5)


        # El boton "."
        boton_punto = ttk.Button(self.ventana, text="3", command=self.controlador.click_3)
        boton_punto.grid(row = 6, column = 1, sticky="nsew", padx=5, pady=5)

    # Los operadores

    def teclas_operadores(self):

        boton_residuo = ttk.Button(self.ventana, text="3", command=self.controlador.click_3)
        boton_residuo.grid(row = 3, column = 2, sticky="nsew", padx=5, pady=5)

        boton_potencia = ttk.Button(self.ventana, text="3", command=self.controlador.click_3)
        boton_potencia.grid(row = 3, column = 2, sticky="nsew", padx=5, pady=5)

        boton_dividr = ttk.Button(self.ventana, text="3", command=self.controlador.click_3)
        boton_dividir.grid(row = 3, column = 2, sticky="nsew", padx=5, pady=5)

        boton_multiplicar = ttk.Button(self.ventana, text="3", command=self.controlador.click_3)
        boton_multiplicar.grid(row = 3, column = 2, sticky="nsew", padx=5, pady=5)

        boton_restar = ttk.Button(self.ventana, text="3", command=self.controlador.click_3)
        boton_restar.grid(row = 3, column = 2, sticky="nsew", padx=5, pady=5)

        boton_sumar = ttk.Button(self.ventana, text="3", command=self.controlador.click_3)
        boton_sumar.grid(row = 3, column = 2, sticky="nsew", padx=5, pady=5)