class Producto:
    def __init__(self, nombre, precio, stock, codigo):
        self.nombre = nombre          # público
        self.precio = precio          # público
        self._stock = stock           # protegido
        self.__codigo = codigo        # privado

    def mostrar_producto(self):
        print(f"Producto : {self.nombre}")
        print(f"Precio   : S/ {self.precio:,.2f}")
        print(f"Stock    : {self._stock} unidades")
        print(f"Código   : {self.__codigo}")

    def aumentar_stock(self, cantidad):
        self._stock = self._stock + cantidad
        print(f"Stock del producto '{self.nombre}' se aumento en {cantidad}")
        print(f"Stock actual: {self._stock}")

    def reducir_stock(self, cantidad):
        self._stock = self._stock - cantidad
        print(f"Stock del producto '{self.nombre}' se redujo en {cantidad}")
        print(f"Stock actual: {self._stock}")

    def consultar_codigo(self):
        print(f"Codigo consultado : {self.__codigo}")
        self.mostrar_producto()

productos = {
    "LAP001": Producto("Laptop", 2500, 10, "LAP001"),
    "MOU001": Producto("Mouse", 80, 25, "MOU001"),
    "TEC001": Producto("Teclado", 150, 15, "TEC001")
}


# Teclado: prueba completa de todos los métodos
productos["TEC001"].mostrar_producto()
print("")

productos["TEC001"].aumentar_stock(5)
print("")

productos["TEC001"].reducir_stock(3)
print("")

productos["TEC001"].consultar_codigo()
print("")

print("Stock final:")
print(f"{productos['TEC001'].nombre} : {productos['TEC001']._stock} unidades")
print("")

# Mouse y Laptop: solo lo esencial
productos["MOU001"].aumentar_stock(5)
print("")
productos["MOU001"].consultar_codigo()
print("")

productos["LAP001"].reducir_stock(3)
print("")
productos["LAP001"].consultar_codigo()
