#EXERCICIO 16..

#A série de Fibonacci é formada pela seqüência 0,1,1,2,3,5,8,13,21,34,55,... Faça um programa que gere a série até que o valor seja maior que 500.

t1 = 0
t2 = 1

print(f'{t1}, {t2}', end ='')

cont = 3
while cont <= 500 :
    t3 = t1 + t2
    print(f', {t3}', end = '')
    t1 = t2
    t2 = t3
    cont = t3

    