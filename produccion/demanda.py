from produccion.orden import Orden


class Demanda(Orden):

    def __repr__(self):
        return f"Demanda(nombre={self.nombre!r}, detalle={self.detalle!r})"

    def __str__(self):
        return f"Demanda {self.nombre} con {len(self.detalle)} productos"
