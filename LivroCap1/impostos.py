salario = float(input('digite seu salario: '))
base = salario
imposto = 0


if base > 3000:
    imposto += (base - 3000) * 0.35
    print(f'seu salario: {salario} R$, total de impostos apagar {imposto} R$')

if base> 1000:
    imposto += (base - 1000) * 0.20
    print(f'seu salario: {salario} R$, total de impostos apagar {imposto} R$')

