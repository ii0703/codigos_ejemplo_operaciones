from datetime import timedelta


class TimeDeltaUtils:

    @staticmethod
    def redondear_timedelta_segundos(
        duracion: timedelta, segundos_multiplo: int
    ) -> timedelta:
        segundos: float = duracion.total_seconds()
        segundos_ajustados = round(segundos / segundos_multiplo) * segundos_multiplo
        return timedelta(seconds=segundos_ajustados)

    @staticmethod
    def calcular_duracion_unidad_por_minuto(cantidad_en_un_minuto) -> timedelta:
        return TimeDeltaUtils.redondear_timedelta_segundos(
            timedelta(minutes=1) / cantidad_en_un_minuto, 1
        )
    
    @staticmethod
    def calcular_duracion_unidad_por_hora(cantidad_en_una_hora) -> timedelta:
        return TimeDeltaUtils.redondear_timedelta_segundos(
            timedelta(hours=1) / cantidad_en_una_hora, 1
        )