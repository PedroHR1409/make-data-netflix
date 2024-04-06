import pandas as pd
import os
import glob # Utilizado para manipular diretórios e arquivos em massa

# Caminho para ler os arquivos raw
folder_path = 'src\\data\\raw'

"""
 JUNTAR OS CAMINHOS DOS ARQUIVOS
glob.glob(<nome_do_caminho>, <root_dir>) é chamado para fazer a união dos caminhos
os.path.join() é chamado para indicarmos que queremos unir os caminhos
folder_path é o local onde está nossos arquivos
'*.xlsx' indica que pegaremos todos os arquivos que terminarem com '.xlsx'
"""

excel_files = glob.glob(os.path.join(folder_path, '*.xlsx')) # Capturando arquivos com extensão .xlsx

if not excel_files:
    print('Nenhum arquivo compatível foi encontrado!') # Se nenhum arquivo for encontrado, retorna mensagem de erro
else:
    dfs = []

    for archive in excel_files:
        
        try:
            dfTemp = pd.read_excel(archive) 
            
            # Pega o nome do arquivo
            file_name = os.path.basename(archive) # Pega o nome dos arquivos usando o os.path.basename()
            
            dfTemp['base_archive'] = file_name

            # Criando coluna 'location' para termos o país de origem do arquivo
            if 'brasil' in file_name.lower():
                dfTemp['location'] = 'br'
            elif 'france' in file_name.lower():
                dfTemp['location'] = 'fr'
            elif 'italian' in file_name.lower():
                dfTemp['location'] = 'it'
            else:
                dfTemp['location'] = None

            # Criar coluna 'campaign' para campanha
            dfTemp['campaign'] = dfTemp['utm_link'].str.extract(r'utm_campaign=(.*)')

            # Salva os dados tratados dentro do df
            dfs.append(dfTemp)

        # Tratando exceções
        except Exception as e:
            print(f'Erro ao ler o arquivo: {archive} : {e}')

if dfs:

    # Concatena todas as tabelas salvas no dfs em uma unica tabela
    result = pd.concat(dfs, ignore_index = True)
    
    # Caminho de saída
    output_file = os.path.join('src', 'data', 'ready', 'clean.xlsx')

    # Configuração do motor de escrita
    writer = pd.ExcelWriter(output_file, engine = 'xlsxwriter')

    # Salvando como excel
    result.to_excel(writer, index = False)
    
    # Salva o arquivo Excel
    writer._save()
else:
    print('Nenhum dado para ser salvo')