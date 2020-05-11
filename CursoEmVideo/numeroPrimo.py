def primos(numero):
    total_de_divisao = 0
    for primo in range(1,numero + 1):
        if numero % primo == 0:
            total_de_divisao += 1

    if total_de_divisao <= 2:
        return print(f'O número: {numero}, é um número primo pois é so e divisivel por 1 e por {numero}')
  
    else:
        return print(f'O número: {numero}, não é primo!')
    

numero = int(input('digite um numero: '))
primos(numero)