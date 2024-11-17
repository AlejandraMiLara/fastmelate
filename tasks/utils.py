import random
import pandas as pd
import os

# Rango de cada número
rangos = [
    range(1, 16),    # R1: 1-15
    range(1, 26),    # R2: 1-25
    range(1, 41),    # R3: 1-40
    range(15, 46),   # R4: 15-45
    range(30, 46),   # R5: 30-45
    range(35, 56)    # R6: 35-55
]

# Función para verificar si un número es primo
def es_primo(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

# Generación de números primos dentro de cada rango
primos_rangos = [[n for n in rango if es_primo(n)] for rango in rangos]

# Función para generar la serie de números únicos
def generar_serie():
    while True:
        serie = []
        primos_agregados = {}  # Diccionario para almacenar posición y número primo agregado

        # Elegimos cuántos números primos vamos a usar (1 a 3)
        num_primos = random.randint(1, 3)
        # Elegimos posiciones aleatorias para los números primos
        posiciones_primos = random.sample(range(6), num_primos)

        # Generamos los 6 números aleatorios respetando posiciones de primos y evitando duplicados
        for i in range(6):
            while True:
                if i in posiciones_primos:
                    # Agregamos un número primo en la posición
                    numero = random.choice(primos_rangos[i])
                else:
                    # Agregamos un número cualquiera en la posición
                    numero = random.choice(rangos[i])
                
                # Verificamos que el número no esté repetido en la serie
                if numero not in serie:
                    serie.append(numero)
                    if i in posiciones_primos:
                        primos_agregados[i] = numero  # Guardamos posición y número primo
                    break

        # Verificamos que la suma esté en el rango deseado
        if 100 <= sum(serie) <= 200:
            # Convertimos la serie a cadena para verificación
            serie_cadena = " ".join(map(str, serie))
            return serie, primos_agregados, serie_cadena

# Cargar el archivo y verificar existencia en la columna
def verificar_unicidad(serie_cadena, archivo="Melate.csv"):
    script_dir = os.path.dirname(__file__)  # Directorio actual del script
    abs_file_path = os.path.join(script_dir, archivo)
    df = pd.read_csv(abs_file_path)
    valores_existentes = df['Series'][1:].astype(str).tolist()
    return serie_cadena not in valores_existentes


# Generación de una serie única
def generar_serie_unica():
    while True:
        serie, primos_agregados, serie_cadena = generar_serie()
        if verificar_unicidad(serie_cadena):
            # Ordenar la serie sin perder el rastreo de los primos
            serie_ordenada = sorted(serie)
            primos_agregados_ordenados = {
                serie_ordenada.index(numero): numero
                for posicion, numero in primos_agregados.items()
            }
            return serie_ordenada, primos_agregados_ordenados, serie_cadena

# Ejecutamos la función y mostramos resultados
serie_valida, primos_agregados, serie_cadena = generar_serie_unica()
#print("Serie generada (ordenada):", serie_valida)
#print("Suma de la serie:", sum(serie_valida))
#print("Números primos agregados y sus posiciones:", primos_agregados)
#print("Serie en cadena única:", serie_cadena)
