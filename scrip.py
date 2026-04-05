import json
import os
import csv

# 1. Nossa "Base de Dados" (Simulando o que viria do JSON)
vendas_json = [
    {"produto": "Teclado Gamer", "valor": 150, "setor": "Informatica"},
    {"produto": "Mouse Pad", "valor": 30, "setor": "Informatica"},
    {"produto": "Monitor 24p", "valor": 850, "setor": "Monitores"},
    {"produto": "Cabo HDMI", "valor": 45, "setor": "Acessorios"}
]

# 2. Criando a lista vazia para o que vamos filtrar
vendas_filtradas = []
total_vendas = 0
# --- SUA VEZ: PARTE 1 (Lógica de Filtro) ---
# Use um 'for' para percorrer 'vendas_json'
# Use um 'if' para verificar se o 'valor' é maior que 100
# Se for verdade, use o '.append()' para colocar na lista 'vendas_filtradas'

for venda in vendas_json:
    # ESC # Remova o pass e complete
    if (venda["valor"] > 100): vendas_filtradas.append(venda)
    else: pass 

# --- SUA VEZ: PARTE 2 (Exportação para CSV) ---
# Agora vamos salvar a lista 'vendas_filtradas' em um arquivo chamado 'vendas_altas.csv'

colunas = ["produto", "valor", "setor"]

with open("vendas_altas.csv", "w", newline="", encoding="utf-8") as f:
    # 1. Crie o escritor (DictWriter)
    # 2. Escreva o cabeçalho (writeheader)
    # 3. Escreva as linhas (writerows)
    
    vendas_altas = csv.DictWriter(f, fieldnames=colunas)
    vendas_altas.writeheader()
    vendas_altas.writerows(vendas_filtradas)

total_vendas = sum(venda["valor"] for venda in vendas_filtradas)
print(f"o total de vendas acima de 100 é: {total_vendas}")