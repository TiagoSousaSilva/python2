"""
Substituir palavras num texto
"""
def string_lista(frase):
        frase_lista = frase.split()
        return frase_lista

if __name__ == '__main__':
        frase = input('Escreva uma frase: ')
        palavra_mudar = input('Qual a palavra que quer mudar: ')

        print(string_lista(frase))