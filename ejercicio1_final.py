
# Ejercicio 1 -
# Sanitización y Análisis Estadístico de Sensores (20 puntos)




def limpiar_registro_sensor(registro_raw):
    sensor_id = registro_raw["sensor_id"].strip()


    texto = str(registro_raw["temperatura"]).strip().upper()
    if texto.endswith("C"):
        texto = texto[:-1].rstrip().removesuffix("°").strip()
    temperatura = float(texto.replace(",", "."))

    ubicacion = (registro_raw.get("ubicacion") or "").strip()

    return {
        "sensor_id": sensor_id,
        "temperatura": temperatura,
        "ubicacion": ubicacion or "Sin ubicación registrada",
    }
# Crear un registro de prueba
registro = {
    "sensor_id": " SENSOR-001 ",
    "temperatura": "24.5C",
    "ubicacion": "Planta Norte"
}

resultado = limpiar_registro_sensor(registro)
print(resultado)

def generar_resumen_sensores(lista_sensores_limpios, umbral_temperatura):
    lista_sensores_alerta = []
    total_temperatura = 0.0

    for sensor in lista_sensores_limpios:
        temperatura = sensor["temperatura"]
        total_temperatura += temperatura

        if temperatura > umbral_temperatura:
            lista_sensores_alerta.append(sensor["sensor_id"])

    promedio_temperatura = None
    if lista_sensores_limpios:
        promedio_temperatura = total_temperatura / len(lista_sensores_limpios)

    return lista_sensores_alerta, promedio_temperatura


if __name__ == "__main__":
    registros_crudos = [
        {"sensor_id": " SENSOR-001 ", "temperatura": "24.5C", "ubicacion": "Planta Norte"},
        {"sensor_id": " SENSOR-002 ", "temperatura": "31,0 °C"},
        {"sensor_id": " SENSOR-003 ", "temperatura": 28.5},
    ]

    sensores_limpios = [
        limpiar_registro_sensor(registro) for registro in registros_crudos
    ]
    umbral = 28.5
    alertas, promedio = generar_resumen_sensores(sensores_limpios, umbral)

    print("Reporte térmico de EcoTech Solutions")
    print(f"Sensores por encima de {umbral:.1f} °C: {', '.join(alertas) or 'Ninguno'}")
    if promedio is None:
        print("No hay lecturas para calcular el promedio.")
    else:
        print(f"Temperatura promedio: {promedio:.2f} °C")