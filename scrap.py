import os, requests, scrapy, shutil, time
from urllib.parse import urljoin

debug = False

def get_pdf_link_scrapy(url):

    if debug: print("Fazendo requisição")

    response = requests.get(url)
    if response.status_code == 200:    

        if debug: print("Requisição feita com sucesso")

        selector = scrapy.Selector(text=response.text)

        if debug: print("Procurando Links")

        for link in selector.xpath("//a"):
            link_xpath = link.xpath("@href").get()

            if not link_xpath.endswith(".pdf"):
                continue

            if not "Anexo_I" in link_xpath:
                continue
            
            if debug: print(f"Link encontrado: {urljoin(url, link_xpath)}")

            download_resource(urljoin(url, link_xpath), "download_pdf", "II" if "Anexo_II" in link_xpath else "I") 
    return None

def download_resource(url, save_folder=".", filecounter="I"):

    if debug: print("Verificando se a pasta existe")

    if not os.path.exists(save_folder) and not save_folder == ".":

        if debug: print("Criando pasta")

        os.makedirs(save_folder)

    if debug: print("Fazendo requisição")
    response = requests.get(url)
    if response.status_code == 200:
        if debug: print("Requisição feita com sucesso")

        filename = os.path.join(save_folder, os.path.basename(f"Anexo_{filecounter}.pdf"))

        if os.path.isdir(filename):
            filename = os.path.join(filename, "downloaded_file")

        with open(filename, 'wb') as file:            
            start_time = time.time()
            if debug: print("Baixando arquivo")
            file.write(response.content)

        if debug: 
            print(f"Download concluido: {url}")
            print(f"Tempo de download: {(time.time() - start_time):.2f} segundos")

    else:
        if debug: print(f"Erro ao fazer download: {url}")

def compact_downloaded_files(save_folder="."):
    if not os.path.exists(save_folder) and not save_folder == ".":
        os.makedirs(save_folder)
    if debug: print("Compactando arquivos")
    shutil.make_archive(os.path.join(save_folder, "anexos_I_e_II"), 'zip', "download_pdf")
    if debug: print("Arquivos compactados\n Finalizando programa")


if __name__ == "__main__":
    get_pdf_link_scrapy("https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos")
    compact_downloaded_files("out")