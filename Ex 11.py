'''Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:

    o produto do dobro do primeiro com metade do segundo .
    a soma do triplo do primeiro com o terceiro.
    o terceiro elevado ao cubo.'''
    
 
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
num3 = int(input("Digite o terceiro número: "))
res1 = (num1 * 2) * (num2 / 2)
res2 = (num1 * 3 ) + num3
res3 = num3 ** 3
print(res1, res2, res3)