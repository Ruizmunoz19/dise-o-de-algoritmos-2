# Elabora un algoritmo y su debido proceso de prueba de un escritorio que permita obtener la factorial de un numero

numero = int(input("Ingresa un número entero no negativo: "))

factorial = 1

if numero < 0:
    print("Error: El número debe ser no negativo.")
elif numero == 0:
    print("El factorial de 0 es 1")
else:
    for i in range(1, numero + 1):
        factorial *= i
    print(f"El factorial de {numero} es {factorial}")

    # Se desea conocer para un grupo de 10 personas el total de personas por rango de edades. Los rangos son los siguientes 0-20,  20-30, 30-40, 40-60 y mayores de 60. Elabore un algoritmo y la prueba de escritorio que permita mostrar los totales respectivos

    total_0_20 = 0
    total_20_30 = 0
    total_30_40 = 0
    total_40_60 = 0
    total_mayores_60 = 0

    for i in range(10):
        edad = int(input(f"Ingrese la edad de la persona {i + 1}: "))

        if edad <= 20:
            total_0_20 += 1
        elif edad <= 30:
            total_20_30 += 1
        elif edad <= 40:
            total_30_40 += 1
        elif edad <= 60:
            total_40_60 += 1
        else:
            total_mayores_60 += 1

    print("Total de personas por rango de edades:")
    print(f"0-20 años: {total_0_20}")
    print(f"20-30 años: {total_20_30}")
    print(f"30-40 años: {total_30_40}")
    print(f"40-60 años: {total_40_60}")
    print(f"Mayores de 60 años: {total_mayores_60}")

#Elabora un algoritmo que permita las tablas de multiplicar del 1 al 100 de un numero ingresado por el usuario. Recuerde realizar la prueba de escritorio

numero = int(input("Ingresa un número para generar su tabla de multiplicar: "))

print(f"Tabla de multiplicar del {numero}:")

for multiplicador in range(1, 101):
    producto = numero * multiplicador
    print(f"{numero} x {multiplicador} = {producto}")

#Realice un programa que permita saber el costo total de 10 productos cualquiera y que al final muestre el precio antes IVA y el precio después de IVA de la compra

IVA = 0.16

costo_total_antes_iva = 0
costo_total_despues_iva = 0

for i in range(1, 11):
    costo_producto = float(input(f"Ingrese el costo del producto {i}: $"))
    costo_total_antes_iva += costo_producto
    costo_total_despues_iva += costo_producto * (1 + IVA)

print("Costo total antes de IVA: $", costo_total_antes_iva)
print("Costo total después de IVA: $", costo_total_despues_iva)