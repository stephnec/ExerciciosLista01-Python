rm = int(input("Digite seu rm: "))

n1 = rm / 10
r1 = int(rm % 10)

n2 = n1 / 10
r2 = int(n1 % 10)

n3 = n2 / 10
r3 = int(n2 % 10)

n4 = n3 / 10
r4 = int(n3 % 10)

n5 = n4 / 10
r5 = int(n4 % 10)

soma = r1 + r2 + r3 + r4 + r5

print(int(r1),int(r2),int(r3),int(r4),int(r5))
print("A soma dos algarismos do rm é: ", soma)