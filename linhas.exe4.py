"""
pede ao utilizador:
 - BI
 - NOME
 - MORADA
 - CODIGO POSTAL
 - PREÇO CUSTO/HORA  xx.xx
 - ANO NASCIMENTO xxxx
 lista = {
    "BI": '',
    "NOME": '',
    "MORADA": '',
    "CODIGO POSTAL": '',
    "PREÇO USTO/HORAS": 0.0,
    "ANO NASCIMENTO": 0,
}
"""


informacoes = {}

max_length = 1

while len(informacoes) < max_length:
    NºBI = "BI"
    BI = int(input('BI: '))
    informacoes[NºBI] = BI ##Ou ( informacoes['BI'] = BI )

    n_nome = 'nome'
    nome = input('nome: ')
    informacoes[n_nome] = nome

    m_morada = 'morada'
    morada = input('Morada: ')
    informacoes[m_morada] = morada

    n_codigo_postal = 'Codigo Postal'
    codigo_postal=int(input('Codigo Postal: '))
    informacoes[n_codigo_postal] = codigo_postal

    n_preco_custohora = 'Preço Custo/Hora'
    preco_custohora = float(input('Preço Custo/Hora: '))
    informacoes[n_preco_custohora] = preco_custohora

    n_ano_nascimento = 'Ano de nascimento'
    ano_nascimento = int(input('Ano de nascimento: '))
    informacoes[n_ano_nascimento] = ano_nascimento

print(informacoes)