import tkinter as tk
 
from Vista import CalculadoraVista
from Modelo import CalculadoraModelo
from Controlador import CalculadoraControlador
 
if __name__ == "__main__":
    inicio = tk.Tk()
 
    modelo = CalculadoraModelo()
    controlador = CalculadoraControlador(modelo)  
    vista = CalculadoraVista(inicio, controlador)  
    controlador.vista = vista                       
 
    inicio.mainloop()