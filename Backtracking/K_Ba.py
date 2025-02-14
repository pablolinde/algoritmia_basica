"""
El Problema:
Los alumnos de informática van a organizar una competición de "tirar de la cuerda". Para jugar a este juego los participantes
deben ser divididos en dos equipos. Cada persona puede estar en uno u otro equipo. El número de personas en los dos
equipos no puede diferir en más de 1. El peso total de los miembros de cada equipo debería ser tan parecido como sea
posible.

Entrada:
La entrada comienza con una línea con un único entero positivo que indica el número de casos de prueba que vienen a
continuación. Después viene una línea en blanco, y también habrá una línea en blanco entre cada dos casos de prueba
consecutivos. La primera línea de cada caso contiene n, el número de participantes en el juego. A continuación vienen n líneas. La primera
línea indica el peso de la persona 1, la segunda el peso de la persona 2, y así sucesivamente. Cada peso es un entero entre 1 y
450. Habrá como máximo 30 participantes en el juego.

Salida:
Para cada caso de prueba, la salida debe seguir la siguiente descripción.
La salida será una única línea con 2 números: el peso total de los miembros de un equipo y el peso de los miembros del otro
equipo. Si estos números son distintos, indicar el menor primero.

Ejemplo de Entrada:
1
3
100
90
200

Ejemplo de Salida:
190 200
"""

def balancear_pesos(archivo_entrada, archivo_salida):

    with open(archivo_entrada, 'r') as file_in, open(archivo_salida, 'w') as file_out:
        P = int(file_in.readline().strip())

        for _ in range(P):
            file_in.readline()  
            participantes = int(file_in.readline().strip())
            pesos = [int(file_in.readline().strip()) for _ in range(participantes)]
            pesos.sort(reverse=True)

            memo = {}
            best_diff, team1 = balance(pesos, 0, 0, 0, memo)

            file_out.write(f"{min(team1, sum(pesos) - team1)} {max(team1, sum(pesos) - team1)}\n")


def balance(pesos, iteracion, total1, total2, memo):

    if iteracion == len(pesos):
        return abs(total1 - total2), total1

    if (iteracion, total1) in memo:
        return memo[(iteracion, total1)]

    diff1, team1 = balance(pesos, iteracion + 1, total1 + pesos[iteracion], total2, memo)
    diff2, team2 = balance(pesos, iteracion + 1, total1, total2 + pesos[iteracion], memo)

    if diff1 < diff2:
        result = diff1, team1
    else:
        result = diff2, team2

    memo[(iteracion, total1)] = result

    return result


if __name__ == "__main__":
    balancear_pesos('./tests/T1/906a.in', './tests/T1/a.out')