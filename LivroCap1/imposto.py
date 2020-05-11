#UTF-8

salario = int(input('Digite seu salário: '))
idade = int(input('Digite sua idade: '))

imposto = 'você deve pagar os impostos'if salario >= 1200 and idade >= 20 else 'você não paga os impostos'

print(f'resultado {imposto}')
