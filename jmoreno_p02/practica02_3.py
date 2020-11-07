print("Benvenido, por favor introduce los siguientes valores:")
peso = float(input("\nIntroduce tu peso en kilogramos: "))
altura = float(input("Introduce tu altura (en metros): "))

def calculaIMC(peso, altura):
    return peso / (altura ** 2) 

print("\nTu IMC con un peso de " + str(peso) + " y una altura de " + str(altura) + " es:")
print(str(round(calculaIMC(peso, altura), 2)))