#Importa as bibliotecas necessárias para o Web_Scraping
import re
import requests
from bs4 import BeautifulSoup

#Função que faz um request com a url passada como parâmetro e cria um objeto soup que interpreta o html da página
def create_soup(url):
    html = requests.get(url).content
    return BeautifulSoup(html, 'html.parser')


#Criamos um soup com a url inicial do teste e procuramos a tag do html que possui o link para a página com a versão mais recente do Padrão TISS
soup_1 = create_soup("https://www.gov.br/ans/pt-br/assuntos/prestadores/padrao-para-troca-de-informacao-de-saude-suplementar-2013-tiss")
link = soup_1.find("a", string=re.compile("Clique aqui para acessar a versão"))['href']


#Criamos mais um soup com a url da página com a versão mais recente do Padrão TISS e procuramos a tag do html que possui o link para o arquivo Padrão TISS mais recente.
soup_2 = create_soup(link)
file_link = soup_2.find("a", class_="btn btn-primary btn-sm center-block internal-link")['href']


#Fazemos um request do conteúdo do arquivo e pegamos o nome desse arquivo.
file_content = requests.get(file_link).content
file_name = file_link.split("/")[-1]

#Criamos um novo arquivo com o nome do arquivo Padrão TISS mais recente e escrevemos nele o conteúdo de que fizemos o request, depois disso fechamos o arquivo.
file = open(file_name, "wb")
file.write(file_content)
file.close()

print("[Web_Scraping] Arquivo", file_name, "baixado.")
