from produccion.base import Producto
from produccion.planificacion import Orden, Periodo
from secuenciamiento.base import Maquina, Linea
from produccion.utils import TimeDeltaUtils, PeriodoUtil, OrdenUtil

from datetime import datetime, timedelta, date
from typing import List, Dict, Tuple, Optional
from random import randint

import pandas as pd

# Se crean los periodos de tiempo que serán usados en la planificación
periodos: List["Periodo"] = PeriodoUtil.generarPeriodosPorNumeroDias(
    date(2024, month=1, day=1), cantidad_periodos=7, cantidad_dias=1
)

# Se crean los productos que serán usados en la planificación, 
# para no estár creando productos, se almacenarán en una lista y luego se usarán
# a través de su posición para registrarlos en la orden
productos: List["Producto"] = []
productos.append(Producto(codigo="A01", nombre="Sillas de Camping"))
productos.append(Producto(codigo="A02", nombre="Sillas de Camping con reposamanos"))
productos.append(Producto(codigo="C01", nombre="Tiendas de campañas de 2 personas"))
productos.append(Producto(codigo="C02", nombre="Tiendas de campañas de 4 personas"))
productos.append(Producto(codigo="C03", nombre="Tiendas de campañas de 6 personas"))

# print(len(periodos), periodos)

# Se crea la orden y se establece su nombre
# Se agregan los productos a la orden con sus respectivas cantidades de demanda
orden: Orden = Orden(nombre="ORD9814257")
cantidades_demanda = [100, 350, 200, 450, 600, 125, 400]
OrdenUtil.agregarProductoDetalle(
    orden=orden, producto=productos[0], periodos=periodos, demandas=cantidades_demanda
)
cantidades_demanda = [125, 250, 150, 375, 450, 175, 325]
OrdenUtil.agregarProductoDetalle(
    orden=orden, producto=productos[2], periodos=periodos, demandas=cantidades_demanda
)
cantidades_demanda = [200, 150, 425, 50, 150, 325, 250]
OrdenUtil.agregarProductoDetalle(
    orden=orden, producto=productos[4], periodos=periodos, demandas=cantidades_demanda
)

# Se crean las máquinas y se establece su código y nombre
maqA: Maquina = Maquina(codigo="A", nombre="Máquina A")
maqB: Maquina = Maquina(codigo="B", nombre="Máquina B")
maqC: Maquina = Maquina(codigo="C", nombre="Máquina C")

# Se crear la línea de producción y se establece la secuencia de las máquinas
lineaA: Linea = Linea("Línea de Principal")
lineaA.agregar(maqB)
lineaA.agregar(maqC)
lineaA.agregar(maqA)

# print(lineaA.secuencia)

# Se establece la duración de cada producto en cada máquina para la línea de producción
lineaA.agregar_duracion_producto(
    codigo_maquina="A",
    codigo_producto="A01",
    duracion=TimeDeltaUtils.calcular_duracion_unidad_por_hora(15),
)
lineaA.agregar_duracion_producto(
    codigo_maquina="B",
    codigo_producto="A01",
    duracion=TimeDeltaUtils.calcular_duracion_unidad_por_hora(25),
)
lineaA.agregar_duracion_producto(
    codigo_maquina="C",
    codigo_producto="A01",
    duracion=TimeDeltaUtils.calcular_duracion_unidad_por_hora(12),
)
lineaA.agregar_duracion_producto(
    codigo_maquina="A",
    codigo_producto="C01",
    duracion=TimeDeltaUtils.calcular_duracion_unidad_por_hora(11),
)
lineaA.agregar_duracion_producto(
    codigo_maquina="B",
    codigo_producto="C01",
    duracion=TimeDeltaUtils.calcular_duracion_unidad_por_hora(17),
)
lineaA.agregar_duracion_producto(
    codigo_maquina="C",
    codigo_producto="C01",
    duracion=TimeDeltaUtils.calcular_duracion_unidad_por_hora(7),
)
lineaA.agregar_duracion_producto(
    codigo_maquina="A",
    codigo_producto="C03",
    duracion=TimeDeltaUtils.calcular_duracion_unidad_por_hora(14),
)
lineaA.agregar_duracion_producto(
    codigo_maquina="B",
    codigo_producto="C03",
    duracion=TimeDeltaUtils.calcular_duracion_unidad_por_hora(15),
)
lineaA.agregar_duracion_producto(
    codigo_maquina="C",
    codigo_producto="C03",
    duracion=TimeDeltaUtils.calcular_duracion_unidad_por_hora(20),
)

# duraciones: List[Optional[Tuple["Maquina", timedelta]]] = lineaA.obtener_duracion_por_maquina_para_producto("A01")
# for duracion in duraciones:
#     print(duracion[0].nombre, duracion[1])

# duraciones: List[Optional[Tuple["Maquina", timedelta]]] = lineaA.obtener_duracion_por_maquina_para_producto("C01")
# for duracion in duraciones:
#     print(duracion[0].nombre, duracion[1])

# duraciones: List[Optional[Tuple["Maquina", timedelta]]] = lineaA.obtener_duracion_por_maquina_para_producto("C03")
# for duracion in duraciones:
#     print(duracion[0].nombre, duracion[1])

# productos: List["Producto"] = orden.listar_productos()
# for producto in productos:
#     print(producto.codigo)

# test
