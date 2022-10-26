# para rodar o chrome em 2º plano
# from selenium.webdriver.chrome.options import Options
# chrome_options = Options()
# chrome_options.headless = True 
# navegador = webdriver.Chrome(options=chrome_options)

#tabela = pd.read_excel('D:\Documentos_\Simples Nacional\Codigo de Acesso SN\_Codigo_De_Acesso.xlsx')
#pd.display(tabela)
#Empresa = 21

#tabela.query('Numero == 21')

# Passo 5: Recalcular o preço de cada produto
# atualizar a cotação
# nas linhas onde na coluna "Moeda" = Dólar
# tabela.loc[tabela["Moeda"] == "Dólar", "Cotação"] = float(cotacao_dolar)
# tabela.loc[tabela["Moeda"] == "Euro", "Cotação"] = float(cotacao_euro)
# tabela.loc[tabela["Moeda"] == "Ouro", "Cotação"] = float(cotacao_ouro)

# atualizar o preço base reais (preço base original * cotação)
# tabela["Preço de Compra"] = tabela["Preço Original"] * tabela["Cotação"]

# atualizar o preço final (preço base reais * Margem)
# tabela["Preço de Venda"] = tabela["Preço de Compra"] * tabela["Margem"]

# tabela["Preço de Venda"] = tabela["Preço de Venda"].map("R${:.2f}".format)

# display(tabela)

# Fórmula similar a procv do Excel para encontrar o CNPJ, CPF e Código de acesso da empresa indicada na variável Empresa.
# Salvar as informações nas variáveis CNPJ, CPF e Código
# Tem que formatar as váriaveis CNPJ, CPF e Código para poder receber "0" a esquerda.


#pip install openpyxl

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

import pyautogui
import pyperclip
import time
import pandas as pd

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_argument('—headless')
options.add_argument("disable-infobars")
options.add_argument("--disable-extensions")

simplesNacional = pd.read_excel(r'C:\Users\DaviF\Desktop\Codigo_De_Acesso.xlsx')

pd.set_option('display.max_rows', simplesNacional.shape[0]+1)

indexes = len(simplesNacional)

# indexes = len(indexes)
# print(indexes)

#indexeK = int(indexes)






indexF = 0

print(simplesNacional)

emp = int(input("Número da Empresa: "))

if emp:
    selecionado=simplesNacional[simplesNacional["Numero"]==emp]

    numeroEmpresa = indexes - 1

    numeroSelecionado = int(simplesNacional.iat[indexF,0])

    selecaoNumeroEmpresa = str(selecionado.iat[0,0])

    selecaoRazaoSocial = str(selecionado.iat[0,1])

    selecaoCNPJ = str(selecionado.iat[0,2])

    selecaoCPF = str(selecionado.iat[0,3])

    selecaoCodigo = str(selecionado.iat[0,4])

    print("Número da Empresa: " + selecaoNumeroEmpresa)
    print("Razão Social: " + selecaoRazaoSocial)
    print("CNPJ: " + '{:0>14}'.format(selecaoCNPJ))
    print("CPF: " + '{:0>11}'.format(selecaoCPF))
    print("Código de Acesso: " + '{:0>12}'.format(selecaoCodigo))
else:
    print("Entrada Inválida")
    exit()







print("")

#print(simplesNacional.iloc[[0]])

#selecao = 0

#while selecao == 0:
#    selecao = simplesNacional.iat[0,0]

#respota = 2
#simplesNacional.iat[0,0]



headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 \(KHTML, like Gecko) Chrome / 86.0.4240.198Safari / 537.36"}

# abrir um navegador
#navegador = webdriver.Chrome()
# caso queira deixar na mesma pasta do seu código
# navegador = webdriver.Chrome("chromedriver.exe")

class Simples:
    def __init__(self):
        self.SITE_LINK = "https://www8.receita.fazenda.gov.br/SimplesNacional/controleAcesso/Autentica.aspx?id=60"
        self.SITE_MAP = {
            "buttons":{
                "cnpj":{
                    "xpath":"/html/body/form/div[3]/div[2]/div[2]/div[1]/div/div[1]/ul/li[1]/input"
                },
                "cpf":{
                    "xpath":"/html/body/form/div[3]/div[2]/div[2]/div[1]/div/div[1]/ul/li[2]/input"
                },
                "codigo":{
                    "xpath":"/html/body/form/div[3]/div[2]/div[2]/div[1]/div/div[1]/ul/li[3]/input"
                },
                "captcha":{
                    "xpath":"/html/body/form/div[3]/div[2]/div[2]/div[1]/div/div[2]/input"
                }
            }
        }
        
        self.driver = webdriver.Chrome(options=options,service=Service(ChromeDriverManager().install()))
        #self.driver = webdriver.Chrome(executable_path="C:\\WebDrivers\\chromedriver.exe")


    def abrir_site(self):
        self.driver.get(self.SITE_LINK)
        self.driver.maximize_window()
        time.sleep(0.5)

    def logar(self):
    
        cnpj = selecaoCNPJ
        cpf = selecaoCPF
        codg = selecaoCodigo

        self.driver.find_element('xpath',self.SITE_MAP["buttons"]["cnpj"]["xpath"]).send_keys('{:0>14}'.format(cnpj))

        self.driver.find_element('xpath',self.SITE_MAP["buttons"]["cpf"]["xpath"]).send_keys('{:0>11}'.format(cpf))

        self.driver.find_element('xpath',self.SITE_MAP["buttons"]["codigo"]["xpath"]).send_keys('{:0>12}'.format(codg))

        
    def captcha(self):

        self.driver.find_element('xpath',self.SITE_MAP["buttons"]["captcha"]["xpath"]).click()
    
simples = Simples()

simples.abrir_site()

simples.logar()

simples.captcha()


# cotacao_dolar = navegador.find_element(By.XPATH,
#    '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute("data-value") 
#print(cotacao_dolar)

# Passo 2: Pegar a cotação do Euro
#navegador.get("https://www.google.com/")
#navegador.find_element(By.XPATH,
#    '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys("cotação euro")
#navegador.find_element(By.XPATH,
#    '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(Keys.ENTER)

#cotacao_euro = navegador.find_element(By.XPATH,
#    '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute("data-value")
#print(cotacao_euro)

# Passo 3: Pegar a cotação do Ouro
#navegador.get("https://www.melhorcambio.com/ouro-hoje")

#cotacao_ouro = navegador.find_element(By.XPATH, '//*[@id="comercial"]').get_attribute("value")
#cotacao_ouro = cotacao_ouro.replace(",", ".")
#print(cotacao_ouro)

#navegador.quit()