setup_with_download = """
import os, requests, scrapy
from lxml import html
from selenium import webdriver
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

def get_pdf_link_soup(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        for link in soup.find_all("a"):
            if link.get("href").endswith(".pdf") and "Anexo_I" in link.get("href"):
                download_resource(urljoin(url, link.get("href")), "soup")
    return None 

def get_pdf_link_scrapy(url):
    response = requests.get(url)
    if response.status_code == 200:
        selector = scrapy.Selector(text=response.text)
        for link in selector.xpath("//a"):
            if link.xpath("@href").get().endswith(".pdf") and "Anexo_I" in link.xpath("@href").get():
                download_resource(urljoin(url, link.xpath("@href").get()), "scrapy")
    return None

def get_pdf_link_selenium(url):
    driver = webdriver.Chrome()
    driver.get(url)
    response = driver.page_source
    driver.quit()

    if response:
        selector = scrapy.Selector(text=response)
        for link in selector.xpath("//a"):
            if link.xpath("@href").get().endswith(".pdf") and "Anexo_I" in link.xpath("@href").get():
                download_resource(urljoin(url, link.xpath("@href").get()), "selenium")
    return None

def get_pdf_link_lxml(url):
    response = requests.get(url)
    if response.status_code == 200:
        tree = html.fromstring(response.text)
        for link in tree.xpath("//a"):
            if link.get("href").endswith(".pdf") and "Anexo_I" in link.get("href"):
                download_resource(urljoin(url, link.get("href")), "lxml")
    return None
    
def download_resource(url, save_folder="."):
    if not os.path.exists(save_folder) and not save_folder == ".":
        os.makedirs(save_folder)

    response = requests.get(url)
    if response.status_code == 200:
        filename = os.path.join(save_folder, os.path.basename(urlparse(url).path))
        if os.path.isdir(filename):
            filename = os.path.join(filename, "downloaded_file")
        with open(filename, 'wb') as file:
            file.write(response.content)
        print(f"Downloaded: " + url)
    else:
        print("Failed to Download: " + url)
"""

setup_with_print ="""
import os, requests, scrapy
from lxml import html
from selenium import webdriver
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

def get_pdf_link_soup(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        for link in soup.find_all("a"):
            if link.get("href").endswith(".pdf") and "Anexo_I" in link.get("href"):
                print(urljoin(url, link.get("href")))
    return None 

def get_pdf_link_scrapy(url):
    response = requests.get(url)
    if response.status_code == 200:
        selector = scrapy.Selector(text=response.text)
        for link in selector.xpath("//a"):
            if link.xpath("@href").get().endswith(".pdf") and "Anexo_I" in link.xpath("@href").get():
                print(urljoin(url, link.xpath("@href").get()))
    return None

def get_pdf_link_selenium(url):
    driver = webdriver.Chrome()
    driver.get(url)
    response = driver.page_source
    driver.quit()

    if response:
        selector = scrapy.Selector(text=response)
        for link in selector.xpath("//a"):
            if link.xpath("@href").get().endswith(".pdf") and "Anexo_I" in link.xpath("@href").get():
                print(urljoin(url, link.xpath("@href").get()))
    return None

def get_pdf_link_lxml(url):
    response = requests.get(url)
    if response.status_code == 200:
        tree = html.fromstring(response.text)
        for link in tree.xpath("//a"):
            if link.get("href").endswith(".pdf") and "Anexo_I" in link.get("href"):
                print(urljoin(url, link.get("href")))
    return None
"""

setup_default ="""
import os, requests, scrapy
from lxml import html
from selenium import webdriver
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

def get_pdf_link_soup(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        for link in soup.find_all("a"):
            if link.get("href").endswith(".pdf") and "Anexo_I" in link.get("href"):
                return None
    return None 

def get_pdf_link_scrapy(url):
    response = requests.get(url)
    if response.status_code == 200:
        selector = scrapy.Selector(text=response.text)
        for link in selector.xpath("//a"):
            if link.xpath("@href").get().endswith(".pdf") and "Anexo_I" in link.xpath("@href").get():
                return None
    return None

def get_pdf_link_selenium(url):
    driver = webdriver.Chrome()
    driver.get(url)
    response = driver.page_source
    driver.quit()

    if response:
        selector = scrapy.Selector(text=response)
        for link in selector.xpath("//a"):
            if link.xpath("@href").get().endswith(".pdf") and "Anexo_I" in link.xpath("@href").get():
                return None
    return None

def get_pdf_link_lxml(url):
    response = requests.get(url)
    if response.status_code == 200:
        tree = html.fromstring(response.text)
        for link in tree.xpath("//a"):
            if link.get("href").endswith(".pdf") and "Anexo_I" in link.get("href"):
                return None
    return None
"""

soup_code = """
get_pdf_link_soup('https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos')
"""

scrapy_code = """
get_pdf_link_scrapy('https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos')
"""

selenium_code = """
get_pdf_link_selenium('https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos')
"""

lxml_code = """
get_pdf_link_lxml('https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos')
"""

if __name__ == "__main__":
    import timeit

    print("Selecione o tipo de execução:")
    print("1 - Sem Download e Sem Print (Padrão)")
    print("2 - Com download")
    print("3 - Com Print")

    input_option = input()
    if input_option == "1":
        setup = setup_default
    elif input_option == "2":
        setup = setup_with_download
    elif input_option == "3":
        setup = setup_with_print
    else:
        print("Usando opção padrão.")
        setup = setup_default

    print("\nDigite o número de iterações para calcular o tempo médio de execução: ")
    input_iterations = input()
    if input_iterations.isdigit():
        iterations = int(input_iterations)
    else:
        print("Número inválido. Usando 10 iterações.")
        iterations = 10
        
    print("\nTempo de execução com BeautifulSoup:")
    print(f"Tempo médio de {iterations} iterações:")
    print(timeit.timeit(setup=setup, stmt=soup_code, number=iterations)/iterations)

    print("\nTempo de execução com Scrapy:")
    print(f"Tempo médio de {iterations} iterações:")
    print(timeit.timeit(setup=setup, stmt=scrapy_code, number=iterations)/iterations)

    print("\nTempo de execução com Selenium:")
    print(f"Tempo médio de {iterations} iterações:")
    print(timeit.timeit(setup=setup, stmt=selenium_code, number=iterations)/iterations)

    print("\nTempo de execução com LXML:")
    print(f"Tempo médio de {iterations} iterações:")
    print(timeit.timeit(setup=setup, stmt=lxml_code, number=iterations)/iterations)