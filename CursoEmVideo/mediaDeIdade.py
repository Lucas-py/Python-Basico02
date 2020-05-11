
maior_idade = 0
media_de_idade = 0
feminino = 0
nome= ''
for v in range(1,5):
    print('-'*20, f'pessoas {v}', '-'*20)
    name = input('digite seu nome: ')
    idade = int(input('digite sua idade: '))
    sexo = input('digite seu sexo: ')
    print()

    media_de_idade += idade

    if sexo == 'f':
        if idade <= 20:
            feminino += 1

    if idade > maior_idade and sexo in 'Mm':
            maior_idade = idade
            nome = name

print('-'*20, 'resultado', '-'*20)
print(f'media das idade e de: {media_de_idade / 4}')
print(f'maior idade {nome} {maior_idade} anos')
print(f'número de mulheres com idade abaixo ou igual a 20 e de {feminino}')
            



