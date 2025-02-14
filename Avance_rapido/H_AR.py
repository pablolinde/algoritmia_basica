"""
El Problema:
Hay que escribir un programa que seleccione el orden de ejecución de las tareas aptas o candidatas a ser ejecutadas así
como la máquina en la que deberán ejecutarse, minimizando el tiempo acumulado de ejecución de las máquinas. Se
conoce de antemano el tiempo de ejecución de cada tarea n en cada máquina m.
En concreto, el objetivo a minimizar es el tiempo en el que acaba de ejecutarse la última tarea en el procesador que acaba
más tarde (lo que se conoce como el tiempo de procesamiento acumulado). Se admitirá cualquier solución cuyo tiempo de 
procesamiento acumulado sea, como máximo, el triple que la solución básica
ideada por el profesor.

Entrada:
La primera línea de la entrada contiene un entero, P, que indica el número de casos de prueba.
Cada caso de prueba contendrá una primera línea con dos enteros,N y M, que indican el número de tareas a ejecutar y el
número de máquinas disponibles, respectivamente. Como máximo, N y M valdrán 100.
A continuación aparecerán N líneas (una por tarea), cada línea contieneM enteros separados por espacios en blanco que
corresponden al tiempo de ejecución de la tarea en cada una de las máquinas disponibles.
Las tareas y las máquinas se numerarán empezando por 1.

Salida:
Para cada caso de prueba, la salida deberá tener tres líneas. La primera línea es el tiempo de procesamiento acumulado
para la máquina con mayor carga, es decir, el tiempo en el que acaba de ejecutarse la última tarea en la última máquina.
La segunda línea debe indicar el orden de selección de las tareas. Esta línea contendráN números enteros, separados por
espacios en blanco. Cada número i-ésimo indica la tarea que se ejecuta eni-ésima posición. La tercera línea contendrá
también N números enteros, e indica en qué máquina se ejecuta la tarea seleccionada eni-ésima posición.

Ejemplo de Entrada:
2
5 2
13 25
7 16
22 19
13 14
14 23
7 5
21 22 24 25 9
7 26 22 7 2
21 13 22 17 20
10 19 1 6 12
4 6 10 9 17
13 11 3 19 22
17 13 19 16 13

Ejemplo de Salida:
34
2 4 1 3 5
1 2 1 2 1
16
4 2 5 6 1 3 7
3 5 1 3 5 2 4
"""

import numpy as np

def planificar_tareas(archivo_entrada, archivo_salida):

    with open(archivo_entrada, 'r') as file_in, open(archivo_salida, 'w') as file_out:

        P = int(file_in.readline())

        for i in range(P):
            N, M = map(int, file_in.readline().split())
            t = [list(map(int, file_in.readline().split())) for i in range(N)]
            tiempos = np.array(t)

            tiempo_acumulado, orden_tareas, maquinas_ejecucion = planificacion(N, M, tiempos)

            # Escribir los resultados en el archivo de salida
            file_out.write(f"{tiempo_acumulado}\n")
            file_out.write(" ".join(map(str, orden_tareas)) + "\n")
            file_out.write(" ".join(map(str, maquinas_ejecucion)) + "\n")


def planificacion(N, M, tiempos):

    orden_tareas = []
    maquinas_ejecucion = []
    tiempo_acumulado = {j: 0 for j in range(M)}

    for i in range(N):
        beneficios = []
        for i in range(N):
            tiempo_acumulado_mejor_maquina_j = sum(tiempo_acumulado[j] for j in range(M))
            beneficio_tarea_i_mejor_maquina_j = - tiempo_acumulado_mejor_maquina_j - tiempos[i, :].min()
            beneficios.append(beneficio_tarea_i_mejor_maquina_j)

        tarea_optima = beneficios.index(max(beneficios))
        maquina_optima = np.argmin(tiempos[tarea_optima, :])

        orden_tareas.append(tarea_optima + 1)
        maquinas_ejecucion.append(maquina_optima + 1)
        tiempo_acumulado[maquina_optima] += tiempos[tarea_optima, maquina_optima]
        tiempos[tarea_optima, :] = 10**9  

    tiempo_maximo = max(tiempo_acumulado.values())

    return tiempo_maximo, orden_tareas, maquinas_ejecucion


if __name__ == "__main__":
    planificar_tareas('./tests/T2/703b.in', './tests/T2/test1703b.out')