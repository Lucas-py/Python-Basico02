'''
Escreva um programa que pergunte a velocidade do carro de um usuário.
 Caso ultrapasse 80 km/h, exiba uma mensagem dizendo que o usuário foi multado.
 Nesse caso, exiba o valor da multa, cobrando R$ 5 por km acima de 80 km/h.
'''

velocidade = int(input('digite a velcidade do veiculo:  '))

if velocidade > 80:
    taxa =  velocidade - 80
    multa = 5 * taxa
    print(f'VOCÊ FOI MULTADO PAGUE: {multa} R$, SUA VELOCIDADE ERA DE: {velocidade} o limite e de 80 km')
else:
    print(f'parabéns você não foi multudado sua velocidade é de {velocidade}')

