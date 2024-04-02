def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def producto(a, b):
    return a * b

def division(a, b):
    if b == 0:
        return "Error: división por cero"
    else:
        return a / b

def calcular_precio_total(cantidad, precio_unitario, forma_pago):
    precio_sin_iva = cantidad * precio_unitario
    if forma_pago.lower() == "contado":
        descuento = precio_sin_iva * 0.05
        precio_con_descuento = precio_sin_iva - descuento
        precio_final = precio_con_descuento * 1.16
    else:
        precio_final = precio_sin_iva * 1.16
    return precio_final

def main():
    import sys

    if len(sys.argv) != 4:
        print("Uso: python calculadora.py [operacion] [valor1] [valor2]")
        sys.exit(1)

    operacion = sys.argv[1]
    valor1 = int(sys.argv[2])
    valor2 = int(sys.argv[3])

    if operacion.lower() == "s":
        resultado = suma(valor1, valor2)
    elif operacion.lower() == "r":
        resultado = resta(valor1, valor2)
    elif operacion.lower() == "p":
        resultado = producto(valor1, valor2)
    elif operacion.lower() == "d":
        resultado = division(valor1, valor2)
    else:
        print("Operación no reconocida.")
        sys.exit(1)

    print("El resultado de la operación es:", resultado)

    cantidad_impresoras = int(input("Ingrese la cantidad de impresoras a comprar: "))
    forma_pago = input("Ingrese la forma de pago (contado o crédito): ")
    precio_unitario_impresora = 80000
    precio_total = calcular_precio_total(cantidad_impresoras, precio_unitario_impresora, forma_pago)
    print(f"El precio total a pagar es: ${precio_total:.2f}")


if __name__ == "_main_":
    main()