import csv

# Substitua 'seuarquivo.csv' pelo nome do seu arquivo CSV
with open('seuarquivo.csv', newline='', encoding='utf-8') as csvfile:
    leitor = csv.reader(csvfile)
    for linha in leitor:
        print(linha)