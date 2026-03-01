class raton:
    def __init__(self, color, tamaño):
        self.color = color
        self.tamaño = tamaño
    
    def ingresar_datos(self):
        self.color = input("Ingrese el color del ratón: ")
        self.tamaño = input("Ingrese el tamaño del ratón: ")
    
    def mostrar_datos(self):
        print(f"Mi ratón es de color {self.color} y tamaño {self.tamaño}.")

if __name__ == "__main__":
    mi_raton = raton("", "")
    mi_raton.ingresar_datos()
    mi_raton.mostrar_datos()