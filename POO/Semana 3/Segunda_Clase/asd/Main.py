import tkinter as tk
 
from Vista import CalculadoraVista
from Modelo import CalculadoraModelo
from Controlador import CalculadoraControlador
 
if __name__ == "__main__":
    inicio = tk.Tk()
 
    modelo = CalculadoraModelo()
    controlador = CalculadoraControlador(modelo)   # todavía sin vista
    vista = CalculadoraVista(inicio, controlador)     # ya usa command=controlador.click_X
    controlador.vista = vista                        # ahora el controlador ya puede usarla
 
    inicio.mainloop()