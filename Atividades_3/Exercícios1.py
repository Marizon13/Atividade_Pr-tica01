# 1- Classificador de Idade

# Crie um programa que solicite a idade do usuário e classifique-o
# em uma das seguintes categorias:

# *Criança (0-12 anos),
# *Adolescente (13-17 anos),
# *Adulto (18-59 anos) ou
# *Idoso (60 anos ou mais).


# Classificador de Idade

idade = int(input("Digite sua idade: "))

if 0 <= idade <= 12:
    print("Categoria: Criança")
elif 13 <= idade <= 17:
    print("Categoria: Adolescente")
elif 18 <= idade <= 59:
    print("Categoria: Adulto")
elif idade >= 60:
    print("Categoria: Idoso")
else:
    print("Idade inválida!")
