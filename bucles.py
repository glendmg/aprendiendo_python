def potencia (numero):
    exponente = 1
    resultado_potencia = 0

    while (resultado_potencia < 1000000):
        resultado_potencia = numero ** exponente
        print('Potencia de {} elevado a la {} es {}'.format(numero, exponente, resultado_potencia))
        exponente += 1


def run():
    valor = int (input("Escribe el numero al cual quieres averiguarle la potencia hasta menos de 1 000 000: "))
    potencia(valor)


if __name__ == '__main__':
    run()