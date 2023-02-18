def compra_vemta (cantidad, tipo_cambio):
    monedas= cantidad * tipo_cambio
    return  monedas

print("¿Comprar o vender dólares?") 
operacion= int( input("Ingrese 1) Compra  2) Venta"))

if operacion == 1:
    cantidad_moneda= int (input("Ingrese ca cantidad de dólares a comprar: "))
    seleccionar_cambio= int( input("Ingrese el tipo de cambio, sugerido 576: "))
    print("Su compra en dolares equilave a", compra_vemta(cantidad_moneda, seleccionar_cambio), " colones.")
else:
    cantidad_moneda= int (input("Ingrese ca cantidad de dólares a vender: "))
    seleccionar_cambio= int( input("Ingrese el tipo de cambio, sugerido 565: "))
    print("Su venta de dólares equilave a", compra_vemta(cantidad_moneda, seleccionar_cambio), " colones.")

