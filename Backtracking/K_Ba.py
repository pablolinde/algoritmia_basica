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
