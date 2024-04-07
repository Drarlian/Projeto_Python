import requests
from bs4 import BeautifulSoup
from selenium import webdriver


def pegando_dolar_by_request():
    # URL da página que você deseja extrair o título:
    url = 'https://dolarhoje.com'

    # Faz a requisição GET para a página:
    response = requests.get(url)

    # Cria um objeto BeautifulSoup com o conteúdo da página:
    soup = BeautifulSoup(response.text, 'html.parser')

    # Pega o conteúdo especifico da página:
    texto = soup.find_all('span', attrs={'class': 'cotMoeda nacional'})

    # Exibe o conteudo da página:
    # print(texto)

    parte1 = parte2 = False
    for elemento in texto:
        parte1 = elemento.find('span').text
        parte2 = elemento.find('input').get('value')

    if parte1 and parte2:
        valor_dolar = f'O valor do Dolár Hoje é igual a: {parte1}{parte2}'
        print(valor_dolar)


def pegando_dolar_by_selenium():
    url = 'https://www.google.com/search?client=opera-gx&q=dolar+hoje&sourceid=opera&ie=UTF-8&oe=UTF-8'
    chrome_configs = webdriver.ChromeOptions()
    # chrome_configs.add_argument("--headless")

    navegador = webdriver.Chrome(options=chrome_configs)
    navegador.get(url)

    navegador.implicitly_wait(5)

    # Abrir o link e pegar dados:
    navegador.get(url)

    soup = BeautifulSoup(navegador.page_source, 'html.parser')
    # print(soup)

    elementos_valores = soup.find_all('div', attrs={'class': 'dDoNo ikb4Bb gsrt GDBPqd'})
    print(elementos_valores)

    lista_temporaria = []
    for elemento in elementos_valores:
        for span in elemento.find_all('span'):
            lista_temporaria.append(span.text)

    print(f'O valor do Dolár Hoje é igual a: {lista_temporaria[0]} {lista_temporaria[1]}')


# pegando_dolar_by_request()
# pegando_dolar_by_selenium()
