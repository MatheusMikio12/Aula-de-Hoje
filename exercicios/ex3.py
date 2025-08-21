import csv 

def filtrar_vendas_por_produto(produto):
    with open('exercicio1.csv', newline='', encoding='utf-8') as csvfile:
        leitor = csv.reader(csvfile)
        linhas = list(leitor)
        vendas_filtradas = [linha for linha in linhas if linha[1].lower() == produto.lower() and linha[0] != 'ID_Venda']
        for venda in vendas_filtradas:
            print(venda)
        print(f"Número de vendas do produto '{produto}': {len(vendas_filtradas)}")
    return

filtrar_vendas_por_produto('Headset')