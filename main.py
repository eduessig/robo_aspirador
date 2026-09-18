import numpy as np
import matplotlib.pyplot as plt
import random

from matplotlib.colors import ListedColormap

matriz = np.zeros((6, 6), dtype=int)

matriz[0, :] = 1
matriz[-1, :] = 1
matriz[:, 0] = 1
matriz[:, -1] = 1

qtde_vezes = random.randint(3, 7)

posicao_coluna = random.randint(1, 4)
posicao_linha = random.randint(1, 4)

for i in range(qtde_vezes):
    linha = random.randint(1, 4)
    coluna = random.randint(1, 4)

    matriz[linha, coluna] = 2

cores = ListedColormap([
    "white",
    "orange",
    "black"
])

plt.imshow(matriz, cmap=cores)

plt.xticks(np.arange(-0.5, 6, 1), [])
plt.yticks(np.arange(-0.5, 6, 1), [])

plt.grid(color="black", linewidth=2)

plt.plot(
    posicao_coluna,
    posicao_linha,
    marker="o",
    markersize=30,
    color="red"
)

plt.show()


def descer():
    global posicao_linha
    posicao_linha += 1


def subir():
    global posicao_linha
    posicao_linha -= 1


def moverDireita():
    global posicao_coluna
    posicao_coluna += 1


def moverEsquerda():
    global posicao_coluna
    posicao_coluna -= 1


def aspirar():
    matriz[posicao_linha, posicao_coluna] = 0


def funcaoMapear():
    posicao = matriz[posicao_linha, posicao_coluna]

    if posicao == 2:
        sujeira = True
    else:
        sujeira = False

    return sujeira


def movimentarAgente():
    if posicao_linha % 2 == 1:
        if posicao_coluna == 4:
            descer()
        else:
            moverDireita()
    else:
        if posicao_coluna == 1:
            descer()
        else:
            moverEsquerda()


def agenteReativoSimples(percepcao):
    sujeira = percepcao

    if sujeira:
        aspirar()
    else:
        movimentarAgente()