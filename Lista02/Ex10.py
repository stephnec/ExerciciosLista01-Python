deltaS = float(input("Digite a distância em metros: "))
t = float(input("Digite o tempo em segundos: "))

vms = deltaS / t
vkmh = vms * 3.6

print("Velocidade em m/s: ", vms)
print("Velocidade em km/h:", vkmh)