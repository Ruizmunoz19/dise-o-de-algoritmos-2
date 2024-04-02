#Crear un programa que pida al usuario una contraseña, de forma repetitiva mientras que no introduzca "1234". Cuando finalmente escriba la contraseña correcta, se le dirá "Bienvenido" y terminará el programa.

contraseña_correcta = "1234"

while True:
    contraseña = input("Por favor, introduce tu contraseña: ")

    if contraseña == contraseña_correcta:
        print("Bienvenido")
        break
    else:
        print("Contraseña incorrecta. Intenta de nuevo.")

        # Crea un programa que genere dos números al azar entre el 0 y el 100, y pida al usuario que calcule e introduzca su suma. Si la respuesta no es correcta, deberá volver a pedirla tantas veces como sea necesario hasta que el usuario acierte. Pista: como verás en el apartado 10, para generar un número al azar del 0 al 100 puedes hacer número <- RANDOM (101).

        import random


        def generar_numeros():
            num1 = random.randint(0, 100)
            num2 = random.randint(0, 100)
            return num1, num2


        def main():
            print("Bienvenido al juego de suma de dos números aleatorios entre 0 y 100.")
            num1, num2 = generar_numeros()
            suma_correcta = num1 + num2
            while True:
                respuesta = int(input(f"¿Cuánto es {num1} + {num2}? "))
                if respuesta == suma_correcta:
                    print("¡Correcto! La suma es", suma_correcta)
                    break
                else:
                    print("Respuesta incorrecta. Intenta de nuevo.")


        if __name__ == "__main__":
            main()