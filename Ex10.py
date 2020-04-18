a = int(input("Digite quantos votos recebeu o candidato A: "))
b = int(input("Digite quantos votos recebeu o candidato B: "))
c = int(input("Digite quantos votos recebeu o canditdato C: "))
branco = int(input("Digite quantos votos foram em branco: "))
nulo = int(input("Digite quantos votos foram nulos: "))

total = a + b + c + branco + nulo

perA = (a * 100) / total
perB = (b * 100) / total
perC = (c * 100) / total
perBranco = (branco * 100) / total
perNulo = (nulo * 100) / total

print("O candidato A recebeu " + str(a) + " votos, tendo " + str(perA) + "% dos votos")
print("O candidato B recebeu " + str(b) + " votos, tendo " + str(perB) + "% dos votos")
print("O candidato C recebeu " + str(c) + " votos, tendo " + str(perC) + "% dos votos")
print("Os votos em branco representam " + str(perBranco) + "% dos votos")
print("Os votos nulos representam " + str(perNulo) + "% dos votos")