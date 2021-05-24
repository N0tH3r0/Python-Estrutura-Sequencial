'''Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:

    Para homens: (72.7*h) - 58
    Para mulheres: (62.1*h) - 44.7 '''
    
print("Bem vindo ao programa de peso ideal")
gen = input("Qual seu genero biologico? (responda M para masculino e F para Feminino): ")
if gen == "M" or gen == "m":
    altura = float(input("Digite sua altura em metros: ")) 
    res = (72.7 * altura) - 58
    print("Seu peso ideal deve ser:", res)
elif gen == "F" or gen == "f":
    altura = float(input("Digite sua altura em metros: "))
    res = (62.1 * altura) - 44.7
    print("Seu peso ideal deve ser:", res)
else:
    print("Digite um genero biológico valido.")
    quit()

    