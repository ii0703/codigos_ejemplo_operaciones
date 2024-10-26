from produccion.base import Producto

from typing import List, Dict, Tuple, Optional
from datetime import timedelta


class CalculadoraTiempoSecuencia:
    def calcular_tiempo_secuencia(self, linea: "Linea", producto: Producto) -> float:
        tiempo_total = 0
        for maquina in linea.secuencia_maquinas:
            tiempo_maquina = linea.tiempos_procesamiento[producto][maquina]
            tiempo_total += tiempo_maquina
        return tiempo_total


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
            print('a')
            duracion = maq.obtener_duracion_producto(codigo_producto=codigo_producto)
            print('b')
            if duracion is not None:
                duraciones.append((maq, duracion))
            else:
                duraciones.append(None)
        return duraciones


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
        print('entro')
        salida: Optional[timedelta] = None
        if codigo_producto in self.duracion_por_producto:
            salida = self.duracion_por_producto[codigo_producto]
        return salida

    def agregar_duracion_producto(
        self, codigo_producto: str, duracion: timedelta
    ) -> None:
        self.duracion_por_producto[codigo_producto] = duracion


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
