import random

def generar_palabra():
    return ''.join(chr(random.randint(97, 122)) for _ in range(4))

def generar_matriz(n):
    return [[generar_palabra() for _ in range(n)] for _ in range(n)]

def mostrar_matriz(matriz):
    for fila in matriz:
        print(' '.join(fila))

vocales = 'aeiou'

def tiene_vocal(palabra):
    for letra in palabra:
        if letra in vocales:
            return True
    return False

def contar_palabras_con_vocal(matriz):
    n = len(matriz)
    if n == 1 and len(matriz[0]) == 1:
        return 1 if tiene_vocal(matriz[0][0]) else 0
    mitad = n // 2
    sub1 = [fila[:mitad] for fila in matriz[:mitad]]
    sub2 = [fila[mitad:] for fila in matriz[:mitad]]
    sub3 = [fila[:mitad] for fila in matriz[mitad:]]
    sub4 = [fila[mitad:] for fila in matriz[mitad:]]
    return (contar_palabras_con_vocal(sub1) +
            contar_palabras_con_vocal(sub2) +
            contar_palabras_con_vocal(sub3) +
            contar_palabras_con_vocal(sub4))

def main():
    n = int(input("Tamaño de la matriz: "))
    matriz = generar_matriz(n)
    mostrar_matriz(matriz)
    total = contar_palabras_con_vocal(matriz)
    print(f"\nPalabras con al menos una vocal: {total}")

if __name__ == "__main__":
    main()
