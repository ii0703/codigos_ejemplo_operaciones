from datetime import timedelta
from typing import Dict, List, Optional

from produccion.producto import Producto


class Maquina:
    def __init__(
        self,
        codigo: str,
        nombre: str,
        buffer_entrada: "Buffer" = "Buffer",
        buffer_salida: "Buffer" = "Buffer",
    ):
        self._codigo: str = codigo
        self._nombre: str = nombre
        self._buffer_entrada: "Buffer" = buffer_entrada
        self._buffer_salida: "Buffer" = buffer_salida
        self._duracion_por_producto: Dict["str", timedelta] = {}

    @property
    def codigo(self) -> str:
        return self._codigo

    @codigo.setter
    def codigo(self, value: str):
        self._codigo = value

    @property
    def nombre(self) -> str:
        return self._nombre

    @nombre.setter
    def nombre(self, value: str):
        self._nombre = value

    @property
    def buffer_entrada(self) -> "Buffer":
        return self._buffer_entrada

    @buffer_entrada.setter
    def buffer_entrada(self, value: "Buffer"):
        self._buffer_entrada = value

    @property
    def buffer_salida(self) -> "Buffer":
        return self._buffer_salida

    @buffer_salida.setter
    def buffer_salida(self, value: "Buffer"):
        self._buffer_salida = value

    @property
    def duracion_por_producto(self) -> Dict["str", timedelta]:
        return self._duracion_por_producto

    @duracion_por_producto.setter
    def duracion_por_producto(self, value: Dict["str", timedelta]) -> None:
        self._duracion_por_producto = value

    def obtener_duracion_producto(self, codigo_producto: str) -> Optional[timedelta]:
        salida: Optional[timedelta] = None
        if codigo_producto in self.duracion_por_producto:
            salida = self.duracion_por_producto[codigo_producto]
        return salida

    def agregar_duracion_producto(
        self, codigo_producto: str, duracion: timedelta
    ) -> None:
        self.duracion_por_producto[codigo_producto] = duracion

    def __repr__(self):
        return f"Maquina(codigo={self.codigo!r}, nombre={self.nombre!r})"

    def __str__(self):
        return f"Máquina {self.nombre} con código {self.codigo}"



class Buffer:
    def __init__(self, capacidad: int = 10):  # Capacidad por defecto: 10
        self._capacidad = capacidad
        self._productos: List[Producto] = []

    @property
    def capacidad(self) -> int:
        return self._capacidad

    @capacidad.setter
    def capacidad(self, value: int):
        self._capacidad = value

    def recibir_producto(self, producto: Producto):
        if len(self._productos) < self._capacidad:
            self._productos.append(producto)
        else:
            raise ValueError("El buffer está lleno.")

    def despachar_producto(self) -> Producto:
        if self._productos:
            return self._productos.pop(0)  # FIFO
        else:
            raise ValueError("El buffer está vacío.")

    def __repr__(self):
        return "Buffer()"

    def __str__(self):
        return "Buffer de la máquina"