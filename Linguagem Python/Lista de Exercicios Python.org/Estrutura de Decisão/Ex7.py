#Faça um Programa que leia três números e mostre o maior e o menor deles.
numeros = []
for c in range(1,4):
    numero = int(input(f'Informe o {c}\u00b0 número: '))
    numeros.append(numero)
print(f'O maior foi o {max(numeros)}, o menor foi o {min(numeros)}.')