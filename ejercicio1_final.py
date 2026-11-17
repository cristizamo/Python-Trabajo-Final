
# Ejercicio 1 -
# Sanitización y Análisis Estadístico de Sensores (20 puntos)


# Punto A: Normalización de Lecturas ( limpiar_registro_sensor ): 
# Diseño de una función limpiar_registro_sensor(registro_raw) encargada del proceso de un 
# diccionario con datos crudos de un sensor y devuelve un registro estandarizado.



def limpiar_registro_sensor(registro_raw):

    # Quita espacios en los extremos del identificador.

    sensor_id = registro_raw["sensor_id"].strip()

    # Convierte la lectura a texto y unifica la unidad en mayúsculas.

    texto = str(registro_raw["temperatura"]).strip().upper()

    # Elimina el sufijo C o °C antes de convertir la lectura a número.
      
    if texto.endswith("C"):
        texto = texto[:-1].rstrip().removesuffix("°").strip()

    # Acepta coma decimal y convierte el texto a float.

    temperatura = float(texto.replace(",", "."))

    ubicacion = (registro_raw.get("ubicacion") or "").strip()

    # Crea un diccionario nuevo y asigna una ubicación segura si quedó vacía.

    return {
        "sensor_id": sensor_id,
        "temperatura": temperatura,
        "ubicacion": ubicacion or "Sin ubicación registrada",
    }
# Creación de un registro de prueba
registro = {
    "sensor_id": " SENSOR-001 ",
    "temperatura": "24.5C",
    "ubicacion": "Planta Norte"
}

resultado = limpiar_registro_sensor(registro)
print(resultado)

# Punto B - Monitoreo y Mapeo Estadístico (generar_resumen_sensores).
# Recibe lecturas limpias y devuelve una tupla con los IDs en alerta y el promedio.

def generar_resumen_sensores(lista_sensores_limpios, umbral_temperatura):
    lista_sensores_alerta = []
    total_temperatura = 0.0

    # Recorre las lecturas y acumula las temperaturas y su cantidad.

    for sensor in lista_sensores_limpios:
        temperatura = sensor["temperatura"]
        total_temperatura += temperatura
        
        # Agrega el ID solamente cuando la temperatura supera el límite.

        if temperatura > umbral_temperatura:
            lista_sensores_alerta.append(sensor["sensor_id"])

    # Usa None si no hay lecturas para evitar una división por cero.

    promedio_temperatura = None
    if lista_sensores_limpios:
        promedio_temperatura = total_temperatura / len(lista_sensores_limpios)

    return lista_sensores_alerta, promedio_temperatura

# Demostración del flujo completo al ejecutar este archivo directamente.

if __name__ == "__main__":

    # Prepara lecturas de ejemplo con espacios, unidades y ubicaciones faltantes.

    registros_crudos = [
        {"sensor_id": " SENSOR-001 ", "temperatura": "24.5C", "ubicacion": "Planta Norte"},
        {"sensor_id": " SENSOR-002 ", "temperatura": "31,0 °C"},
        {"sensor_id": " SENSOR-003 ", "temperatura": 28.5},
    ]

    # Limpia cada registro antes de realizar los cálculos.

    sensores_limpios = [
        limpiar_registro_sensor(registro) for registro in registros_crudos
    ]
    umbral = 28.5
    alertas, promedio = generar_resumen_sensores(sensores_limpios, umbral)

    # Muestra las lecturas normalizadas, las alertas y el promedio formateado.

    print("Reporte térmico de EcoTech Solutions")
    print(f"Sensores por encima de {umbral:.1f} °C: {', '.join(alertas) or 'Ninguno'}")
    if promedio is None:
        print("No hay lecturas para calcular el promedio.")
    else:
        print(f"Temperatura promedio: {promedio:.2f} °C")