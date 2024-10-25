from producion.base import Producto
from typing import List, Dict
from datetime import datetime, date, timedelta


class Periodo:
    def __init__(self, fecha_inicio: datetime, delta: timedelta = timedelta(days=1)):
        self._fecha_inicio = fecha_inicio
        self._delta = delta
        self._anno_iso, self._numero_semana_iso, self._dia_semana_iso = (
            self._fecha_inicio.isocalendar()
        )

    @property
    def fecha_inicio(self) -> datetime:
        return self._fecha_inicio

    @fecha_inicio.setter
    def fecha_inicio(self, valor_nuevo: datetime):
        self._fecha_inicio = valor_nuevo
        self._anno_iso, self._numero_semana_iso, self._dia_semana_iso = (
            self._fecha_inicio.isocalendar()
        )

    @property
    def fecha_final(self) -> datetime:
        return self._fecha_inicio + self._delta

    @property
    def delta(self) -> timedelta:
        return self._delta

    @delta.setter
    def delta(self, valor_nuevo: timedelta):
        self._delta = valor_nuevo

    @property
    def semana_iso(self) -> str:
        return '{:d}-W{:02d}'.format(self._anno_iso, self._numero_semana_iso)

    @property
    def semana_iso_dia(self) -> str:
        return '{:d}-W{:02d}-{:d}'.format(
            self._anno_iso, self._numero_semana_iso, self._dia_semana_iso
        )

    def verificar_fecha_en_periodo(self, fecha: datetime) -> bool:
        return self.fecha_inicio <= fecha < self.fecha_final

    def __repr__(self):
        return self.fecha_inicio.isoformat()

    def __str__(self):
        return self.fecha_inicio.isoformat()


class PeriodoUtil:
    @staticmethod
    def generarPeriodosPorNumeroDias(
        inicio: date, cantidad_periodos: int = 1, cantidad_dias: int = 1
    ) -> List['Periodo']:
        salida: List['Periodo'] = []
        delta: timedelta = timedelta(days=cantidad_dias)
        for i in range(cantidad_periodos):
            salida.append(Periodo(fecha_inicio=(inicio + i * delta), delta=delta))

        return salida

    @staticmethod
    def generarPeriodosPorNumeroSemanas(
        inicio: date, cantidad_periodos: int = 1, cantidad_semanas: int = 1
    ) -> List['Periodo']:
        salida: List['Periodo'] = []
        delta: timedelta = timedelta(weeks=cantidad_semanas)
        for i in range(cantidad_periodos):
            salida.append(Periodo(fecha_inicio=(inicio + i * delta), delta=delta))

        return salida

    @staticmethod
    def generarPeriodosPorNumeroHoras(
        inicio: date, cantidad_periodos: int = 1, cantidad_horas: int = 1
    ) -> List['Periodo']:
        salida: List['Periodo'] = []
        delta: timedelta = timedelta(hours=cantidad_horas)
        for i in range(cantidad_periodos):
            salida.append(Periodo(fecha_inicio=(inicio + i * delta), delta=delta))

        return salida


class Orden:
    def __init__(
        self, nombre: str, detalle: Dict[Producto, Dict['Periodo', float]] = {}
    ):
        ''' '''
        self._nombre = nombre
        self._detalle = detalle

    @property
    def nombre(self) -> str:
        return self._nombre

    @nombre.setter
    def nombre(self, value: str) -> None:
        self._nombre = value

    @property
    def detalle(self) -> Dict[Producto, Dict['Periodo', float]]:
        return self._detalle

    @detalle.setter
    def detalle(self, value: Dict[Producto, Dict['Periodo', float]]):
        self._detalle = value

    def agregar_producto_con_detalle(
        self, producto: Producto, detalle: Dict['Periodo', float]
    ) -> None:
        self.detalle[producto] = detalle


class OrdenUtil:
    @staticmethod
    def generarOrdenConProductoPeriodosEnCero(
        nombre: str, productos: List['Producto'], periodos: List['Periodo']
    ) -> Orden:
        salida: Orden = Orden(nombre=nombre)
        for producto in productos:
            detalle: Dict['Periodo', float] = {}
            for periodo in periodos:
                detalle[periodo] = 0

            salida.agregar_producto_con_detalle(producto=producto, detalle=detalle)

        return salida


class Demanda(Orden):
    pass  # Hereda de Orden
