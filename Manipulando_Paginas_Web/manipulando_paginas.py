from selenium import webdriver

continuar = True
while continuar:
    url = ''
    # chrome_configs = webdriver.ChromeOptions()
    # chrome_configs.add_argument("--headless")

    # navegador = webdriver.Chrome(options=chrome_configs)
    navegador = webdriver.Chrome()
    navegador.get(url)

    # navegador.implicitly_wait(5)

    # Abrir o link e pegar dados:
    navegador.get(url)

    # Dados
    login = ''
    senha = ''

    # Encontrando os campos de texto:
    navegador.find_element('xpath', '//*[@id="root"]/div[2]/div[2]/div/form/div[1]/input').send_keys(login)

    navegador.find_element('xpath', '//*[@id="root"]/div[2]/div[2]/div/form/div[2]/input').send_keys(senha)

    # Clicando no Botão:
    navegador.find_element('xpath', '//*[@id="signin"]').click()

    validacao = str(input('Deseja continuar? [S/N] ')).upper()

    if validacao == 'N':
        break
    else:
        continue
