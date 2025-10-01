
# 3- Conversor de Temperatura
# Crie um programa que converta temperaturas entre Celsius, Fahrenheit e Kelvin.
# O usuário deve informar a temperatura, a unidade de origem e a unidade para qual deseja converter.

# Conversor de Temperatura

print("Unidades disponíveis: Celsius (C), Fahrenheit (F), Kelvin (K)")

temp = float(input("Digite a temperatura: "))
origem = input("Digite a unidade de origem (C/F/K): ").upper()
destino = input("Digite a unidade de destino (C/F/K): ").upper()

# Converter para Celsius primeiro
if origem == "C":
    celsius = temp
elif origem == "F":
    celsius = (temp - 32) * 5/9
elif origem == "K":
    celsius = temp - 273.15
else:
    print("Unidade de origem inválida!")
    exit()

# Converter de Celsius para destino
if destino == "C":
    convertido = celsius
elif destino == "F":
    convertido = (celsius * 9/5) + 32
elif destino == "K":
    convertido = celsius + 273.15
else:
    print("Unidade de destino inválida!")
    exit()

print(f"{temp:.2f}{origem} = {convertido:.2f}{destino}")
