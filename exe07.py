# Faça um Programa que leia três números e mostre o maior e o menor deles.

# ENTRADA
num1 = float(input('Digite um número:'))
num2 = float(input('Digite outro número:'))
num3 = float(input('Digite mais um número:'))

# PROCESSAMENTO/SAÍDA

maior = num1
if num2 > num1 and num2 > num3:
    maior = num2
if num3 > num1 and num3 >= num2:
    maior = num3
menor = num1
if num2 < num3 and num2 < num1:
    menor = num2
if num3 <= num2 and num3 < num1:
    menor = num3

print('O menor número digitado foi:', menor)
print('O maior número digitado foi:', maior)
