pesos = ''
maior_peso = 0
menor_peso = 0
for c in range(1,6):
    peso = float(input(f'pessoa: {c} digite seu peso: '))

    if c == 1:
        menor_peso = peso
        maior_peso = peso
    else:
        if peso > maior_peso:
            maior_peso = peso
        if peso < menor_peso:
            menor_peso = peso
            

print(f'maior peso e de: {maior_peso}')
print(f'menor peso e de: {menor_peso}')




