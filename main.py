import xmltodict  # Biblioteca para converter arquivos XML em dicionários Python.
import os  # Biblioteca para manipulação de arquivos e diretórios.
import pandas as pd  # Biblioteca para manipulação de dados e criação de tabelas.

def pegar_infos(nome_arquivo, valores):
    """
    Função que extrai informações de um arquivo XML de nota fiscal e as adiciona a uma lista.

    Parâmetros:
    - nome_arquivo (str): Nome do arquivo XML a ser lido.
    - valores (list): Lista onde os dados extraídos serão armazenados.
    """

    # Abre o arquivo XML localizado dentro da pasta "nfs"
    with open(f'nfs/{nome_arquivo}', "rb") as arquivo_xml:
        # Converte o conteúdo do XML em um dicionário Python
        dic_arquivo = xmltodict.parse(arquivo_xml)

        # As notas fiscais podem estar estruturadas de duas formas diferentes:
        # 1. Diretamente dentro da chave "NFe"
        # 2. Dentro de "nfeProc" > "NFe"
        if "NFe" in dic_arquivo:
            infos_nf = dic_arquivo["NFe"]['infNFe']
        else:
            infos_nf = dic_arquivo['nfeProc']["NFe"]['infNFe']

        # Extração dos dados necessários
        numero_nota = infos_nf["@Id"]  # Identificação da nota fiscal
        empresa_emissora = infos_nf['emit']['xNome']  # Nome da empresa que emitiu a nota
        nome_cliente = infos_nf["dest"]["xNome"]  # Nome do destinatário (cliente)
        endereco = infos_nf["dest"]["enderDest"]  # Endereço do cliente

        # Algumas notas podem não ter informação sobre peso dentro da chave "vol"
        if "vol" in infos_nf["transp"]:
            peso = infos_nf["transp"]["vol"]["pesoB"]  # Peso da mercadoria
        else:
            peso = "Não informado"  # Caso o peso não esteja disponível

        # Adiciona os dados coletados na lista de valores
        valores.append([numero_nota, empresa_emissora, nome_cliente, endereco, peso])

# Lista todos os arquivos dentro da pasta "nfs"
lista_arquivos = os.listdir("nfs")

# Definição das colunas para o DataFrame
colunas = ["numero_nota", "empresa_emissora", "nome_cliente", "endereco", "peso"]
valores = []  # Lista onde serão armazenados os dados extraídos

# Para cada arquivo encontrado na pasta "nfs", chama a função pegar_infos
for arquivo in lista_arquivos:
    pegar_infos(arquivo, valores)

# Cria um DataFrame com os dados extraídos e define as colunas
tabela = pd.DataFrame(columns=colunas, data=valores)

# Salva os dados extraídos em um arquivo Excel chamado "NotasFiscais.xlsx"
tabela.to_excel("NotasFiscais.xlsx", index=False)  # index=False para não incluir a numeração automática

