salAntigo = float(input("Digite o valor do salário antigo: "))
salNovo = float(input("Digite o valor do salário novo: "))

percentual = (100 * salNovo / salAntigo) - 100

print("O percentual de aumento do salário é: ", int(percentual), "%")