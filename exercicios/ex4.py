import csv

def gravar_resultados(total_vendas, vendas_filtradas, nome_arquivo='resultados.csv'):
    with open(nome_arquivo, 'w', newline='', encoding='utf-8') as arquivo_csv:
        escritor = csv.writer(arquivo_csv)
        escritor.writerow(['Produto', 'Quantidade', 'Preço_Unitário', 'Total_Venda'])
        for venda in vendas_filtradas:
            produto = venda[1]
            quantidade = int(venda[2])
            preco_unitario = float(venda[3])
            total_venda = quantidade * preco_unitario
            escritor.writerow([produto, quantidade, preco_unitario, f"{total_venda:.2f}"])
        escritor.writerow([])
        escritor.writerow(['Total de Vendas', f"{total_vendas:.2f}"])

# NAO ENTENDI
