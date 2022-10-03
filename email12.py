"""
Escreva um programa em Python que calcula o valor da soma.

1 + x + x2/2! + x3/3! + ... + xn/n!

para um dado valor de x e de n. O seu programa deve ter em atenção
que o i-ésimo termo da soma pode ser obtido do termo na posição i
1,
multiplicando-o por x/i. O seu programa deve permitir a interação:
"""


def calculo(x, n):
    total = 1 + x + (x^n/n)