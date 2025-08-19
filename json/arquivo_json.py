import json

# Substitua 'seuarquivo.json' pelo nome do seu arquivo JSON
with open('seuarquivo.json', 'r', encoding='utf-8') as arquivo:
    dados = json.load(arquivo)
    print(dados)