#Faça um Programa que peça um número correspondente a um determinado ano e em seguida informe se este ano é ou não bissexto.
import math

#ENTRADA
print('Vamos descobrir se um ano é bissexto.')
ano = float(input('Digite um ano:'))

#PROCESSAMENTO/SAÍDA
if ano%4==0 and ano%100!=0:
    print('É um ano bissexto!')
else:
    print('Não é um ano bissexto.')