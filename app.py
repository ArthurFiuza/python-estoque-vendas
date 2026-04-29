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
            
def escolherOpcao():
    print("******************")
    print("     Bem vindo\n        ao\nSistema de Estoque")
    print("******************")
    opcao = input("\nDigite a opção que deseja escolher: ").lower()
  

def menu():
   
    opcao = escolherOpcao()
    
    match opcao:
        case 'a':
            return print("Opção escolhida: A")
        case 'b':
            return print("Opção escolhida: B")
        case 'c':
            return print("Opção escolhida: C")
        case 'd':
            return print("Opção escolhida: D")

    
criar_arquivos_produtos()
menu()

