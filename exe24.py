#Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar.
#O resultado da operação deve ser acompanhado de uma frase que diga se o número é:
import math

#ENTRADA
num1 = float(input('Digite um número:'))
num2 = float(input('Digite outro número:'))
escolha = int(input('Para jogar, escolha (1) par ou ímpar, (2) positivo ou negativo, (3) inteiro ou decimal:'))

#PROCESSAMENTO/SAÍDA
if escolha>3 and escolha<0:
    print('Opção inválida.')
elif escolha==1:
    if (num1%2==0) and (num2%2==0):
        print('Ambos os números são pares.')
    if (num1%2==0) and (num2%2!=0):
        print('O primeiro número é par, o segundo é ímpar.')
    if (num1%2!=0) and (num2%2==0):
        print('O primeiro número é ímpar, o segundo é par.')
    if (num1%2!=0) and (num2%2!=0):
        print('Ambos os números são ímpares.')
elif escolha==2:
    if (num1<0) and (num2<0):
        print('Ambos os números são negativos.')
    if (num1<0) and (num2>0):
        print('O primeiro número é negativo, o segundo é positivo.')
    if (num1>0) and (num2>0):
        print('Ambos os números são positivos.')
    if (num1>0) and (num2<0):
        print('O primeiro número é positivo, o segundo é negativo.')
elif escolha==3:
    if (num1%1==0) and (num2%1==0):
        print('Ambos os números são inteiros.')
    if (num1%1!=0) and (num2%1==0):
        print('O primeiro número é decimal, o segundo é inteiro.')
    if (num1%1==0) and (num2%1!=0):
        print('O primeiro número é inteiro, o segundo é decimal.')
    if (num1%1!=0) and (num2%1!=0):
        print('Ambos os números são decimais.')