def converterTempo(tempo, valor):
    if (tempo == '1'):
        minutos = valor * 60
        segundos = valor * 3600
        milisegundos = valor * 216000

        return (str(valor) + ' hora(s) é igual a '
                + str(minutos) + ' minutos, '
                + str(segundos) + ' segundos e '
                + str(milisegundos) + ' milisegundos.')

    if (tempo == '2'):
        segundos = valor * 60
        milisegundos = valor * 3600
        horas = valor / 60

        return (str(valor) + ' minuto(s) é igual a '
                + str(segundos) + ' segundos, '
                + str(milisegundos) + ' milisegundos e '
                + str(horas) + ' hora(s).')

    if (tempo == '3'):
        milisegundos = valor * 60
        minutos = valor / 60
        horas = valor / 3600

        return (str(valor) + ' segundo(s) é igual a '
                + str(milisegundos) + ' milisegundos, '
                + str(minutos) + ' minutos e '
                + str(horas) + ' hora(s).')

    if (tempo == '4'):
        segundos = valor / 60
        minutos = valor / 3600
        horas = valor / 216000

        return (str(valor) + ' milisegundo(s) é igual a '
                + str(segundos) + ' segundos, '
                + str(minutos) + ' minutos e '
                + str(horas) + ' hora(s).')
