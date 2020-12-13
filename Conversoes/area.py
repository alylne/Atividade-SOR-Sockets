def converterArea(area, valor):
    if (area == '1'):
        cm = valor * 100
        mm = valor * 1000000

        return (str(valor) + ' m² é igual a: '
                + str(cm) + ' cm² e '
                + str(mm) + ' mm².')

    if (area == '2'):
        m = valor * 0.001
        mm = valor * 100

        return (str(valor) + ' cm² é igual a: '
                + str(m) + ' m² e '
                + str(mm) + ' mm².')

    if (area == '3'):
        m = valor / 1000000
        cm = valor / 100

        return (str(valor) + ' mm² é igual a: '
                + str(m) + ' m² e '
                + str(cm) + ' cm².')