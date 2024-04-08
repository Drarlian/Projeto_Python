import csv

data = [['Nome', 'Idade'], ['Renato', 22], ['Claudio', 33], ['Roberto', 60]]


def ler_arquivo():
    # Abrindo um arquivo CSV em Modo de Leitura, o 'r' representa read.
    with open('arquivo.csv', 'r') as arquivo:  # Criando um apelido para o arquivo, chamando ele de arquivo.
        leitor = csv.reader(arquivo, delimiter='&')  # Criando um objeto de leitura e informando o separador do arquivo CSV.

        for linha in leitor:  # Para cada linha dentro do meu arquivo, vou imprimir a linha.
            print(linha)


def escrever_arquivo():
    # Abrindo um arquivo CSV em Modo de Escrita, o 'w' representa write.
    with open('arquivo.csv', 'w', newline='') as arquivo:  # Criando um apelido para o arquivo, chamando ele de arquivo.
        escritor = csv.writer(arquivo, delimiter='&')  # Criando um objeto de escrita e informando o separador do arquivo CSV.

        escritor.writerows(data)  # Escreve todos os elementos da lista 'data' dentro do arquivo.


# O codigo abaixo está comentando, para executar o codigo de fato, descomente a funcionaldiade desejada.
# ler_arquivo()  # -> Executo a leitura do arquivo.
# escrever_arquivo()  # -> Executo a escrita do arquivo.
