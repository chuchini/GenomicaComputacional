def calculaDescuento(total_compra):
    nuevo_total_compra = total_compra
    if (total_compra >= 100):
        nuevo_total_compra = total_compra - (total_compra * 0.10)

    return nuevo_total_compra

total_compra = float(input('Ingresa el total de la compra: '))
print("Su total final es: " + str(calculaDescuento(total_compra)))