from produccion.base import Producto
from produccion.planificacion import Periodo, Orden
from typing import List, Dict
from datetime import datetime, date, timedelta
from math import ceil, floor


class PeriodoUtil:
    @staticmethod
    def generarPeriodosPorNumeroDias(
        inicio: date, cantidad_periodos: int = 1, cantidad_dias: int = 1
    ) -> List["Periodo"]:
        salida: List["Periodo"] = []
        delta: timedelta = timedelta(days=cantidad_dias)
        for i in range(cantidad_periodos):
            salida.append(Periodo(fecha_inicio=(inicio + i * delta), delta=delta))

        return salida

    @staticmethod
    def generarPeriodosPorNumeroSemanas(
        inicio: date, cantidad_periodos: int = 1, cantidad_semanas: int = 1
    ) -> List["Periodo"]:
        salida: List["Periodo"] = []
        delta: timedelta = timedelta(weeks=cantidad_semanas)
        for i in range(cantidad_periodos):
            salida.append(Periodo(fecha_inicio=(inicio + i * delta), delta=delta))

        return salida

    @staticmethod
    def generarPeriodosPorNumeroHoras(
        inicio: date, cantidad_periodos: int = 1, cantidad_horas: int = 1
    ) -> List["Periodo"]:
        salida: List["Periodo"] = []
        delta: timedelta = timedelta(hours=cantidad_horas)
        for i in range(cantidad_periodos):
            salida.append(Periodo(fecha_inicio=(inicio + i * delta), delta=delta))

        return salida


class OrdenUtil:
    @staticmethod
    def generarOrdenConProductoPeriodosEnCero(
        nombre: str, productos: List["Producto"], periodos: List["Periodo"]
    ) -> Orden:
        salida: Orden = Orden(nombre=nombre)
        for producto in productos:
            detalle: Dict["Periodo", float] = {}
            for periodo in periodos:
                detalle[periodo] = 0

            salida.agregar_producto_con_detalle(producto=producto, detalle=detalle)

        return salida

    @staticmethod
    def agregarProductoDetalle(
        orden: "Orden",
        producto: Producto,
        periodos: List["Periodo"],
        demandas: List[float],
    ) -> None:
        valores: Dict["Periodo", float] = {k: v for k, v in zip(periodos, demandas)}
        orden.agregar_producto_con_detalle(producto=producto, detalle=valores)


class TimeDeltaUtils:

    @staticmethod
    def redondear_timedelta_segundos(
        duracion: timedelta, segundos_multiplo: int
    ) -> timedelta:
        segundos: float = duracion.total_seconds()
        segundos_ajustados = round(segundos / segundos_multiplo) * segundos_multiplo
        return timedelta(seconds=segundos_ajustados)

    @staticmethod
    def calcular_duracion_unidad_por_minuto(cantidad_en_un_minuto) -> timedelta:
        return TimeDeltaUtils.redondear_timedelta_segundos(
            timedelta(minutes=1) / cantidad_en_un_minuto, 1
        )
    
    @staticmethod
    def calcular_duracion_unidad_por_hora(cantidad_en_una_hora) -> timedelta:
        return TimeDeltaUtils.redondear_timedelta_segundos(
            timedelta(hours=1) / cantidad_en_una_hora, 1
        )