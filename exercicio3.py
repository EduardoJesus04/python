print("Saiba qual será o reajuste de seu salário!!!")

salario = float(input("Digite seu salário: "))

if (salario <= 280):
    ajuste = 20
elif (salario <= 700):
    ajuste = 15
elif (salario <= 1500):
    ajuste = 10
elif (salario >= 1500):
    ajuste = 5

print("Seu salário era de: ", str(salario))
print("Recebeu aumento de: ", str(ajuste), "%")

ajuste = salario / 100
aumento = salario * ajuste
salario_reajustado = salario + ajuste

print("O aumento do seu salário será de: ", str(aumento))
print("O seu novo salário será de: ", str(salario_reajustado))


