def es_palindromo(frase):
    frase_limpia= frase.replace(' ','').lower()
    if (frase_limpia == frase_limpia[::-1]):
        print("¡ES PALÍNDROMO!")
    else:
        print("NO ES PALINDROMO")

def potenciacion(numero):
    for i in range(11):
        print("El número {} elevado a la {} es {}".format(numero, i, numero**i))
    

def run():
    salida = False
    while salida == False:
        menu = """
        Bienvenido al conversor de monedas

        1- Averiguar si una expresión es palíndromo
        2- Calcular la potencia de un numero hasta la décima potencia
        3- Salir

        Elige una opcion: """
        opcion= int(input(menu))

        if opcion == 1:
            salida= False
            print("\nAveriguar si una frase es palíndromo...")
            es_palindromo(frase= input("Ingrese una frase a evaluar: "))
        
        elif opcion == 2:
            salida= False
            print("\nElevar hasta 10 un número...\n")
            potenciacion(int(input("Ingrese el número potenciar hasta 10: ")))

        elif opcion == 3:
            print("Hasta luego.\n")
            salida= True 
        else:
            print("Seleccione una opción. ")


if __name__ == '__main__':
    run()
    