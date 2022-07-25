#PROJETO 1...

#Controle de cotas de disco. A ACME Inc., uma organização com mais de 1500 funcionários, está tendo problemas de espaço em disco no seu servidor de arquivos. Para tentar resolver este problema, o Administrador de Rede precisa saber qual o espaço em disco ocupado pelas contas dos usuários, e identificar os usuários com maior espaço ocupado. Através de um aplicativo baixado da Internet, ele conseguiu gerar o seguinte arquivo, chamado usuarios.txt:

#alexandre       456123789
#anderson        1245698456
#antonio         123456456
#carlos          91257581
#cesar           987458
#rosemary        789456125
#Neste arquivo, o primeiro campo corresponde ao login do usuário e o segundo ao espaço em disco ocupado pelo seu diretório home. A partir deste arquivo, você deve criar um programa que gere um relatório, chamado relatório.txt, no seguinte formato:

#ACME Inc.           Uso do espaço em disco pelos usuários
#------------------------------------------------------------------------
#Nr.  Usuário        Espaço utilizado     % do uso

#1    alexandre       434,99 MB            16,85%
#2    anderson       1187,99 MB            46,02%
#3    antonio         117,73 MB             4,56%
#4    carlos           87,03 MB             3,37%
#5    cesar             0,94 MB             0,04%
#6    rosemary        752,88 MB            29,16%
#Espaço total ocupado: 2581,57 MB

#Espaço médio ocupado: 430,26 MB

#O arquivo de entrada deve ser lido uma única vez, e os dados armazenados em memória, caso sejam necessários, de forma a agilizar a execução do programa. A conversão da espaço ocupado em disco, de bytes para megabytes deverá ser feita através de uma função separada, que será chamada pelo programa principal. O cálculo do percentual de uso também deverá ser feito através de uma função, que será chamada pelo programa principal.

#Recursos adicionais: opcionalmente, desenvolva as seguintes funcionalidades:

#Ordenar os usuários pelo percentual de espaço ocupado; Mostrar apenas os n primeiros em uso, definido pelo usuário;

#Gerar a saída numa página html;

#Criar o programa que lê as pastas e gera o arquivo inicial;

lista_de_dados = []

def transformar_em_megabytes(tamanho_em_bytes:str) -> float:
  return int(tamanho_em_bytes) / (2**10) **2



with open('sample_data/usuarios.txt', 'r') as arquivo:
  for linha in arquivo:
    linha = linha.strip()
    usuario = linha[:15]
    tamanho_em_disco = transformar_em_megabytes(linha[16:])

    lista_de_dados.append((tamanho_em_disco, usuario))




cabecalho = ''' ACME Inc.               Uso do espaço em disco pelos usuários
-------------------------------------------------------------
Nr.     Usuário        Espaço utilizado     % do uso
'''

n = int(input('Digite o número de usuarios a serem exibidos: '))

lista_de_dados.sort(reverse=True)
lista_de_dados = lista_de_dados [:n]

with open('sample_data/relatorio.txt', 'w') as arquivo:
  tamanho_total_consumido = sum([tamanho for tamanho,_ in lista_de_dados ])
  media = tamanho_total_consumido/len(lista_de_dados)
  arquivo.writelines(cabecalho)
  for indice, dados in enumerate(lista_de_dados, start=1):
    tamanho_em_disco, usuario = dados
    arquivo.writelines(f'{indice:<4}    {usuario} {tamanho_em_disco:9.2f} MB'
    f'         {tamanho_em_disco / tamanho_total_consumido:>6.2%}\n')


  arquivo.writelines('\n')
  arquivo.writelines(f'Espaço total ocupado: {tamanho_total_consumido:.2f} MB\n')
  arquivo.writelines(f'Espaço médio ocupado:  {media:.2f} MB')

  