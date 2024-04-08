import csv

data = [['Nome', 'Idade'], ['Renato', 22], ['Claudio', 33], ['Roberto', 60]]


def ler_arquivo():
    with open('arquivo.csv', 'r') as arquivo:
        leitor = csv.reader(arquivo, delimiter='&')

        for linha in leitor:
            print(linha)


def escrever_arquivo():
    with open('arquivo.csv', 'w', newline='') as arquivo:
        escritor = csv.writer(arquivo, delimiter='&')

        escritor.writerows(data)


# ler_arquivo()
# escrever_arquivo()
