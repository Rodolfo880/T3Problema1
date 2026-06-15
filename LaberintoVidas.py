def imprimir(mat):
    for f in mat:
        print(f)
    print()


def validar(lab, f, c, res):

    if f < 0 or f >= len(lab):
        return False

    if c < 0 or c >= len(lab[0]):
        return False

    if lab[f][c] == 0:   # pared
        return False

    if res[f][c] == 1:   # ya visitado
        return False

    return True


def aplicar_vida(valor, vida):

    if valor == -1:
        vida -= 1
    elif valor == -2:
        vida -= 2

    return vida


def laberinto(lab, res, f, c, vida, ff, cf):

    # CASO BASE: llegó a la salida (F)
    if f == ff and c == cf and vida > 0:
        res[f][c] = 1
        imprimir(res)
        return True

    if vida <= 0:
        return False

    if validar(lab, f, c, res):

        res[f][c] = 1
        imprimir(res)

        vida_actual = aplicar_vida(lab[f][c], vida)

        # abajo
        if laberinto(lab, res, f + 1, c, vida_actual, ff, cf):
            return True

        # derecha
        elif laberinto(lab, res, f, c + 1, vida_actual, ff, cf):
            return True

        # arriba
        elif laberinto(lab, res, f - 1, c, vida_actual, ff, cf):
            return True

        # izquierda
        elif laberinto(lab, res, f, c - 1, vida_actual, ff, cf):
            return True

        else:
            res[f][c] = 0
            return False

    return False