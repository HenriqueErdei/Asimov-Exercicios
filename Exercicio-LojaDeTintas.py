print("Seja bem vindo a loja de tintas.")
print("Informe qual o valor da área que deseja pintar")
area = float(input())

volume_necessario = area / 3
latas =  int(volume_necessario / 18)
custo = latas * 80

print("voce precisara de {} latas e elas custarão {} reais".format(latas,custo))