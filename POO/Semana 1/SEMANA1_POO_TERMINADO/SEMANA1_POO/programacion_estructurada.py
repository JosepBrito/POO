#En programación estructurada los datos se mantienen separados de las funciones.
# Función que muestra la información del empleado
def mostrar_empleado(nombre, cargo, salario):
    print("----- DATOS DEL EMPLEADO -----")
    print("Nombre:", nombre)
    print("Cargo:", cargo)
    print("Salario:", salario)


# Función que calcula el salario anual
def calcular_salario_anual(salario):
    return salario * 12


# Función que aplica un aumento porcentual
def aumentar_salario(salario, porcentaje):
    return salario + (salario * porcentaje / 100)


# Datos del empleado
nombre = "Carlos"
cargo = "Técnico de Sistemas"
salario = 1800

# Mostrar información
mostrar_empleado(nombre, cargo, salario)

# Calcular salario anual
salario_anual = calcular_salario_anual(salario)
print("Salario anual:", salario_anual)

# Aplicar aumento
nuevo_salario = aumentar_salario(salario, 10)
print("Nuevo salario:", nuevo_salario)

