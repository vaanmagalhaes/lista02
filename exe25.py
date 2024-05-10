pontuacao = 0

'Telefonou para a vítima?'
'Esteve no local do crime?'
'Mora perto da vítima?'
'Devia para a vítima?'
'Já trabalhou com a vítima?'

print('Digite 1 (sim) ou 0 (não)')
resp = int(input('Telefonou para a vítima?'))
pontuacao = pontuacao + resp

print('Digite 1 (sim) ou 0 (não)')
resp = int(input('Esteve no local do crime?'))
pontuacao = pontuacao + resp

print('Digite 1 (sim) ou 0 (não)')
resp = int(input('Mora perto da vítima?'))
pontuacao = pontuacao + resp

print('Digite 1 (sim) ou 0 (não)')
resp = int(input('Devia para a vítima?'))
pontuacao = pontuacao + resp

print('Digite 1 (sim) ou 0 (não)')
resp = int(input('Já trabalhou com a vítima?'))
pontuacao = pontuacao + resp

if pontuacao == 0:
    print('Você é inocente.')

elif pontuacao <= 2:
    print('Você é um suspeito.')

elif pontuacao >= 3 and pontuacao <= 4:
    print('Você é um cúmplice...')

else:
    print('Você é o assassino!')
