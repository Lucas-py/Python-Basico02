preco = float(input('digite valor do preço: '))
desconto = int(input('digite o valor do desconto: '))

reducao_de_preco = preco * desconto / 100
total_apagar = preco - reducao_de_preco
print(f'total a pagar: {total_apagar}, desconto: {reducao_de_preco}, valor sem desconto: {preco}')
