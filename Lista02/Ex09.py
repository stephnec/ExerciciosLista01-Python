produto = float(input("Digite o valor do produto: "))
percentual = int(input("Digite a porcentagem do desconto: "))

desconto = produto * percentual / 100

produtoNovoValor = produto - desconto

print("O valor do produto reajustado é: ", produtoNovoValor)

