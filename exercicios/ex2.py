import csv

def calcular_total_vendas():
    with open('exercicio1.csv', newline='', encoding='utf-8') as csvfile:
        leitor = csv.reader(csvfile)
        linhas = list(leitor)
        for i in linhas:
            if i[0] != 'ID_Venda':
                total = int(i[2]) * float(i[3])
                print(f"Total da venda do produto {i[1]}: R$ {total:.2f}")
        print(f"O numero de vendas: {len(linhas) - 1}")
        return

calcular_total_vendas()