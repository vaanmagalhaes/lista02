# Faça um Programa que leia três números e mostre o maior deles.

# ENTRADA
num1 = float(input('Digite um número:'))
num2 = float(input('Digite outro número:'))
num3 = float(input('Digite mais um número:'))

# PROCESSAMENTO/SAÍDA
if num1 > num2 and num1 > num3:
    print('Número 1 é maior')
elif num2 > num1 and num2 > num3:
    print('Número 2 é maior')
elif num1 == num2 or num2 == num3 or num1 == num3:
    print('São iguais')
else:
    print('Número 3 é maior')