#Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.
import math

#ENTRADA
dia = int(input('Dia:'))
mes = int(input('Mês:'))
ano = int(input('Ano:'))

#PROCESSAMENTO/SAÍDA
if (mes==1 or mes==3 or mes==5 or mes==7 or mes==8 or mes==10 or mes==12):
    if (dia<=31):
        print('Data válida')
    else:
        print('Data inválida')

if (mes==4 or mes==6 or mes==9 or mes==11):
    if (dia<=30):
        print('Data válida')
    else:
        print('Data inválida')
        
if (mes==2):
    if (dia<=28):
        print('Data válida')
    else:
        print('Data inválida')
