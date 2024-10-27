from datetime import date
from random import randint
from typing import List

import pandas as pd


from produccion.cliente import Producto
from produccion.orden import Orden
from produccion.periodo import Periodo, PeriodoUtil


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

# productos: List["Producto"] = orden.listar_productos()
# for producto in productos:
#     print(producto.codigo)

# periodos_prueba: List["Periodo"] = []
# periodos_prueba.append(Periodo(fecha_inicio=datetime(2024, 1, 3, 0, 0, 0)))
# periodos_prueba.append(Periodo(fecha_inicio=datetime(2024, 1, 5, 0, 0, 0)))
# periodos_prueba.append(Periodo(fecha_inicio=datetime(2024, 1, 2, 0, 0, 0)))
# periodos_prueba.append(Periodo(fecha_inicio=datetime(2024, 1, 1, 0, 0, 0)))
# periodos_prueba.append(Periodo(fecha_inicio=datetime(2024, 1, 4, 0, 0, 0)))

# for p in periodos_prueba:
#     print(p)

# print("Ordenados")
# periodos_ordenados: List["Periodo"] = PeriodoUtil.ordenarPeriodosPorFechaInicio(periodos_prueba)
# for p in periodos_ordenados:
#     print(p)

# fecha_para_buscar: datetime = datetime(2024, 1, 6, 12, 0, 0)
# periodo_encontrado: Optional["Periodo"] = PeriodoUtil.identificarPeriodoPorFecha(periodos_ordenados, fecha_para_buscar)
# print('Periodo encontrado:', periodo_encontrado, 'para la fecha ', fecha_para_buscar)

orden: Orden = Orden(nombre="ORD9814257")
for producto in productos:
    for periodo in periodos:
        orden.agregar_producto_con_detalle(producto=producto, periodo=periodo, cantidad=randint(0, 1000))

df: pd.DataFrame = orden.generar_dataframe()

print(df)