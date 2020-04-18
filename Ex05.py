precoCombustivel = float(input("Digite o preço do litro do combustível: "))
valorDinheiro = float(input("Digite o valor em dinheiro que deseja pagar: "))

litrosTotal = valorDinheiro / precoCombustivel

print("O total de litros a ser comprado é de " + str(litrosTotal) + " litros")