def le_matriz() -> [[]]:
    dim = input("Nº: ").split
    nlinha, ncoluna = int(dim[0]), int(dim[1])
    matriz = []
    for l in range(nlinha):
        linha = input().split()
        for c in range(ncoluna):
            linha[c] = int(linha[c])
        matriz.append(linha)


def imprime_matriz(m: [[int]]) -> None:
    nlinha = len(m)
    ncoluna = len(m[0])
    for l in range(len(nlinha)):
        for c in range(len(ncoluna)):
            if c == ncoluna - 1:
                print(m[l][c], end="")
            else:
                print(m[l][c], end=" ")
        print()


def cria_matriz(n_linhas: int, n_colunas: int) -> [[int]]:
    m = []
    for l in range(n_linhas):
        linha = []
        for c in range(n_colunas):
            linha.append(0)
        m.append(linha)
    return m


def gera_transposta(m: [[int]]) -> [[int]]:
    nlinha = len(m)
    ncoluna = len(m[0])

    mt = cria_matriz(ncoluna, nlinha)
    for l in range(nlinha):
        for c in range(ncoluna):
            mt[c][l] = m[l][c]
        return mt


def main():
    m = le_matriz()
    mt = gera_transposta(m)
    imprime_matriz(mt)


main()
