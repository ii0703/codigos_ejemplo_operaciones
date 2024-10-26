from typing import List, Dict


class Producto:
    def __init__(
        self,
        codigo: str,
        nombre: str,
        costo: float = 0,
        cantidad_total: int = 0,
        cantidad_disponible: int = 0,
    ):
        self._codigo = codigo
        self._nombre = nombre
        self._costo = costo
        self._cantidad_total = cantidad_total
        self._cantidad_disponible = cantidad_disponible

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
    def costo(self) -> float:
        return self._costo

    @costo.setter
    def costo(self, value: float):
        self._costo = value

    @property
    def cantidad_total(self) -> int:
        return self._cantidad_total

    @cantidad_total.setter
    def cantidad_total(self, value: int):
        self._cantidad_total = value

    @property
    def cantidad_disponible(self) -> int:
        return self._cantidad_disponible

    @cantidad_disponible.setter
    def cantidad_disponible(self, value: int):
        self._cantidad_disponible = value

    def __str__(self):
        return "([{:_>20}]:-{:40})".format(self.codigo, self.nombre)

    def __repr__(self):
        return "([{:_>20}]:{:40})".format(self.codigo, self.nombre)


class MateriaPrima(Producto):
    pass  # Hereda de Producto


class Cliente:
    def __init__(self, codigo: str, nombre: str):
        self._codigo = codigo
        self._nombre = nombre

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

    def __repr__(self):
        return f"Cliente(codigo={self.codigo!r}, nombre={self.nombre!r})"

    def __str__(self):
        return f"Cliente {self.nombre} con código {self.codigo}"