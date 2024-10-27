from datetime import date, datetime
from random import randint
from typing import List

import pandas as pd

from produccion.orden import Orden
from produccion.periodo import Periodo, PeriodoUtil
from produccion.producto import Producto


periodos: List["Periodo"] = PeriodoUtil.generarPeriodosPorNumeroDias(
    date(2024, month=1, day=1), cantidad_periodos=4, cantidad_dias=1
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
# orden: Orden = Orden(nombre="ORD9814257")
# cantidades_demanda = [100, 350, 200, 450, 600, 125, 400]
# OrdenUtil.agregarProductoDetalle(
#     orden=orden, producto=productos[0], periodos=periodos, demandas=cantidades_demanda
# )
# cantidades_demanda = [125, 250, 150, 375, 450, 175, 325]
# OrdenUtil.agregarProductoDetalle(
#     orden=orden, producto=productos[2], periodos=periodos, demandas=cantidades_demanda
# )
# cantidades_demanda = [200, 150, 425, 50, 150, 325, 250]
# OrdenUtil.agregarProductoDetalle(
#     orden=orden, producto=productos[4], periodos=periodos, demandas=cantidades_demanda
# )

# # Se crean las máquinas y se establece su código y nombre
# maqA: Maquina = Maquina(codigo="A", nombre="Máquina A")
# maqB: Maquina = Maquina(codigo="B", nombre="Máquina B")
# maqC: Maquina = Maquina(codigo="C", nombre="Máquina C")

# # Se crear la línea de producción y se establece la secuencia de las máquinas
# lineaA: Linea = Linea("Línea de Principal")
# lineaA.agregar(maqB)
# lineaA.agregar(maqC)
# lineaA.agregar(maqA)

# print(lineaA.secuencia)

# # Se establece la duración de cada producto en cada máquina para la línea de producción
# lineaA.agregar_duracion_producto(
#     codigo_maquina="A",
#     codigo_producto="A01",
#     duracion=TimeDeltaUtils.calcular_duracion_unidad_por_hora(15),
# )
# lineaA.agregar_duracion_producto(
#     codigo_maquina="B",
#     codigo_producto="A01",
#     duracion=TimeDeltaUtils.calcular_duracion_unidad_por_hora(25),
# )
# lineaA.agregar_duracion_producto(
#     codigo_maquina="C",
#     codigo_producto="A01",
#     duracion=TimeDeltaUtils.calcular_duracion_unidad_por_hora(12),
# )
# lineaA.agregar_duracion_producto(
#     codigo_maquina="A",
#     codigo_producto="C01",
#     duracion=TimeDeltaUtils.calcular_duracion_unidad_por_hora(11),
# )
# lineaA.agregar_duracion_producto(
#     codigo_maquina="B",
#     codigo_producto="C01",
#     duracion=TimeDeltaUtils.calcular_duracion_unidad_por_hora(17),
# )
# lineaA.agregar_duracion_producto(
#     codigo_maquina="C",
#     codigo_producto="C01",
#     duracion=TimeDeltaUtils.calcular_duracion_unidad_por_hora(7),
# )
# lineaA.agregar_duracion_producto(
#     codigo_maquina="A",
#     codigo_producto="C03",
#     duracion=TimeDeltaUtils.calcular_duracion_unidad_por_hora(14),
# )
# lineaA.agregar_duracion_producto(
#     codigo_maquina="B",
#     codigo_producto="C03",
#     duracion=TimeDeltaUtils.calcular_duracion_unidad_por_hora(15),
# )
# lineaA.agregar_duracion_producto(
#     codigo_maquina="C",
#     codigo_producto="C03",
#     duracion=TimeDeltaUtils.calcular_duracion_unidad_por_hora(20),
# )

# print("A01")
# duraciones: List[Optional[Tuple["Maquina", timedelta]]] = lineaA.obtener_duracion_por_maquina_para_producto("A01")
# for duracion in duraciones:
#     print(duracion[0].nombre, duracion[1])

# print("C01")
# duraciones: List[Optional[Tuple["Maquina", timedelta]]] = lineaA.obtener_duracion_por_maquina_para_producto("C01")
# for duracion in duraciones:
#     print(duracion[0].nombre, duracion[1])

# print("C03")
# duraciones: List[Optional[Tuple["Maquina", timedelta]]] = lineaA.obtener_duracion_por_maquina_para_producto("C03")
# for duracion in duraciones:
#     print(duracion[0].nombre, duracion[1])


orden: Orden = Orden(nombre="ORD9814257")


for periodo in periodos:
    orden.agregar_periodo(periodo)

for producto in productos[:4]:
    orden.agregar_producto(producto)


df: pd.DataFrame = orden.generar_dataframe()
print(df)

orden.agregar_codigo_producto_fecha_con_cantidad("A01", datetime(2024, 1, 1), 100)
orden.agregar_codigo_producto_fecha_con_cantidad("A02", datetime(2024, 1, 2), 100)
orden.agregar_codigo_producto_fecha_con_cantidad("C01", datetime(2024, 1, 3), 100)
orden.agregar_codigo_producto_fecha_con_cantidad("C02", datetime(2024, 1, 4), 100)
orden.agregar_codigo_producto_fecha_con_cantidad("C02", datetime(2024, 1, 4, 15, 30), 300)

df: pd.DataFrame = orden.generar_dataframe()
print(df)

