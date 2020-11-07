print("Benvenido, por favor introduce los siguientes valores:")
base = float(input("\nIntroduce la longitud de la base del triángulo: "))
altura = float(input("Introduce la altura del triángulo: "))

def calculaAreaTriangulo(base, altura):
    return (base * altura) / 2

print("\nEl área del triángulo con una base de " + str(base) + " y una altura de " + str(altura) + " es:")
print(str(round(calculaAreaTriangulo(base, altura), 2)))