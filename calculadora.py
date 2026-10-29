"""Módulo de cálculo de impacto energético y huella de carbono."""


def estimar_consumo_wh(potencia_w: float, horas_uso: float, iteraciones: int = 1) -> float:
    """Calcula el consumo energético total en Vatios-hora (Wh)."""
    consumo = potencia_w * horas_uso 
    print(f"El consumo total de este dispositivo es de {consumo}wh)")
    return consumo


def calcular_huella_co2(consumo_wh: float, factor_emision: float = 0.23) -> float:
     """Calcula la huella de carbono en kilogramos de C02 equivalente (kg CO2e)"""
     kwh = (consumo_wh / 1000.0) * factor_emision
     emisiones = kwh * factor_emision
     return kwh 

def main() -> None:
     wh = float(input("Introduce el consumo en wh: ").strip())
     horasuso = float(input("Introduce las horas de uso: ").strip())
     consumo = estimar_consumo_wh(wh, horasuso)
     calcular_huella_co2(consumo)

if __name__ == "__main__":
     main()
