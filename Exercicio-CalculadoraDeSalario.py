print("Calculadora de Salario")

print("Informe seu salario por horas")
salario_hora = float(input())

print("Informe quantas horas trabalhou no mes")
horas_trabalhadas = float(input())

salario  = (salario_hora * horas_trabalhadas)
ir = (salario * 0.11)
inss = (salario - ir) * 0.08
sindicato = (salario - ir - inss) * 0.05

print("--------------------------------------------")
print("Salario bruto R${:.2f}".format(salario))
print("Valor pago de IR R${:.2f}".format(ir))
print("Valor pago de INSS R${:.2f}".format(inss))
print("Valor pago de sindicato R${:.2f}".format(sindicato))
print("Salario liquido R${:.2f}".format(salario - ir - inss - sindicato))

