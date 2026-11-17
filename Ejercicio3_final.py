

def calcular_emisiones_carbono(consumo_kwh, factor_emision=0.4):
    if consumo_kwh < 0:
        raise ValueError("El consumo en kWh no puede ser negativo.")

    return consumo_kwh * factor_emision

import unittest

from .emisiones import calcular_emisiones_carbono


class TestCalculoEmisiones(unittest.TestCase):
    def test_consumo_positivo_con_factor_por_defecto(self):
        self.assertAlmostEqual(calcular_emisiones_carbono(12.3), 4.92)

    def test_factor_personalizado(self):
        resultado = calcular_emisiones_carbono(100, factor_emision=0.25)
        self.assertAlmostEqual(resultado, 25.0)

    def test_consumo_cero(self):
        self.assertEqual(calcular_emisiones_carbono(0), 0.0)

    def test_consumo_negativo(self):
        with self.assertRaises(ValueError):
            calcular_emisiones_carbono(-1)

            import unittest

from .emisiones import calcular_emisiones_carbono


class TestCalculoEmisiones(unittest.TestCase):
    def test_consumo_positivo_con_factor_por_defecto(self):
        self.assertAlmostEqual(calcular_emisiones_carbono(12.3), 4.92)

    def test_factor_personalizado(self):
        resultado = calcular_emisiones_carbono(100, factor_emision=0.25)
        self.assertAlmostEqual(resultado, 25.0)

    def test_consumo_cero(self):
        self.assertEqual(calcular_emisiones_carbono(0), 0.0)

    def test_consumo_negativo(self):
        with self.assertRaises(ValueError):
            calcular_emisiones_carbono(-1)

# Punto B — Métricas y vista de Django
# Para identificar la planta de mayor consumo, primero se suman todos los registros de cada planta y después se comparan los totales. La vista usa un historial de ejemplo y pasa las métricas como contexto a render().

# Agregá esta función a sustentabilidad/emisiones.py:


def obtener_metricas_consumo(registros):
    total_emisiones = 0.0
    consumo_por_planta = {}

    for registro in registros:
        planta = registro["planta"]
        consumo_kwh = registro["consumo_kwh"]

        total_emisiones += calcular_emisiones_carbono(consumo_kwh)
        consumo_por_planta[planta] = consumo_por_planta.get(planta, 0) + consumo_kwh

    planta_mayor_consumo = max(
        consumo_por_planta,
        key=consumo_por_planta.get,
        default=None,
    )

    return {
        "total_emisiones": total_emisiones,
        "planta_mayor_consumo": planta_mayor_consumo,
        "mayor_consumo_kwh": consumo_por_planta.get(planta_mayor_consumo, 0),
    }

from django.shortcuts import render

from .emisiones import obtener_metricas_consumo


REGISTROS_CONSUMO_DEMO = [
    {"planta": "Planta Norte", "consumo_kwh": 800},
    {"planta": "Planta Sur", "consumo_kwh": 1000},
    {"planta": "Planta Norte", "consumo_kwh": 500},
    {"planta": "Planta Este", "consumo_kwh": 350},
]


def vista_panel_sustentabilidad(request):
    contexto = obtener_metricas_consumo(REGISTROS_CONSUMO_DEMO)
    return render(request, "sustentabilidad/panel.html", contexto)
En sustentabilidad/templates/sustentabilidad/panel.html:
<h1>Panel de sustentabilidad</h1>
<p>Emisiones totales: {{ total_emisiones|floatformat:2 }} kg de CO₂</p>

{% if planta_mayor_consumo %}
    <p>Planta de mayor consumo: {{ planta_mayor_consumo }} ({{ mayor_consumo_kwh }} kWh)</p>
{% else %}
    <p>No hay registros de consumo.</p>
{% endif %}