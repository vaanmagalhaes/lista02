#Atividade 1: Suponha que um clube esportivo está realizando o cadastro de atletas e
#precisa classificá-los de acordo com sua categoria, de maneira que ao final o algoritmo mostre na tela:
#“Fulano, você se enquadra na categoria: ...”
#As faixa de idade para classificação são:
#Infantil (até 9 anos)
#Juvenil (de 9 a 15 anos)
#Junior (de 16 a 18 anos)
#Adulto (maior que 18 anos)

#ENTRADA
print('Bem-vindo ao processo de cadastro!')
nome = input('Nos diga seu nome:')
nome = nome.capitalize()
idade = int(input('Agora usando apenas números, nos diga sua idade:'))

#PROCESSAMENTO
if idade<=9:
    print(nome, 'você se enquadra na categoria INFANTIL')
elif idade>9 and idade<=15:
    print(nome, 'você se enquadra na categoria JUVENIL')
elif idade>15 and idade<=18:
    print(nome, 'você se enquadra na categoria JUNIOR')
elif idade>18:
    print(nome, 'você se enquadra na categoria ADULTO')

print('Bem vindo ao clube!')