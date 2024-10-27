from datetime import datetime, time, timedelta
from typing import List, Optional


class Periodo:
    def __init__(self, fecha_inicio: datetime, delta: timedelta = timedelta(days=1)):
        if not isinstance(fecha_inicio, datetime):
            fecha_inicio = datetime.combine(fecha_inicio, time())
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
    def delta(self, valor_nuevo: timedelta) -> None:
        self._delta = valor_nuevo

    @property
    def semana_iso(self) -> str:
        return "{:d}-W{:02d}".format(self._anno_iso, self._numero_semana_iso)

    @property
    def semana_iso_dia(self) -> str:
        return "{:d}-W{:02d}-{:d}".format(
            self._anno_iso, self._numero_semana_iso, self._dia_semana_iso
        )

    def verificar_fecha_en_periodo(self, fecha: datetime) -> bool:
        return self.fecha_inicio <= fecha < self.fecha_final

    def __repr__(self):
        return "[{},{})".format(
            self.fecha_inicio.isoformat(), self.fecha_final.isoformat()
        )

    def __str__(self):
        return "[{},{})".format(
            self.fecha_inicio.isoformat(), self.fecha_final.isoformat()
        )


class PeriodoUtil:
    @staticmethod
    def generarPeriodosPorNumeroDias(
        inicio: datetime, cantidad_periodos: int = 1, cantidad_dias: int = 1
    ) -> List["Periodo"]:
        salida: List["Periodo"] = []
        delta: timedelta = timedelta(days=cantidad_dias)
        for i in range(cantidad_periodos):
            salida.append(Periodo(fecha_inicio=(inicio + i * delta), delta=delta))

        return salida

    @staticmethod
    def generarPeriodosPorNumeroSemanas(
        inicio: datetime, cantidad_periodos: int = 1, cantidad_semanas: int = 1
    ) -> List["Periodo"]:
        salida: List["Periodo"] = []
        delta: timedelta = timedelta(weeks=cantidad_semanas)
        for i in range(cantidad_periodos):
            salida.append(Periodo(fecha_inicio=(inicio + i * delta), delta=delta))

        return salida

    @staticmethod
    def generarPeriodosPorNumeroHoras(
        inicio: datetime, cantidad_periodos: int = 1, cantidad_horas: int = 1
    ) -> List["Periodo"]:
        salida: List["Periodo"] = []
        periodos: List[datetime] = []
        delta: timedelta = timedelta(hours=cantidad_horas)

        for i in range(cantidad_periodos):
            periodos.append(datetime.combine(inicio, time()) + (i * delta))

        for p in periodos:
            salida.append(Periodo(fecha_inicio=p, delta=delta))

        return salida

    @staticmethod
    def identificarPeriodoPorFecha(
        periodos: List["Periodo"], fecha: datetime
    ) -> Optional["Periodo"]:
        for periodo in periodos:
            if periodo.verificar_fecha_en_periodo(fecha):
                return periodo

        return None

    @staticmethod
    def ordenarPeriodosPorFechaInicio(periodos: List["Periodo"]) -> List["Periodo"]:
        return sorted(periodos, key=lambda x: (x.fecha_inicio, x.fecha_final))
