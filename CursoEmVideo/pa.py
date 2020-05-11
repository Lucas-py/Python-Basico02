razao = int(input('digite a razao: '))
final = int(input('digite numero final: '))

for numero in range(0,final,razao):
 
    if numero < final:
        print(numero)
    else:
        break

