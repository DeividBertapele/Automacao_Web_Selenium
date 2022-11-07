# Automação Web com Selenium 

#  - 2 importantes:
#     - Instalar Selenium  ===> pip install selenium
#     - Webdriver Manager  ===> pip install webdriver-manager

#     Link:
#       - https://pypi.org/project/webdriver-manager/
#       - https://selenium-python.readthedocs.io/getting-started.html


# Importar as bibliotecas e intalar o ChromeDrivermanager
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv = Service(ChromeDriverManager().install())

nav = webdriver.Chrome(service=serv)


#### FAZER O TESTE NO RECLAME AQUI ####


# Primeiro Passo:
    
nav.get('https://www.reclameaqui.com.br/')

# Segundo Passo:
nav.find_element(By.ID, "btn-signin").click()  # para clicar Fazer Login

# Terceiro Passo:
nav.find_element(By.NAME, "username").send_keys('Teste') # colocar nome do usuário

# Quarto Passo:
nav.find_element(By.ID, "password").send_keys('12345') # colocar nome do usuário

# Quinto Passo:
nav.find_element(By.ID, "kc-login").click() # colocar nome do usuário


print('Automação finalizado.')