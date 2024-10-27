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