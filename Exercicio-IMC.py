altura = float(input("Qual a sua altura?"))
peso = int(input("Qual o seu peso?"))

multiplicar_altura = (altura * altura)

dividir_peso_por_altura = (peso / multiplicar_altura)

resultado_final = int(dividir_peso_por_altura)

print("Seu IMC é {:.2f}".format(resultado_final))