salario = float(input("Digite o valor do seu salário: "))
despesas = float(input("Digite suas despesas mensais: "))

sobra = salario - despesas
anos = (1000000 - sobra) / 12

print("Será necessário " + str(anos) + " anos para ser milionario")