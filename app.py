import csv
import os

def criar_arquivos_produtos():
    if not os.path.exists("produtos.csv"):
        with open("produtos.csv", "w", newline="", encoding="utf-8") as arquivo:
            writer = csv.writer(arquivo)
            
            writer.writerow([
                "id_produto",
                "nome",
                "categoria",
                "quantidade",
                "preco",
                "fornecedor",
                "data_adicao"
            ])
  

def menu():
    print("Sistema de Estoque")

    
criar_arquivos_produtos()
menu()

