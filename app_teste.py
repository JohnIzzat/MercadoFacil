import openpyxl
from openpyxl import Workbook
import customtkinter as ctk

# variavel Janela representa a Interface gráfica

# Criando a Janela principal
janela = ctk.CTk()
janela.title("Mercado Facil")
janela.geometry("400x300")

# aparencia de acordo com a configuração do pc
ctk.set_appearance_mode("System")
# Tema de cor: pode ser blue, green, ou dark-blue
ctk.set_default_color_theme("dark-blue")


# Nome do arquivo XLS
ARQUIVO_XLS = "base_de_dados.xlsx"


def criar_arquivo_xls():
    """Cria um arquivo XLS inicial, se não existir."""
    try:
        wb = openpyxl.load_workbook(ARQUIVO_XLS)
    except FileNotFoundError:
        wb = Workbook()
        ws = wb.active
        ws.title = "Produtos"
        ws.append(["Produto", "Valor"])
        wb.save(ARQUIVO_XLS)
        print(f"Arquivo {ARQUIVO_XLS} criado com sucesso!")


def registrar_produto(produto, valor):
    """Registra um produto e valor no arquivo XLS."""
    wb = openpyxl.load_workbook(ARQUIVO_XLS)
    ws = wb["Produtos"]
    ws.append([produto, valor])
    wb.save(ARQUIVO_XLS)
    print(f"Produto '{produto}' com valor {valor} registrado com sucesso!")


def buscar_menor_valor(produto):
    """Busca o menor valor registrado para um produto."""
    wb = openpyxl.load_workbook(ARQUIVO_XLS)
    ws = wb["Produtos"]
    # Aqui já usamos diretamente row[1], pois `values_only=True` retorna os valores das células.
    valores = [
        row[1] for row in ws.iter_rows(min_row=2, values_only=True)
        if row[0] and row[0].lower() == produto.lower()
    ]
    if valores:
        menor_valor = min(valores)
        print(f"O menor valor registrado para '{produto}' é: {menor_valor}")
    else:
        print(f"Produto '{produto}' não encontrado.")


def menu():
    """Menu principal do programa."""
    criar_arquivo_xls()
    while True:
        print("\n1. Registrar produto")
        print("2. Buscar menor valor de um produto")
        print("3. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            produto = input("Informe o nome do produto: ")
            valor = float(input("Informe o valor do produto: "))
            registrar_produto(produto, valor)
        elif opcao == "2":
            produto = input("Informe o nome do produto para buscar: ")
            buscar_menor_valor(produto)
        elif opcao == "3":
            print("Saindo do programa. Até mais!")
            break
        else:
            print("Opção inválida! Tente novamente.")

# Função para centralizar a janela
def centralizar_janela(janela, largura, altura):
    # Obtém a largura e altura da tela
    largura_tela = janela.winfo_screenwidth()
    altura_tela = janela.winfo_screenheight()

    # Calcula a posição no centro
    pos_x = int((largura_tela - largura) / 2)
    pos_y = int((altura_tela - altura) / 2)

    # Aplica a geometria para centralizar a janela
    janela.geometry(f"{largura}x{altura}+{pos_x}+{pos_y}")



 # 1 Função para Consultar Produto

def consultar_produto_gui():
    janela.withdraw()  # Oculta a janela principal
    consultar_produto = ctk.CTkToplevel()  # Cria a nova janela
    consultar_produto.title("Consultar Produto")
    consultar_produto.geometry("400x400")

    # Função para voltar para a tela principal
    def home():
        consultar_produto.destroy()  # Fecha a janela atual
        janela.deiconify()  # Reexibe a janela principal

    # Widgets na nova janela
    label_consultarProduto = ctk.CTkLabel(
        consultar_produto, text="Consulta de Produto"
    )
    label_consultarProduto.pack(pady=20)

    botao_voltar = ctk.CTkButton(
        consultar_produto, text="Inicio", command=home
    )
    botao_voltar.pack(pady=20)


# Botão para abrir a janela de consulta de produto
button_consultarProduto = ctk.CTkButton(
    janela, text="Consultar Produto", command=consultar_produto_gui
)
button_consultarProduto.pack(padx=20, pady=20)




# Iniciar o loop principal da interface
janela.mainloop()
