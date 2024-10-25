from producion.base import Producto
from typing import List, Dict


class CalculadoraTiempoSecuencia:
    def calcular_tiempo_secuencia(self, linea: "Linea", producto: Producto) -> float:
        """
        Calcula el tiempo total de procesamiento de un producto en una línea.
        """
        tiempo_total = 0
        for maquina in linea.secuencia_maquinas:
            tiempo_maquina = linea.tiempos_procesamiento[producto][maquina]
            tiempo_total += tiempo_maquina
        return tiempo_total


class Linea:
    def __init__(
        self,
        nombre: str,
        producto: Producto,
        secuencia_maquinas: List["Maquina"],
        tiempos_procesamiento: Dict[Producto, Dict["Maquina", float]],
    ):
        """
        secuencia_maquinas: Lista de máquinas en la línea de producción.
        tiempos_procesamiento: Diccionario con Productos como llaves y un
                               diccionario como valor. Este segundo
                               diccionario tiene como llave la máquina y
                               como valor el tiempo de procesamiento
                               por unidad de producto en esa máquina.
        """
        self._nombre = nombre
        self._producto = producto
        self._secuencia_maquinas = secuencia_maquinas
        self._tiempos_procesamiento = tiempos_procesamiento

    @property
    def nombre(self) -> str:
        return self._nombre

    @nombre.setter
    def nombre(self, value: str):
        self._nombre = value

    @property
    def producto(self) -> Producto:
        return self._producto

    @producto.setter
    def producto(self, value: Producto):
        self._producto = value

    @property
    def secuencia_maquinas(self) -> List["Maquina"]:
        return self._secuencia_maquinas

    @secuencia_maquinas.setter
    def secuencia_maquinas(self, value: List["Maquina"]):
        self._secuencia_maquinas = value

    @property
    def tiempos_procesamiento(self) -> Dict[Producto, Dict["Maquina", float]]:
        return self._tiempos_procesamiento

    @tiempos_procesamiento.setter
    def tiempos_procesamiento(self, value: Dict[Producto, Dict["Maquina", float]]):
        self._tiempos_procesamiento = value


class Maquina:
    def __init__(
        self,
        codigo: str,
        nombre: str,
        buffer_entrada: "Buffer",
        buffer_salida: "Buffer",
    ):
        self._codigo = codigo
        self._nombre = nombre
        self._buffer_entrada = buffer_entrada
        self._buffer_salida = buffer_salida

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
