# 1- Conversor de Moeda
# Crie um programa que converte um valor em reais para dólares e euros. Use os seguintes dados:

# * Valor em reais: R$ 100.00
# * Taxa do dólar: R$ 5.20
# * Taxa do euro: R$ 6.15
# O programa deve calcular e exibir os valores convertidos, arredondando para duas casas decimais.

# Dados de entrada
valor_reais = 100 
taxa_usd = 5.20         
taxa_euro = 6.15        

# Conversões
valor_usd = valor_reais / taxa_usd
valor_euro = valor_reais / taxa_euro

# Exibição com 2 casas decimais
print(f"Valor em Real: R$ {valor_reais:.2f}")
print(f"Em USD: US$ {valor_usd:.2f}")
print(f"Em EURO: € {valor_euro:.2f}")