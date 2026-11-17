

class StockInvalidoError(ValueError):
    """El stock debe ser un número entero no negativo."""


class DispositivoEcológico:
    def __init__(self, codigo, nombre, stock):
        self.codigo = codigo
        self.nombre = nombre
        self.stock = stock

    @property
    def stock(self):
        return self.__stock

    @stock.setter
    def stock(self, nuevo_stock):
        if type(nuevo_stock) is not int or nuevo_stock < 0:
            raise StockInvalidoError("El stock debe ser un entero no negativo.")
        self.__stock = nuevo_stock

    def ficha_tecnica(self):
        return f"{self.codigo} | {self.nombre} | Stock: {self.stock} unidades"

    def a_diccionario(self):
        return {
            "tipo": type(self).__name__,
            "codigo": self.codigo,
            "nombre": self.nombre,
            "stock": self.stock,
        }


class PanelSolar(DispositivoEcológico):
    def __init__(self, codigo, nombre, stock, potencia_w, eficiencia_pct):
        super().__init__(codigo, nombre, stock)
        self.potencia_w = potencia_w
        self.eficiencia_pct = eficiencia_pct

    def ficha_tecnica(self):
        return (
            f"{super().ficha_tecnica()} | Potencia: {self.potencia_w} W "
            f"| Eficiencia: {self.eficiencia_pct:.1f} %"
        )

    def a_diccionario(self):
        datos = super().a_diccionario()
        datos["potencia_w"] = self.potencia_w
        datos["eficiencia_pct"] = self.eficiencia_pct
        return datos


import json


# Clase para guardar el inventario
class GestorInventario:

    def guardar_catalogo_json(self, lista_dispositivos, ruta_archivo):
        datos = []

        for dispositivo in lista_dispositivos:
            datos.append(dispositivo.a_diccionario())

        with open(ruta_archivo, "w", encoding="utf-8") as archivo:
            json.dump(datos, archivo, indent=4, ensure_ascii=False)


# BLOQUE DE EJECUCIÓN

# Crear dos paneles solares
panel1 = PanelSolar("P001", "Panel Solar Eco", 10, 400, 20.5)
panel2 = PanelSolar("P002", "Panel Solar Plus", 5, 550, 22.0)

# Mostrar las fichas técnicas
print(panel1.ficha_tecnica())
print(panel2.ficha_tecnica())

# Probar un stock incorrecto
try:
    panel1.stock = -5
except StockInvalidoError as error:
    print("Error detectado:", error)

# Crear el catálogo
catalogo = [panel1, panel2]

# Guardar en JSON
gestor = GestorInventario()
gestor.guardar_catalogo_json(catalogo, "catalogo_ecotech.json")

print("Catálogo guardado correctamente.")