import csv  

def ler_dados_csv ():
    with open('exercicio1.csv', newline='', encoding='utf-8') as csvfile:
        leitor = csv.reader(csvfile)
        for linha in leitor:
            print(linha)

ler_dados_csv()