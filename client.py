import socket

HOST = '127.0.0.1'
PORT = 8080
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
local = (HOST, PORT)
s.connect(local)

verificador = 1
while verificador != 0:
    print("=====================================")
    menu = 'MENU'
    print(f'{menu:^36s}')
    result = input('Selecione uma opção para converter:\n'
                   '1 - Para converter unidades de tempo\n'
                   '2 - Para converter unidades de área\n'
                   '0 - Para sair\n'
                   '=====================================\n')

    # Loop para tratamento de erro na escolha da opção
    while result != '1' and result != '2' and result != '0':
        print('Valor inválido')
        print("====================================")

        result = input('Digite uma opcão válida:\n'
                       '1 - Para converter unidades de tempo\n'
                       '2 - Para converter unidades de área\n'
                       '0 - Para sair\n'
                       '====================================\n')

    while result != '0':
        # Menu para a conversão de tempo
        if result == '1':
            result = result.encode('utf-8')
            s.send(result)
            print("========================================================")
            print("Qual unidade de tempo você deseja converter?")
            print("1 - Hora(s) para minutos, segundos e milisegundos\n"
                  "2 - Minuto(s) para segundos, milisegundos e hora(s).\n"
                  "3 - Segundo(s) para milisegundos, minuto(s) e hora(s).\n"
                  "4 - Milisegundo(s) para segundo(s), minuto(s) e hora(s).\n"
                  "5 - Voltar para o Menu.")
            print("========================================================")
            tempo = input()

            # Condição para voltar para o menu
            if tempo == '5':
                break

            # Loop para tratamento de erro na escolha da opção
            while tempo != '1' and tempo != '2' and tempo != '3' and tempo != '4':
                print('Valor inválido')
                print("========================================================")

                print("Qual unidade de tempo você deseja converter?")
                print("1 - Hora(s) para minutos, segundos e milisegundos\n"
                      "2 - Minuto(s) para segundos, milisegundos e hora(s).\n"
                      "3 - Segundo(s) para milisegundos, minuto(s) e hora(s).\n"
                      "4 - Milisegundo(s) para segundo(s), minuto(s) e hora(s).\n"
                      "5 - Voltar para o Menu.")
                print("========================================================")
                tempo = input('\nDigite uma opção válida:  ')
            tempo = tempo.encode('utf-8')
            s.send(tempo)
            valor = -1

            # Loop para selecionar a opção
            while type(valor) != float:
                try:
                    valor = int(input("Qual o valor para conversão: "))
                    break
                except:
                    print("Valor inválido")
                    continue

            valor = str(valor).encode('utf-8')
            s.send(valor)
            result = s.recv(1024)  # result vai receber mensagem com no maximo 1024 bytes
            result = result.decode('utf-8')  # formatar a mensagem que vai vir em ascii
            print("O resultado da conversão foi: ", result)



        # Menu para a conversão de área
        elif result == '2':
            result = result.encode('utf-8')
            s.send(result)
            print("=========================================================================")
            print("Qual área você deseja fazer a conversão?")
            print("1 - Metro ao quadrado para Centímetro ao quadrado e Milimetro ao quadrado\n"
                  "2 - Centímetro ao quadrado para Metro ao quadrado e Milimetro ao quadrado\n"
                  "3 - Milimetro ao quadrado pra Metro ao quadrado e Centímetro ao quadrado\n"
                  "4 - Voltar para o Menu")
            print("=========================================================================")
            area = input()

            # Condição para voltar para o menu
            if area == '4':
                break

            # Loop para tratamento de erro na escolha da opção
            while area != '1' and area != '2' and area != '3':
                print('Valor inválido.')
                print("=========================================================================")
                print("Qual área você deseja fazer a conversão?")
                print("1 - Metro ao quadrado para Centímetro ao quadrado e Milimetro ao quadrado\n"
                      "2 - Centímetro ao quadrado para Metro ao quadrado e Milimetro ao quadrado\n"
                      "3 - Milimetro ao quadrado pra Metro ao quadrado e Centímetro ao quadrado\n"
                      "4 - Voltar para o Menu")
                print("=========================================================================")
                area = input('\nDigite uma opção válida:  ')
            area = area.encode('utf-8')
            s.send(area)
            valor = -1

            # Loop para selecionar a opção
            while type(valor) != float:
                try:
                    valor = int(input("Qual o valor para conversão: "))
                    break
                except:
                    print("Valor inválido.")
                    continue

            valor = str(valor).encode('utf-8')
            s.send(valor)
            result = s.recv(1024)  # Recebe no maximo 1024 bytes
            result = result.decode('utf-8')  # Formatação em string

            print("O resultado da conversão foi: ", result)
            result = input('\nDigite:'
                           '\n 1 - Para converter unidades de tempo'
                           '\n 2 - Para converter unidades de área.'
                           '\n Ou digite 0 para sair:  ')

# Fim do programa
print('Programa finalizado.')

s.close()
