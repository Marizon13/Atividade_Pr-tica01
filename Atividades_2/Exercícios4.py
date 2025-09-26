# 4.Calculadora de Consumo de Combustível
# Desenvolva um programa que calcula o consumo médio de combustível de um veículo. Use os seguintes dados:

# * Distância percorrida: 300 km
# * Combustível gasto: 25 litros
# O programa deve calcular o consumo médio (km/l) e exibir todos os dados da viagem, incluindo o resultado final arredondado para duas casas decimais.

# Dados de entrada
distancia_km = 300.0   
combustivel_l = 25.0   

# Cálculo do consumo médio (km por litro)
consumo_km_por_l = distancia_km / combustivel_l

# Exibição dos resultados
print("=== Consumo de Combustível ===")
print(f"Distância percorrida: {distancia_km:.2f} km")
print(f"Combustível gasto: {combustivel_l:.2f} L")
print(f"Consumo médio: {consumo_km_por_l:.2f} km/L")