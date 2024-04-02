#Pide al usuario que ingrese una palabra o frase y usa un ciclo for para contar cuántas vocales (a, e, i, o, u) contiene. Luego, muestra el conteo de cada vocal por separado.

palabra_frase = input("Ingresa una palabra o frase: ").lower()

vocales = ['a', 'e', 'i', 'o', 'u']

conteo_vocales = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}

for letra in palabra_frase:
    if letra in vocales:
        conteo_vocales[letra] += 1

for vocal, conteo in conteo_vocales.items():
    print(f"La vocal {vocal} aparece {conteo} veces.")

#Escribe un programa que lea una lista de nombres e imprima la lista en orden alfabético.

nombres = input("Ingresa una lista de nombres separados por comas: ")

lista_nombres = nombres.split(',')

lista_nombres = [nombre.strip() for nombre in lista_nombres]

lista_nombres.sort()

print("Lista de nombres en orden alfabético:")
for nombre in lista_nombres:
    print(nombre)

#Escribe un programa que lea una lista de palabras e imprima la lista de palabras que comiencen con una determinada letra.

palabras = input("Ingresa una lista de palabras separadas por comas: ")

lista_palabras = palabras.split(',')

letra = input("Ingresa una letra para filtrar las palabras que comienzan con esa letra: ")

letra = letra.lower()

palabras_con_letra = [palabra for palabra in lista_palabras if palabra.lower().startswith(letra)]

print(f"Palabras que comienzan con la letra '{letra}':")
for palabra in palabras_con_letra:
    print(palabra)

#Escribe un programa lea una lista de números e imprima la suma de los números pares

numeros = input("Ingresa una lista de números separados por comas: ")

lista_numeros = numeros.split(',')

lista_numeros = [int(numero) for numero in lista_numeros]

suma_pares = 0

for numero in lista_numeros:
    if numero % 2 == 0:
        suma_pares += numero

print("La suma de los números pares es:", suma_pares)