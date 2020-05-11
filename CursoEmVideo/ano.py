maior_de_idade = 0
menor_de_idade = 0
ano_atual = 2020

for ano in range(0,7):
    ano_de_nascimento = int(input(f'pessoa{ano} digite sua idade: '))
    
    if ano_atual - ano_de_nascimento >= 21:
        maior_de_idade += 1
    else:
        menor_de_idade += 1

print(f'quantidade de pessoas maiores de idade {maior_de_idade}, quantidade de menores de idade{menor_de_idade}')
        


