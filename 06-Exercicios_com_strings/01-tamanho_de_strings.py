#EXERCICIO 1.. Tamanho de strings. Faça um programa que leia 2 strings e informe o conteúdo delas seguido do seu comprimento. Informe também se as duas strings possuem o mesmo comprimento e são iguais ou diferentes no conteúdo.

#Compara duas strings

#String 1: Brasil Hexa 2006

#String 2: Brasil! Hexa 2006!

#Tamanho de "Brasil Hexa 2006": 16 caracteres

#Tamanho de "Brasil! Hexa 2006!": 18 caracteres

#As duas strings são de tamanhos diferentes.

#As duas strings possuem conteúdo diferente.

s1 = input('Digite uma String: ')
s2 = input('Digite uma String: ')

tamanho1 = len(s1)
tamanho2 = len(s2)

print(f'{s1} : {tamanho1} caracteres.')
print(f'{s2} : {tamanho2} caracteres.')

comparacao_de_tamanho = 'diferentes'
comparacao_de_conteudo = 'diferente'

if s1 == s2:
  comparacao_de_tamanho = 'iguais'
  comparacao_de_conteudo = 'igual'
elif tamanho1 == tamanho2:
  comparacao_de_tamanho = 'iguais'

print(f'As duas String são de tamanhos {comparacao_de_tamanho}')
print(f'As duas String possuem conteudo {comparacao_de_conteudo}')
