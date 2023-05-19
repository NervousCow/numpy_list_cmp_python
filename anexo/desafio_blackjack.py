# Numpy [Python]
# Ejercicios de profundización

# Autor: Inove Coding School
# Version: 2.0

# NOTA: 
# Estos ejercicios son de mayor dificultad que los de clase y práctica.
# Están pensados para aquellos con conocimientos previo o que dispongan
# de mucho más tiempo para abordar estos temas por su cuenta.
# Requiere mayor tiempo de dedicación e investigación autodidacta.

# IMPORTANTE: NO borrar los comentarios en VERDE o NARANJA

'''
Enunciado:
Black jack! [o algo parecido :)]

El objetivo es realizar una aproximación al juego de black jack,
el objetivo es generar una lista de 2 números aleatorios
entre 1 al 10 inclusive, y mostrar los "números" al usuario.

El usuario debe indicar al sistema si desea sacar más
números para sumarlo a la lista o no sacar más

A medida que el usuario vaya sacando números aleatorios que se suman
a su lista se debe ir mostrando en pantalla la suma total
de los números hasta el momento.

Cuando el usuario no desee sacar más números o cuando el usuario
haya superado los 21 (como la suma de todos) se termina la jugada
y se presenta el resultado en pantalla

BONUS Track: Realizar las modificaciones necesarias para que jueguen
dos jugadores y compitan para ver quien sacá la suma de números
más cercanos a 21 sin pasarse!
'''

import random
import numpy as np



def cartas():
    cartas = []
    while len(cartas) < 2:
        carta = random.randint(1,10)
        if carta == 1:
            carta_as = int(input('Salio un As. Qué valor le das? 11 o 1?'))
            if carta_as == 11:
                carta_as = 11
                cartas.append(carta_as)
            elif carta_as == 1:
                carta_as = 1
                cartas.append(carta_as)
            else:
                print('Bueno como NO pusiste 11 o 1 decido yo al azar!')
                carta_as = random.choice([1,11])
                cartas.append(carta_as)
        else:
            cartas.append(carta)

    return cartas

def mas_cartas():
    nueva_carta = random.randint(1,10)
    if nueva_carta == 1:
            carta_as = int(input('Salio un As. Qué valor le das? 11 o 1?'))
            if carta_as == 11:
                nueva_carta = 11
            elif carta_as == 1:
                nueva_carta = 1
            else:
                print('Bueno como NO pusiste 11 o 1 decido yo al azar!')
                nueva_carta = random.choice([1,11])
    
    return nueva_carta

def juego(nombre):
    print()
    print('Bueno,', nombre, 'arrancamos.')
    cartas_inicio = cartas()
    suma_cartas = sum(cartas_inicio)
    print('Tus cartas son,', cartas_inicio, 'y suman', suma_cartas)
    print()
    while suma_cartas <= 21:
        sigue = input('Queres otra carta? S / N: ').upper()
        if sigue == 'S':
            nueva_carta = mas_cartas()
            suma_cartas += nueva_carta
            if suma_cartas == 21:
                cartas_inicio.append(nueva_carta)
                print(nombre, 'tus cartas son', cartas_inicio, 'y suman', suma_cartas, 'nos plantamos acá campeón!')
                no_va_mas = {'nombre': nombre, 'puntos': suma_cartas}
                break
            elif suma_cartas < 21:
                cartas_inicio.append(nueva_carta)
                print('Tus cartas son,', cartas_inicio, 'y suman', suma_cartas)
                continue
            elif suma_cartas > 21:
                cartas_inicio.append(nueva_carta)
                print(f'{nombre}, te re pasaste...', cartas_inicio)
                no_va_mas = {'nombre': nombre, 'puntos': 0}
                break
        elif sigue == 'N':
                print(f'El jugador {nombre}, se planta con {suma_cartas}')
                no_va_mas = {'nombre': nombre, 'puntos': suma_cartas}
                break
        else:
            print('Ingresa "S" o "N"')
            continue
    
    return no_va_mas
    



if __name__ == '__main__':
    print("Ahora sí! buena suerte :)")
    # A partir de aquí escriba el código que resuelve el enunciado
    # Leer el enunciado con atención y consultar cualquier duda


    print('Bienvenidos! juguemos un poco al \033[1;32m$Black Jack$\033[1;0m')
    print()
    cantidad_jugadores = int(input('Cuantos jugadores son?? '))
    jugadores = []
    print('A continuación te voy pedir que ingreses un nombre o alias para cada jugador')
    
    for i in range(cantidad_jugadores):
        print()
        nombre_alias = input('Ingresa un nombre o alias: ')
        jugadores.append(nombre_alias)
    print('Perfecto, ya tenemos a los jugadores!')

    resultado_jugadores = [juego(jugadores[x]) for x in range(len(jugadores))]

    # NO ENTINEDO BIEN el motivo por el que tengo que definir una funcion en el
    # key del sort. No entiedo por que no puedo escribir simplemente 'puntos'. Si
    # ya estoy indicando que lo que quiero ordenar es una lista de diccionarios!
    resultado_jugadores.sort(key=lambda x: x['puntos'], reverse=True)

    print('*' * 40, end='')
    print()
    print('\033[1;36mRANKING\033[1;0m')
    print()
    [print('Jugador:', x.get('nombre'), 'con', x.get('puntos'), 'puntos') for x in resultado_jugadores]
    print()
    print('*' * 40, end='')

    print()
    
    if cantidad_jugadores > 1:
        if resultado_jugadores[0]['puntos'] == 0:
            print('\033[1;36mTODOS PERDIERON!\033[1;0m')
        elif resultado_jugadores[0]['puntos'] == resultado_jugadores[1]['puntos']:
            print('\033[1;36mHAY EMPATE, LA CASA SE LLEVA TODO\033[1;0m')
        else:
            ganador = resultado_jugadores[0]['nombre']
            print(f'\033[1;36m{ganador} ES EL GANADOR\033[1;0m')
    


    print("terminamos")