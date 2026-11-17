# Trabajo Final de Python

Trabajo práctico con ejercicios de procesamiento de datos, programación orientada a objetos y sustentabilidad, ambientados en EcoTech Solutions.

El proyecto aborda la limpieza de lecturas de sensores, la gestión de un inventario de dispositivos ecológicos y el cálculo de emisiones de carbono a partir del consumo eléctrico.

## Contenido del proyecto

| Archivo | Descripción |
| --- | --- |
| `ejercicio1_final.py` | Limpieza de registros de sensores y generación de un resumen de temperaturas. |
| `Ejercicio2_final.py` | Modelado de dispositivos ecológicos, validación de stock y exportación del catálogo a JSON. |
| `Ejercicio3_final.py` | Cálculo de emisiones, pruebas unitarias y propuesta de un panel de sustentabilidad con Django. |

## Ejercicio 1 — Sensores y temperaturas

La función `limpiar_registro_sensor` normaliza los datos de cada sensor.

- Elimina espacios al comienzo y al final del identificador.
- Convierte la temperatura a un número decimal y admite valores con coma, punto y sufijos como `C` o `°C`.
- Completa las ubicaciones ausentes o vacías con el texto «Sin ubicación registrada».

La función `generar_resumen_sensores` recibe una lista de registros limpios y un umbral de temperatura. Devuelve los identificadores de los sensores que superan ese umbral y la temperatura promedio. Si la lista está vacía, el promedio es `None`.

El archivo incluye datos de ejemplo y muestra los resultados en la consola.

## Ejercicio 2 — Inventario de dispositivos ecológicos

El inventario utiliza clases, herencia y propiedades para representar dispositivos y validar sus datos.

- `DispositivoEcológico` almacena código, nombre y stock, y permite obtener una ficha técnica y una representación como diccionario.
- `PanelSolar` incorpora la potencia en watts y el porcentaje de eficiencia.
- `StockInvalidoError` informa los intentos de asignar un stock que incumple la condición de entero no negativo.
- `GestorInventario` guarda el catálogo de dispositivos en un archivo JSON.

El ejemplo crea dos paneles solares, imprime sus fichas técnicas, demuestra el manejo de un stock inválido y genera `catalogo_ecotech.json` en el directorio desde el que se ejecuta el programa. Si ese archivo ya existe, su contenido se reemplaza.

## Ejercicio 3 — Emisiones y panel de sustentabilidad

La función `calcular_emisiones_carbono` multiplica el consumo en kWh por un factor de emisión. El factor predeterminado es `0.4`, y los consumos negativos generan un `ValueError`.

El archivo incluye pruebas con `unittest` para consumo positivo, consumo cero, factor personalizado y consumo negativo.

La función `obtener_metricas_consumo` acumula las emisiones de los registros y suma el consumo por planta para identificar la de mayor consumo total. También se incluye una vista de Django con datos de ejemplo y el contenido de una plantilla para mostrar esas métricas.

### Estado actual del ejercicio 3

Este archivo reúne fragmentos que requieren organización antes de ejecutarse.

- Las importaciones relativas hacen referencia a un módulo `emisiones.py` que debe incorporarse a un paquete.
- La clase de pruebas aparece duplicada.
- El texto explicativo y la plantilla HTML están incluidos directamente en el archivo Python.
- La vista requiere un proyecto Django configurado y la plantilla `sustentabilidad/templates/sustentabilidad/panel.html`.

La integración de esos componentes queda pendiente para una próxima revisión.

## Requisitos y ejecución

Los ejercicios 1 y 2 utilizan Python y su biblioteca estándar. Para el primero se requiere Python 3.9 o posterior por el uso de `str.removesuffix`.

Desde la carpeta del proyecto, ejecutar cada ejercicio por separado.

```bash
python ejercicio1_final.py
python Ejercicio2_final.py
```

Los resultados se muestran en la consola. El segundo ejercicio también escribe el catálogo JSON.

La parte web del ejercicio 3 requiere Django y la organización indicada en su sección antes de contar con un procedimiento de ejecución completo.

## Conceptos trabajados

- Funciones, listas y diccionarios.
- Limpieza y transformación de datos.
- Cálculo de promedios y acumulación de valores.
- Clases, herencia, encapsulamiento y propiedades.
- Validación de datos y manejo de excepciones.
- Escritura de archivos JSON.
- Pruebas unitarias.
- Vistas y plantillas de Django.

## Estado del documento

Primera versión descriptiva basada en los archivos actuales del proyecto, preparada para futuras ediciones.
