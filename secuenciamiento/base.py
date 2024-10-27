
from produccion.linea import Linea
from produccion.producto import Producto


class CalculadoraTiempoSecuencia:
    def calcular_tiempo_secuencia(self, linea: "Linea", producto: Producto) -> float:
        tiempo_total = 0
        for maquina in linea.secuencia_maquinas:
            tiempo_maquina = linea.tiempos_procesamiento[producto][maquina]
            tiempo_total += tiempo_maquina
        return tiempo_total

    def __repr__(self):
        return "CalculadoraTiempoSecuencia()"

    def __str__(self):
        return "Calculadora de tiempo de secuencia"
