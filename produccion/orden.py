from datetime import datetime
from typing import Dict, List, Optional, Tuple

import pandas as pd

from produccion.periodo import Periodo, PeriodoUtil
from produccion.producto import Producto


class Orden:
    def __init__(self, nombre: str):
        self._nombre = nombre
        self._periodos: List["Periodo"] = []
        self._productos: Dict[str, "Producto"] = {}
        self._contenido: Dict[Tuple[Tuple["Producto", "Periodo"]], float] = {}

    @property
    def nombre(self) -> str:
        return self._nombre

    @nombre.setter
    def nombre(self, value: str) -> None:
        self._nombre = value

    @property
    def periodos(self) -> List["Periodo"]:
        return self._periodos

    @property
    def productos(self) -> List["Producto"]:
        return list(self._productos.keys())

    @property
    def contenido(self) -> Dict[Tuple[Tuple["Producto", "Periodo"]], float]:
        return self._contenido

    @property
    def contenido_simplificado(self) -> List[Tuple[str, str, float]]:
        return [
            (k[0].codigo, k[1].fecha_inicio.isoformat(), v)
            for k, v in self._contenido.items()
        ]

    def agregar_producto(self, producto: "Producto") -> bool:
        if producto.codigo in self._productos:
            return False
        else:
            self._productos[producto.codigo] = producto
            for periodo in self._periodos:
                self.agregar_producto_periodo_con_cantidad(producto, periodo, 0)
            return True

    def encontrar_producto_por_codigo(self, codigo: str) -> Optional["Producto"]:
        if codigo in self._productos:
            return self._productos[codigo]
        else:
            return None

    def agregar_periodo(self, periodo: "Periodo") -> bool:
        periodo_existente: Optional["Periodo"] = PeriodoUtil.identificarPeriodoPorFecha(
            self._periodos, periodo.fecha_inicio
        )
        if periodo_existente is None:
            self._periodos.append(periodo)
            self._periodos = PeriodoUtil.ordenarPeriodosPorFechaInicio(self._periodos)
            for producto in self._productos.values():
                self.agregar_producto_periodo_con_cantidad(producto, periodo, 0)
            return True
        else:
            return False

    def encontrar_periodo_por_fecha(self, fecha: datetime) -> Optional["Periodo"]:
        return PeriodoUtil.identificarPeriodoPorFecha(self._periodos, fecha)

    def agregar_producto_periodo_con_cantidad(
        self, producto: "Producto", periodo: "Periodo", cantidad: float
    ) -> float:
        producto_agregado: bool = self.agregar_producto(producto)
        if not producto_agregado:
            producto = self._productos[producto.codigo]
        periodo_agregado: bool = self.agregar_periodo(periodo)
        if not periodo_agregado:
            periodo = PeriodoUtil.identificarPeriodoPorFecha(
                self._periodos, periodo.fecha_inicio
            )
        total: float = 0
        if (producto, periodo) in self._contenido:
            total = self._contenido[(producto, periodo)]

        total = total + cantidad
        self._contenido[(producto, periodo)] = total

        return total

    def agregar_codigo_producto_fecha_con_cantidad(
        self, codigo_producto: str, fecha: datetime, cantidad: float
    ) -> float:
        producto : Optional["Producto"] = self.encontrar_producto_por_codigo(codigo_producto)
        periodo: Optional["Periodo"] = self.encontrar_periodo_por_fecha(fecha)
        if producto is not None and periodo is not None:
            return self.agregar_producto_periodo_con_cantidad(producto, periodo, cantidad)
        else:
            return 0

    def generar_dataframe(self) -> pd.DataFrame:
        data: List[Tuple[str, str, float]] = self.contenido_simplificado

        # Crear un DataFrame a partir de la lista de tuplas
        df = pd.DataFrame(data, columns=["Producto", "Período", "Cantidad"])

        # Usar pivot para reorganizar los datos
        df = df.pivot(index="Producto", columns="Período", values="Cantidad")

        return df

    def __repr__(self):
        return f"Orden(nombre={self.nombre!r}, contenido={self.contenido!r})"

    def __str__(self):
        return f"Orden {self.nombre} con {len(self.contenido)} líneas"


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
