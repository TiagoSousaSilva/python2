def getletra(nota):
    letra = 'A'
    if nota >= 80:
        letra = 'A'
    if nota >= 60:
        letra = 'B'
    if nota >= 40:
        letra = 'C'
    if nota >= 20:
        letra = 'D'
    if nota >= 0:
        letra = 'E'
    return letra

nota = int(input('Qual num: '))

print(f'a tua nota é {getletra(nota)}' )

##n esta completo


