#Elabore un programa que permita mostrar el sueldo promedio de un grupo de empleado
num_empleados = int(input("Ingrese el número de empleados: "))

total_sueldos = 0
for i in range(1, num_empleados + 1):
        sueldo = float(input(f"Ingrese el sueldo del empleado {i}: "))
        total_sueldos += sueldo

promedio_sueldos = total_sueldos / num_empleados
print(f"El sueldo promedio de los {num_empleados} empleados es: {promedio_sueldos}")

#Elabore un programa que muestre la potencia de 2 de un numero x mientras llegue a 1000
def potencia_de_dos_hasta_mil():
    x = 1
    while True:
        potencia_de_dos = 2 ** x
        if potencia_de_dos <= 1000:
            print(f"2^{x} = {potencia_de_dos}")
            x += 1
        else:
            break

potencia_de_dos_hasta_mil()

#Elaborar un programa que permita ingresar 10letras y luego nos indique al final cuantas vocales y consonantes se ingresaron.

def contar_vocales_y_consonantes(letras):
    vocales = 0
    consonantes = 0
    for letra in letras:
        if letra.lower() in 'aeiou':
            vocales += 1
        elif letra.isalpha():
            consonantes += 1
    return vocales, consonantes

def main():
    letras = []
    for i in range(10):
        letra = input(f"Ingrese la letra {i + 1}: ")
        letras.append(letra)

    vocales, consonantes = contar_vocales_y_consonantes(letras)
    print(f"Se ingresaron {vocales} vocales y {consonantes} consonantes.")

if __name__ == "__main__":
    main()


    # Elaborará un programa para obtener resultado del escrutinio de las elecciones de alcaldía con 3 candidatos que se postularon considerando que ha 200 electores y todos votaron el programa debe declarara al ganador por mayoría simple.

    def escrutinio_votos(votos_candidatos):
        total_votos = sum(votos_candidatos)
        porcentaje_votos = [(votos / total_votos) * 100 for votos in votos_candidatos]
        max_votos = max(votos_candidatos)
        ganador = votos_candidatos.index(max_votos) + 1
        return porcentaje_votos, ganador


    def main():
        candidatos = ['Candidato 1', 'Candidato 2', 'Candidato 3']
        votos_candidatos = []

        print("Ingrese el número de votos para cada candidato:")
        for candidato in candidatos:
            votos = int(input(f"Votos para {candidato}: "))
            votos_candidatos.append(votos)

        porcentaje_votos, ganador = escrutinio_votos(votos_candidatos)

        print("\nResultados del escrutinio:")
        for i, candidato in enumerate(candidatos):
            print(f"{candidato}: {votos_candidatos[i]} votos ({porcentaje_votos[i]:.2f}%)")

        print(
            f"\nEl ganador de las elecciones es el {candidatos[ganador - 1]} con {votos_candidatos[ganador - 1]} votos.")


    if __name__ == "__main__":
        main()

# Una ONG tiene puntos de reparto de vacunas que se pretende funcionen de la siguiente manera. Cada día, empezar con 1000 vacunas disponibles y a través de un programa que controla las entregas avisar si el inventario baja de 200 unidades. Desarrollar el algoritmo.
def reparto_vacunas():
    vacunas_disponibles = 1000
    umbral_aviso = 200

    while True:
        vacunas_disponibles -= entregar_vacunas()

        if vacunas_disponibles < umbral_aviso:
            avisar_bajo_inventario(vacunas_disponibles)

        if vacunas_disponibles <= 0:
            print("Se han agotado las vacunas. La simulación ha terminado.")
            break

def entregar_vacunas():
    cantidad_entregada = 50
    return cantidad_entregada

def avisar_bajo_inventario(vacunas_disponibles):
    print("¡Atención! El inventario de vacunas está por debajo del umbral. Vacunas disponibles:", vacunas_disponibles)

reparto_vacunas()

#Un vivero forestal actualiza cada seis meses los precios de la planta que vende en función de los valores oficiales de inflación mensual. Desean desarrollar un programa que proporcione el precio actualizado a partir del precio anterior y los valores de inflación.

def calcular_precio_actualizado(precio_anterior, inflaciones):
    # Calcular el aumento acumulado de precios
    aumento_acumulado = 0
    for inflacion in inflaciones:
        aumento_acumulado += inflacion

    # Calcular el precio actualizado
    precio_actualizado = precio_anterior * (1 + aumento_acumulado)

    return precio_actualizado


# Ejemplo de uso del programa
if __name__ == "__main__":
    precio_anterior = float(input("Ingrese el precio anterior de la planta: "))
    inflaciones = []
    meses = int(input("Ingrese el número de meses para los que tiene los valores de inflación: "))
    for i in range(meses):
        inflacion = float(input(f"Ingrese la inflación del mes {i + 1}: "))
        inflaciones.append(inflacion)

    precio_actualizado = calcular_precio_actualizado(precio_anterior, inflaciones)
    print("El precio actualizado de la planta es:", precio_actualizado)


    # Desarrolle un programa que calcule el promedio de edad hombre y mujeres_de_un_grupo_de_estudiantes.
    def pro_edad(t_personas, edades):
        if t_personas == 0:
            return 0
        suma_edades = sum(edades)
        promedio = suma_edades / t_personas
        return promedio


    def main():
        c_hom = int(input("Ingrese la cantidad de hombres en el grupo: "))
        edades_hombres = []
        for i in range(c_hom):
            edad = int(input(f"Ingrese la edad del hombre {i + 1}: "))
            edades_hombres.append(edad)

        cantidad_mujeres = int(input("Ingrese la cantidad de mujeres en el grupo: "))
        edades_mujeres = []
        for i in range(cantidad_mujeres):
            edad = int(input(f"Ingrese la edad de la mujer {i + 1}: "))
            edades_mujeres.append(edad)

        pro_hom = pro_edad(c_hom, edades_hombres)
        pro_muj = pro_edad(cantidad_mujeres, edades_mujeres)

        print(f"El promedio de edad de los hombres es: {pro_hom}")
        print(f"El promedio de edad de las mujeres es: {pro_muj}")


    if __name__ == "__main__":
        main()

#Realice un programa que permita realizar un bingo digita

import random
class Bingo:
    def __init__(self):
        self.carton = self.generar_carton()
        self.numeros_llamados = set()

    def generar_carton(self):
        return [random.randint(1, 99) for _ in range(15)]

    def llamar_numero(self):
        numero = random.randint(1, 99)
        print("El número llamado es:", numero)
        self.numeros_llamados.add(numero)

    def imprimir_carton(self):
        print("----- Cartón de Bingo -----")
        for i in range(3):
            print(self.carton[i * 5:i * 5 + 5])
        print("---------------------------")

    def marcar_numero(self, numero):
        if numero in self.carton:
            print(f"¡Has marcado el número {numero}!")
            self.carton[self.carton.index(numero)] = "X"
        else:
            print(f"El número {numero} no está en tu cartón.")

    def verificar_carton(self):
        return all(numero == "X" for numero in self.carton)


def main():
    print("¡Bienvenido al Bingo Digital!")
    juego = Bingo()

    while True:
        opcion = input("\nElige una opción:\n1. Llamar número\n2. Marcar número\n3. Ver cartón\n4. Salir\nOpción: ")

        if opcion == "1":
            juego.llamar_numero()
            if juego.verificar_carton():
                print("¡Bingo! Has completado tu cartón.")
                break
        elif opcion == "2":
            numero = int(input("Ingresa el número que deseas marcar: "))
            juego.marcar_numero(numero)
        elif opcion == "3":
            juego.imprimir_carton()
        elif opcion == "4":
            print("¡Gracias por jugar al Bingo Digital!")
            break
        else:
            print("Opción inválida. Por favor, elige una opción válida.")


if __name__ == "__main__":
    main()


#Considerando que el consumo de servicios de públicos de un establecimiento ha venido aumentando el alcalde de la ciudad requiere de un programa que le permita saber cuánto ha pagado al año y por mes le muestre cuanto paga para poder tener un control de su gasto para este concepto.

def cal_p_anual(c_mensual, p_servicio):
    pago_anual = c_mensual * p_servicio * 12
    return pago_anual

def cal_p_mensual(c_mensual, p_servicio):
    pago_mensual = c_mensual * p_servicio
    return pago_mensual

def main():
    consumo_mensual = float(input("Ingrese el consumo mensual de servicios públicos: "))
    precio_servicio = float(input("Ingrese el precio del servicio por unidad: "))

    pago_anual = cal_p_anual(consumo_mensual, precio_servicio)
    pago_mensual = cal_p_mensual(consumo_mensual, precio_servicio)

    print(f"El establecimiento paga {pago_anual} al año por servicios públicos.")
    print(f"El establecimiento paga {pago_mensual} por mes por servicios públicos.")

if __name__ == "__main__":
    main()


    # Desarrolle un programa que permita saber el salario de 20 empleados por mes se requiere el promedio de estos y el pago de cado uno de igual manera cuanto ganaran si se hace un incremento del 2.5%

    def c_s_mensual(salarios):  # recolecta los datos
        ttl_sal = sum(salarios)
        promedio_salarios = ttl_sal / len(salarios)
        return promedio_salarios


    def incr_sal(salarios, incr_porcentaje):  # incrementa el porcentaje
        salarios_incrementados = [salario * (1 + incr_porcentaje / 100) for salario in salarios]
        return salarios_incrementados


    def main():
        sal_empleados = []  # recolecto salario de empleados

        for i in range(5):  # se defina la cant de datos ingresados
            salario = float(input(f"Ingrese el salario del empleado {i + 1}: "))
            sal_empleados.append(salario)  #

        pro_salarios = c_s_mensual(sal_empleados)

        # Calcular los salarios incrementados en un 2.5%
        salarios_incrementados = incr_sal(sal_empleados, 2.5)

        print(f"El promedio de los salarios mensuales es: {pro_salarios}")

        print("\nSalarios incrementados en un 2.5%:")
        for i, salario in enumerate(salarios_incrementados):
            print(f"Empleado {i + 1}: {salario}")


    if __name__ == "__main__":
        main()

