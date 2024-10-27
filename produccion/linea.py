from datetime import timedelta
from typing import List, Optional, Tuple

from produccion.maquina import Maquina


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
    
    @staticmethod
    def evaluar_duracion_por_maquina_para_producto(duraciones: List[Optional[Tuple["Maquina", timedelta]]]) -> bool:
        return all([d is not None for d in duraciones])


    def __repr__(self):
        return f"Linea(nombre={self.nombre!r}, secuencia_maquinas={self.secuencia_maquinas!r})"

    def __str__(self):
        return f"Línea {self.nombre} con {len(self.secuencia_maquinas)} máquinas"