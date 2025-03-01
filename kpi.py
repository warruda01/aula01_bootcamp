CONSTANTE_BONUS = 1000.00

# O programa deve começar solicitando ao usuário que insira seu nome.
nome_usuario = input("Digite seu nome --> ")

# Em seguida, o programa deve pedir ao usuário para inserir o valor do seu salário. 
# Considere que este valor pode ser um número decimal.
salario = float(input("Digite o seu salário -->"))

# Depois, o programa deve solicitar a porcentagem do bônus recebido pelo usuário, 
# que também pode ser um número decimal
porcentagem_bonus = float(input("Digite a porcentagem (em %) do Bônus --> "))

# O cálculo do KPI do bônus de 2024 é de 1000 + salario * bônus
valor_bonus = float((salario * porcentagem_bonus/100) + salario + CONSTANTE_BONUS)

# Finalmente, o programa deve imprimir uma mensagem no seguinte formato:
# "Olá [nome], o seu valor bônus foi de 5000".
# poderia ser --> print("Olá " + nome + ", seu bonus foi de " + str(bonus))
print(f"Olá {nome_usuario}, o seu valor de bonus foi de {valor_bonus}")
