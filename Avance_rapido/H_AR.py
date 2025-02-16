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
