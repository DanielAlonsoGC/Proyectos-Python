from random import *
palabras = ['granadilla', 'cocodrilo', 'murcielago','palindromo']
letras_correctas = []
letras_incorrectas = []
intento = 6
aciertos = 0
juego_terminado = False

# eleccion de una palabra y cantidad de letras unicas
def eleccion_palabra(lista_palabras):
    palabra_elegida = choice(lista_palabras)
    letras_unicas = len(set(palabra_elegida))
    return palabra_elegida, letras_unicas
#eleccion de una letra
def pedir_letra():
    letra_elegida = ''
    es_valida = False
    sopa_letras = 'abcdefghijklmnsopqrstuvwxyz'
    while not es_valida :
        letra_elegida = input("Elige una letra: ")
        if letra_elegida in sopa_letras and len(letra_elegida) == 1:
            es_valida = True
        else:
            "No haz elegido la letra correcta"
    return letra_elegida
def mostrar_tablero(palabra_elegida):
    lista_oculta=[]
    for l in palabra_elegida:
        # al comienzo no entra en el if sino solo al else
        if l in letras_correctas:
            lista_oculta.append(l)
        else:
            lista_oculta.append('-')
    print(' '.join(lista_oculta))


def chequear_letra(letra_elegida,palabra_oculta, vidas, coincidencias):
    fin = False
    # verfica si la letra ingresada esta en la palabra seleccionada al azar
    if letra_elegida in palabra_oculta:
        letras_correctas.append(letra_elegida)
        coincidencias += 1
    else:
        letras_incorrectas.append(letra_elegida)
        vidas = vidas -1

    if vidas == 0:
        fin = perder()
    elif coincidencias == letras_unicas:
        fin = ganar(palabra_oculta)
    return vidas, fin, coincidencias

def perder():
    print('Te haz quedado sin vidas')
    print("la palabra oculta era "+ palabra)
    return True
def ganar(palabra_descubierta):
    mostrar_tablero(palabra_descubierta)
    print("Felicitaciones, haz encontrado la palabra: ")
    return True

# creacion del programa
palabra, letras_unicas =eleccion_palabra(palabras)
while not juego_terminado:
    print("\n" + '*' * 20 + '\n')
    mostrar_tablero(palabra)
    print('\n')
    print('Letras incorrectas: ' + '-'.join(letras_incorrectas))
    print(f'Vidas: {intento}')
    print('\n'+ '*' * 20 + '\n')
    letra = pedir_letra()
    # funcion chequear
    intento, terminado, aciertos = chequear_letra(letra, palabra, intento, aciertos)
    juego_terminado = terminado

