# Metodologia
Esse é uma documentação de qual foi minha linha de raciocínio para realizar o teste de nivelamento.

## Teste de Web Scraping
### Configurando meu ambiente de desenvolvimento

#### Escolha da linguagem
Ao receber a tarefa, vi que teria que trabalhar com Python ou Java, dado o escopo do projeto, e visando a linguagem que tenho maior domínio, decidi por usar **python**.

#### Instalação de requisitos
Primeiro, instalei o `Python`, criei um ambiemente virtual e instalei as seguintes bibliotecas: `BeautifuSoup4`, `Selenium`, `Scrapy` e `Lxml`. O motivo para instalar bilbiotecas diferentes de webscreping, é para testar a velocidade de execução de cada uma e comparar a forma mais performática de se executar essa tarefa. Considerando que meu ambiente de desenvlvimento é o Arch linux usando Nvim, para realizar essas tarefas, executei os seguintes comandos:

```bash
sudo pacman -Syu # Atualizar o sistema
sudo pacman -S python # Instalar python

mkdir ~/teste-de-nivelamento # Criar pasta contendo o projeto
cd ~/teste-de-nivelamento # Ir para tal pasta
git init # Iniciar versionamento do projeto

touch README.md # Criar arquivo para explicar funcionamento do projeto
touch Metodologia.md # Criar arquivo para explicar sua metodologia de desenvolvimento

python -m venv webscrap # Criar um ambiente virtual para webscraping
source webscrap/bin/activate # iniciar o ambiente virtual

pip install --upgrade pip # Devido a natureza do Arch, provavelmente será necessário atualizar o pip

pip install BeautifulSoup4 selenium scrapy lxml # Instalar as bibliotecas
```
e também é necessário criar o arquivo .gitignore considerando o venv, por isso, usei o padrão do github, disponível em: https://github.com/github/gitignore/blob/main/Python.gitignore e adicionei os seguintes itens no arquivo:

```git
lxml/
scrapy/
selenium/
soup/
download/
anexos_I_e_II
```

#### Teste de performance
Para os testes de performance, foi feito um script usando o `timeit`, pode executar ele com:
```bash
python scrap_performance.py
```
E com o tipo de teste padrão e com 50 iterações, estes foram os resultados:
```
Tempo de execução com BeautifulSoup:
Tempo médio de 50 iterações:
0.5095246508599667

Tempo de execução com Scrapy:
Tempo médio de 50 iterações:
0.45109446000002207

Tempo de execução com Selenium:
Tempo médio de 50 iterações:
2.6060390113799077

Tempo de execução com LXML:
Tempo médio de 50 iterações:
0.5261936143798812
```
Logo, o restante do processo será usando Scrapy.

