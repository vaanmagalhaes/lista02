#Faça um Programa que peça um número e informe se o número é inteiro ou decimal. Dica: utilize uma função de arredondamento.
import math

#ENTRADA
num = float(input('Digite um número:'))

#PROCESSAMENTO
if (num%1==0):
    print('Número inteiro')
else:
    print('Número decimal')