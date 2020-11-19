from campeonato import campeonato


def equipo_ganador(campeonato):
    max_puntos_totales = 0
    for equipo in campeonato:
        puntos_equipo_actual = campeonato[equipo][0] * \
            3 + campeonato[equipo][1] * 1
        if puntos_equipo_actual > max_puntos_totales:
            max_puntos_totales = puntos_equipo_actual
            equipo_campeon = equipo
    return print("El equipo campeon es {} con {} puntos.".format(equipo_campeon, max_puntos_totales))


def equipo_perdedor(campeonato):
    min_puntos_totales = 100
    for equipo in campeonato:
        puntos_equipo_actual = campeonato[equipo][0] * \
            3 + campeonato[equipo][1] * 1
        if puntos_equipo_actual < min_puntos_totales:
            min_puntos_totales = puntos_equipo_actual
            equipo_desciende = equipo
    return print("El equipo que desciende es {} con {} puntos.".format(equipo_desciende, min_puntos_totales))


def mas_empates(campeonato):
    max_empates = 0
    for equipo in campeonato:
        empates = campeonato[equipo][1]
        if empates > max_empates:
            max_empates = empates
            equipo_max_empates = equipo
    return print("El equipo que mas partidos empato es {} con {} partidos.".format(equipo_max_empates, max_empates))


def ratio_goles(campeonato):
    max_ratio_goles = 0
    for equipo in campeonato:
        ratio_goles_equipo = campeonato[equipo][3] / campeonato[equipo][4]
        if ratio_goles_equipo > max_ratio_goles:
            max_ratio_goles = ratio_goles_equipo
            equipo_max_ratio = equipo
    return print("El equipo con mejor proporcion goleadora es {} con {}.".format(equipo_max_ratio, max_ratio_goles))


def mostrar_estadisticas():
    equipo_ganador(campeonato)
    equipo_perdedor(campeonato)
    mas_empates(campeonato)
    ratio_goles(campeonato)


mostrar_estadisticas()
