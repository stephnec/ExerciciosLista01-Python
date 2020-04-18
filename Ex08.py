valorBoleto = float(input("Digite o valor do boleto: "))
juros = int(input("Digite o percentual de juros a ser cobrado: "))
dias = int(input("Digite quantos dias está em atraso: "))

novoValor = float(valorBoleto + (valorBoleto * (juros / 100)) * dias)

print("O novo valor do boleto a ser cobrado é de: " + str(novoValor) + " reais")