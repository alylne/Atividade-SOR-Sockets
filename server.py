from Conversoes.tempo import *
from Conversoes.area import *

import socket

HOST = ''                                                                              # IP do servidor
PORT = 8080                                                                            # Porta do cliente ao servidor
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)                                  # Objeto do tipo socket

local = (HOST, PORT)                                                                   # Recebe IP e Porta
s.bind(local)                                                                          # Une o IP e a Porta
s.listen(1)                                                                            # Quantidade de conexões

while True:
    con, cliente = s.accept()                                                          # Aceita a conexão solicitada
    print('Conectado por', cliente)                                                    # Printa a conexão

    while True:
        result = con.recv(1024)                                                        # Recebe no maximo 1024 bytes
        if not result: break                                                           # Para o loop caso não haja mensagem
        result = result.decode('utf-8')                                                # Formatação em utf-8
        print(result)                                                                  # Mensagem recebida do client

        if ((result) == '1'):
            tempo = con.recv(1024)
            tempo = tempo.decode('utf-8')

            valor = con.recv(1024)
            valor = valor.decode('utf-8')

            resultado = converterTempo(str(tempo), float(valor))
            resultado = resultado.encode('utf-8')
            con.send(resultado)

        if ((result) == '2'):
            area = con.recv(1024)
            area = area.decode('utf-8')

            valor = con.recv(1024)
            valor = valor.decode('utf-8')

            resultado = converterArea(str(area), float(valor))
            resultado = resultado.encode('utf-8')
            con.send(resultado)


    print('Finalizando conexão com cliente', cliente)
    con.close()                                                                        # Finaliza a conexão


