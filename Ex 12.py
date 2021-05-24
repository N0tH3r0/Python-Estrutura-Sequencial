'''Tendo como dados de entrada a altura de uma pessoa
construa um algoritmo que calcule seu peso ideal
usando a seguinte fórmula: (72.7*altura) - 58 '''

altura = float(input("Digite sua altura em metros para o calculo de peso ideal: "))
res = (72.7 * altura) - 58
print("Seu peso ideal em kg é:", res)
