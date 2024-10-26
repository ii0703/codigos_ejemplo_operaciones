from producion.base import Producto
from producion.planificacion import Orden, Periodo, PeriodoUtil, OrdenUtil
from secuenciamiento.base import Maquina, Linea

from datetime import datetime, timedelta, date
from typing import List, Dict
from random import randint

import pandas as pd

periodos: List['Periodo'] = PeriodoUtil.generarPeriodosPorNumeroDias(
    date(2024, month=1, day=1), cantidad_periodos=7, cantidad_dias=1
)

productos: List['Producto'] = []
productos.append(Producto(codigo='A01', nombre='Sillas de Camping'))
productos.append(Producto(codigo='A02', nombre='Sillas de Camping con reposamanos'))
productos.append(Producto(codigo='C01', nombre='Tiendas de campañas de 2 personas'))
productos.append(Producto(codigo='C02', nombre='Tiendas de campañas de 4 personas'))
productos.append(Producto(codigo='C03', nombre='Tiendas de campañas de 6 personas'))

print(len(periodos), periodos)
# print(productos)
#orden: Orden = OrdenUtil.generarOrdenConProductoPeriodosEnCero('ORD9814257', productos=productos, periodos=periodos)
orden: Orden = Orden(nombre='ORD9814257')
cantidades_demanda = [100, 350, 200, 450, 600, 125, 400]
OrdenUtil.agregarProductoDetalle(orden=orden, producto=productos[0], periodos=periodos, demandas=cantidades_demanda)
cantidades_demanda = [125, 250, 150, 375, 450, 175, 325]
OrdenUtil.agregarProductoDetalle(orden=orden, producto=productos[2], periodos=periodos, demandas=cantidades_demanda)
cantidades_demanda = [200, 150, 425, 50, 150, 325, 250]
OrdenUtil.agregarProductoDetalle(orden=orden, producto=productos[4], periodos=periodos, demandas=cantidades_demanda)

maqA: Maquina = Maquina(codigo='A',nombre='Máquina A')
maqB: Maquina = Maquina(codigo='B',nombre='Máquina B')
maqC: Maquina = Maquina(codigo='C',nombre='Máquina C')

lineaA: Linea = Linea('Línea de Principal')
lineaA.agregar(maqB)
lineaA.agregar(maqC)
lineaA.agregar(maqA)

print(lineaA.secuencia)