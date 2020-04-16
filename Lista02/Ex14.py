vAVista = float(input("Digite o valor total do IPTU à vista: "))
vParcela = float(input("Digite o valor de cada parcela: "))

parcelado = vParcela * 10

desconto = parcelado - vAVista

percentual =  desconto * 100 / parcelado


print("O percentual de desconto é ", percentual, "%")
