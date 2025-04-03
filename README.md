# Extrator de Informações de Notas Fiscais (XML)

Este projeto tem como objetivo automatizar a extração de informações de notas fiscais eletrônicas (NF-e) armazenadas em arquivos XML. Ele processa os arquivos, extrai os principais dados e os exporta para uma planilha Excel.

📌 Funcionalidades

Leitura automática de arquivos XML de notas fiscais.

Extração de informações essenciais, como:

Número da nota fiscal.

Nome da empresa emissora.

Nome e endereço do cliente.

Peso da mercadoria (se disponível).

Armazenamento dos dados em um DataFrame com Pandas.

Exportação dos dados para um arquivo Excel (NotasFiscais.xlsx).

🛠 Tecnologias Utilizadas

Python

xmltodict (para converter XML em dicionário)

Pandas (para manipulação de dados e geração da planilha Excel)

OS (para manipulação de arquivos e diretórios)

📂 Estrutura do Projeto

📁 nfs/                # Pasta onde os arquivos XML das NF-es devem ser armazenados
📜 extrator.py         # Script principal para extração e exportação dos dados
📜 NotasFiscais.xlsx   # Arquivo Excel gerado com os dados extraídos
📜 README.md           # Documentação do projeto

🚀 Como Usar

Clone o repositório:

git clone https://github.com/seu-usuario/nome-do-repositorio.git
cd nome-do-repositorio

Instale as dependências:

pip install pandas xmltodict

Adicione os arquivos XML na pasta nfs/.

Execute o script:

python extrator.py

O arquivo NotasFiscais.xlsx será gerado com os dados extraídos.

📌 Observações

Certifique-se de que os arquivos XML das notas fiscais estejam corretamente armazenados na pasta nfs/.

Caso alguma nota não tenha a informação de peso, o campo será preenchido com "Não informado".

📜 Licença

Este projeto está sob a licença MIT - sinta-se livre para utilizá-lo e modificá-lo conforme necessário.
