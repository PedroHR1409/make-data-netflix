# Github com os arquivos fonte
https://github.com/digitalinnovationone/netflix-dataset/

# Instalações necessárias
Python 3.x

# Conceitos
* Virtual Environment (venv)
* Mkdir
* Lib Glob
* Regex
* Organização do projeto (pastas)
* Dados crus (raw) são tratados e salvos após o tratamento (ready)
* Dados prontos (ready) são os dados após o tratamento do script deste projeto

# Comandos terminal
## 1. Criar um diretório para execução do projeto
mkdir make-data-netflix
## 2. Abre o vscode utilizando o diretório informado
code make-data-netflix

## 3. Cria o python em um ambiente virtual isolado
python -m venv venv 

## 4. Conectando ao ambiente virtual (venv)
venv/scripts/activate

## 5. Instalação Bibliotecas Python -> pip install <biblioteca>
Biblioteca | Descrição
:----------: | :---------:
Pandas | Será utilizado para manipular Dataframes
Openpyxl | Será utilizado para ler arquivos Excel
xlsxwriter | Será utilizado para escrever em arquivos Excel
