'''Usar a variavel peso pra calcular o excedente(se o valor colocado for maior que 50) e 
        O valor da multa de R$4.00 por excedente'''

peso = float(input("Digite a quantidade peixes em kg: "))
if peso > 50:
    excedente = peso - 50
    multa = 4.00
    res = (excedente * multa)
    print("O Excedente em kg foi:", excedente, "e o valor da multa sera em:", res, "reais")
else:
    print("Não houve excedente")
    