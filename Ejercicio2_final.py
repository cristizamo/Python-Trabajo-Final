from pathlib import Path
from tempfile import TemporaryDirectory



# Punto A - Dominio del Catálogo y Reglas de Inventario.
# Define la excepción personalizada para comunicar errores en el stock.

class StockInvalidoError(ValueError):
    """El stock debe ser un número entero no negativo."""

# El stock debe ser un número entero no negativo.
# Clase base con los atributos comunes de los productos ecológicos.

class DispositivoEcológico: 
    
    def __init__(self, codigo, nombre, stock):
        self.codigo = codigo
        self.nombre = nombre
        self.stock = stock

    # Permite consultar el atributo privado __stock mediante dispositivo.stock.

    @property
    def stock(self):
        return self.__stock
    
    # Valida cada asignación antes de modificar el atributo privado.

    @stock.setter
    def stock(self, nuevo_stock):

        # Rechaza números negativos, decimales, textos y valores booleanos.

        if type(nuevo_stock) is not int or nuevo_stock < 0:
            raise StockInvalidoError("El stock debe ser un entero no negativo.")
        self.__stock = nuevo_stock

        # Devuelve la ficha comercial común a los dispositivos.

    def ficha_tecnica(self):
        return f"{self.codigo} | {self.nombre} | Stock: {self.stock} unidades"

    # Convierte los atributos del objeto a un diccionario serializable.

    def a_diccionario(self):
        return {
            "tipo": type(self).__name__,
            "codigo": self.codigo,
            "nombre": self.nombre,
            "stock": self.stock,
        }
    
# Hereda los datos comunes y agrega potencia y eficiencia.

class PanelSolar(DispositivoEcológico):
    def __init__(self, codigo, nombre, stock, potencia_w, eficiencia_pct):

         # Reutiliza el constructor de la clase base.

        super().__init__(codigo, nombre, stock)
        self.potencia_w = potencia_w
        self.eficiencia_pct = eficiencia_pct

    # Aplica polimorfismo al personalizar el mismo método de la clase base.

    def ficha_tecnica(self):
        return (
            f"{super().ficha_tecnica()} | Potencia: {self.potencia_w} W "
            f"| Eficiencia: {self.eficiencia_pct:.1f} %"
        )

    # Incluye los atributos específicos del panel en la exportación.

    def a_diccionario(self):
        datos = super().a_diccionario()
        datos["potencia_w"] = self.potencia_w
        datos["eficiencia_pct"] = self.eficiencia_pct
        return datos


import json
# Punto B - Persistencia y Gestión del Catálogo.
# Guarda los productos como una lista de diccionarios en un archivo JSON.

# Clase para guardar el inventario

class GestorInventario:
    def guardar_catalogo_json(self, lista_dispositivos, ruta_archivo):

        # Cada objeto produce su diccionario según la clase a la que pertenece.

        catalogo = [dispositivo.a_diccionario() for dispositivo in lista_dispositivos]
        ruta = Path(ruta_archivo)

        # Reemplazamos el catálogo cuando el archivo nuevo ya está completo.

        with TemporaryDirectory(dir=ruta.parent) as directorio_temporal:
            ruta_temporal = Path(directorio_temporal) / ruta.name
            with ruta_temporal.open("w", encoding="utf-8") as archivo:

                # Escribe JSON legible y conserva las tildes del texto.

                json.dump(catalogo, archivo, indent=4, ensure_ascii=False)
                archivo.write("\n")
            ruta_temporal.replace(ruta)


# Bloque de prueba al ejecutar este archivo directamente.

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