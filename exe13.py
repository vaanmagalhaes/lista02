#Faça um Programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.

#ENTRADA
dia = float(input('Digite um número entre 1 e 7:'))

#PROCESSAMENTO
if dia == 1:
    print('Domingo')
elif dia == 2:
    print('Segunda-feira')
elif dia == 3:
    print('Terça-feira')
elif dia == 4:
    print('Quarta-feira')
elif dia == 5:
    print('Quinta-feira')
elif dia == 6:
    print('Sexta-feira')
elif dia == 7:
    print('Sábado')
else:
    print('Valor inválido')