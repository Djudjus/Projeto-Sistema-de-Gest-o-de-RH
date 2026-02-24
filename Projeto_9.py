import datetime

print("-" * 30)
print(f"{'SISTEMA DE RH TECHSOLUTIONS':^30}")
print("-" * 30)

nome = input("Nome do colaborador: ")
salario_atual = float(input(f"Salário atual de {nome}: R$"))

# Lógica de mercado: Quem ganha menos recebe um aumento percentual maior
if salario_atual <= 2000:
    novo_salario = salario_atual + (salario_atual * 0.15)
    percentual = 15
elif salario_atual <= 5000:
    novo_salario = salario_atual + (salario_atual * 0.10)
    percentual = 10
else:
    novo_salario = salario_atual + (salario_atual * 0.05)
    percentual = 5


# Simulação de desconto de INSS para efeito do exercício
inss = novo_salario * 0.11
salario_liquido = novo_salario - inss

# Saída profissional com formatação de moeda)
print(f"\n--- RELATÓRIO DE REAJUSTE [{datetime.date.today().year}] ---")
print(f"Colaborador: {nome}")
print(f"Aumento aplicado: {percentual}%")
print(f"Salário Bruto: R${novo_salario:>10.2f}")
print(f"Desconto INSS: R${inss:>10.2f}")
print("-" * 35)
print(f"Salário Líquido: R${salario_liquido:>10.2f}")
print("-" * 35)
