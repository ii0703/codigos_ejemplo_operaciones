from producion.base import Producto
from producion.planificacion import Orden, Periodo, PeriodoUtil, OrdenUtil
from secuenciamiento.base import Maquina, Linea

from datetime import datetime, timedelta, date
from typing import List, Dict
from random import randint

import pandas as pd

periodos: List['Periodo'] = PeriodoUtil.generarPeriodosPorNumeroDias(
    date(2024, month=1, day=1), cantidad_periodos=7, cantidad_dias=2
)

productos: List['Producto'] = []
productos.append(Producto(codigo='A01', nombre='Sillas de Camping'))
productos.append(Producto(codigo='A02', nombre='Sillas de Camping con reposamanos'))
productos.append(Producto(codigo='C01', nombre='Tiendas de campañas de 2 personas'))
productos.append(Producto(codigo='C02', nombre='Tiendas de campañas de 4 personas'))
productos.append(Producto(codigo='C03', nombre='Tiendas de campañas de 6 personas'))

# print(periodos)
# print(productos)
orden: Orden = OrdenUtil.generarOrdenConProductoPeriodosEnCero('ORD9814257', productos=productos, periodos=periodos)

maqA: Maquina = Maquina(codigo='A',nombre='Máquina A')
maqB: Maquina = Maquina(codigo='B',nombre='Máquina B')
maqC: Maquina = Maquina(codigo='C',nombre='Máquina C')

lineaA: Linea = Linea('Línea de Principal')
lineaA.agregar(maqB)
lineaA.agregar(maqC)
lineaA.agregar(maqA)

print(lineaA.secuencia)