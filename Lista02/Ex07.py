num = int(input("Digite um número de 0 a 99: "))

if(num < 0 or num > 99):
    num = int(input("O número deve ser entre 0 a 99: "))
else:
    dezena = int(num / 10)
    unidade = num % 10

    print("Dezena:", dezena)
    print("Unidade:", unidade)