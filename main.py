from producion.base import Producto
from producion.planificacion import Orden, Periodo, PeriodoUtil

from datetime import datetime, timedelta, date
from typing import List, Dict
from random import randint

import pandas as pd

orden: Orden = Orden()

periodos: List["Periodo"] = PeriodoUtil.generarPeriodosPorNumeroDias(
    date(2024, month=1, day=1), cantidad_periodos=7, cantidad_dias=2
)

periodos2: List["Periodo"] = PeriodoUtil.generarPeriodosPorNumeroSemanas(
    date(2024, month=1, day=1), cantidad_periodos=7, cantidad_semanas=2
)

periodos3: List["Periodo"] = PeriodoUtil.generarPeriodosPorNumeroHoras(
    datetime(2024, month=1, day=1, hour=8, minute=0), cantidad_periodos=9, cantidad_horas=1
)

print(periodos)
print(periodos2)
print(periodos3)

# productos: List["Producto"] = []

# productos.append(Producto(codigo="A01", nombre="Sillas de Camping"))
# productos.append(Producto(codigo="A02", nombre="Sillas de Camping con reposamanos"))
# productos.append(Producto(codigo="C01", nombre="Tiendas de campañas de 2 personas"))
# productos.append(Producto(codigo="C02", nombre="Tiendas de campañas de 4 personas"))
# productos.append(Producto(codigo="C03", nombre="Tiendas de campañas de 6 personas"))
# print(productos)

# fecha_inicio = datetime(year=2024, month=1, day=1, hour=8, minute=0)
# delta = timedelta(hours=1)

# for producto in productos:
#     datos: Dict["Periodo", float] = {}
#     for i in range(8):
#         periodo = Periodo(fecha_inicio=fecha_inicio + (delta * i), delta=delta)
#         datos[periodo] = randint(1, 10)

#     orden.agregar_producto_con_periodos(producto=producto, periodo=datos)

# for producto, periodos in orden.productos.items():
#     print(producto)
#     for periodo, cantidad in periodos.items():
#         print("{} {:10.2f}".format(periodo, cantidad))

# # Convertir a DataFrame
# df = pd.DataFrame.from_dict(productos, orient="index")

# # # Ajustar nombres de columnas y filas
# # df.columns = ['Periodo ' + str(col) for col in df.columns]
# # df.index = ['Producto ' + str(i+1) for i in range(len(df))]

# print(df)
