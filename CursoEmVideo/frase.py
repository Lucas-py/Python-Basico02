#UTF-8

frase = 'o lobo ama o bolo'

nova_frase= frase.replace(' ','')

poli = nova_frase[::-1]

resultado = 'e um polimetro' if nova_frase == poli else 'nao é um pli'

print(f'A frase {frase} {resultado}')

