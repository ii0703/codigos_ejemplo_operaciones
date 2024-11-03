from datetime import timedelta
from typing import Dict, List, Optional, Tuple

import numpy as np
import pandas as pd

from produccion.maquina import Maquina
from produccion.orden import Orden
from produccion.producto import Producto


class Linea:
    def __init__(
        self,
        nombre: str,
        secuencia_maquinas: List["Maquina"] = [],
    ):
        self._nombre = nombre
        self._secuencia_maquinas = secuencia_maquinas

    @property
    def nombre(self) -> str:
        return self._nombre

    @nombre.setter
    def nombre(self, value: str):
        self._nombre = value

    @property
    def secuencia_maquinas(self) -> List["Maquina"]:
        return self._secuencia_maquinas

    @secuencia_maquinas.setter
    def secuencia_maquinas(self, value: List["Maquina"]):
        self._secuencia_maquinas = value

    @property
    def secuencia(self) -> List[str]:
        return [m._codigo for m in self.secuencia_maquinas]

    def agregar(self, maquina: "Maquina") -> None:
        self.secuencia_maquinas.append(maquina)

    def agregar_duracion_producto(
        self, codigo_maquina: str, codigo_producto: str, duracion: timedelta
    ) -> None:
        for maquina in self.secuencia_maquinas:
            if maquina.codigo == codigo_maquina:
                maquina.agregar_duracion_producto(codigo_producto, duracion)

    def obtener_duracion_por_maquina_para_producto(
        self, codigo_producto: str
    ) -> List[Optional[Tuple["Maquina", timedelta]]]:
        duraciones: List[Tuple["Maquina", timedelta] | None] = []
        duracion: Optional[timedelta] = None
        for maq in self.secuencia_maquinas:
            duracion = maq.obtener_duracion_producto(codigo_producto=codigo_producto)
            if duracion is not None:
                duraciones.append((maq, duracion))
            else:
                duraciones.append(None)
        return duraciones

    def obtener_tiempo_produccion_producto(
        self, codigos_producto: List[str]
    ) -> Dict[str, Dict[str, timedelta]]:
        resultado: Dict[str, Dict[str, timedelta]] = {}
        for codigo_producto in codigos_producto:
            duraciones: List[Optional[Tuple["Maquina", timedelta]]] = (
                self.obtener_duracion_por_maquina_para_producto(codigo_producto)
            )
            if self.evaluar_duracion_por_maquina_para_producto(duraciones):
                resultado[codigo_producto] = {
                    maquina.codigo: duracion for maquina, duracion in duraciones
                }

        return resultado

    def calcular_tiempo_orden(self, orden: "Orden") -> pd.DataFrame:
        tiempo_producccion_unitaria: Dict[str, Dict[str, timedelta]] = (
            self.obtener_tiempo_produccion_producto(orden.productos)
        )
        datos: pd.DataFrame = orden.generar_dataframe()
        tiempos: Dict[str, Dict[str, timedelta]] = (
            self.obtener_tiempo_produccion_producto(orden.productos)
        )

        # Crear un nuevo DataFrame para almacenar los resultados
        df_resultado = pd.DataFrame(
            np.zeros((len(datos.index), len(datos.columns)), dtype="timedelta64[ns]"),
            index=datos.index,
            columns=datos.columns,
        )

        # Iterar sobre las filas (productos)
        for producto in datos.index:
            # Iterar sobre las filas (productos)
            # Obtener los tiempos de producción del producto
            timedeltas_segundos = [
                t.total_seconds() for t in tiempos[producto].values()
            ]
            for fecha in datos.columns:
                cantidad = datos.loc[producto, fecha]
                total = sum([t * cantidad for t in timedeltas_segundos])
                # Convertir la cantidad a timedelta (puedes ajustar la unidad según tus necesidades)
                tiempo_total = pd.to_timedelta(
                    total, unit="seconds"
                )  # 'hours', 'minutes', 'seconds', etc.
                df_resultado.loc[producto, fecha] = tiempo_total

        return df_resultado

    @staticmethod
    def evaluar_duracion_por_maquina_para_producto(
        duraciones: List[Optional[Tuple["Maquina", timedelta]]]
    ) -> bool:
        return all([d is not None for d in duraciones])

    def __repr__(self):
        return f"Linea(nombre={self.nombre!r}, secuencia_maquinas={self.secuencia_maquinas!r})"

    def __str__(self):
        return f"Línea {self.nombre} con {len(self.secuencia_maquinas)} máquinas"
