import customtkinter as ctk

# Interface Gráfica

# Configuração Inicial do customTkinter
# aparencia da interface de acordo com a configuração do pc
ctk.set_appearance_mode("System")
# Tema de cor: pode ser blue, green, ou dark-blue
ctk.set_default_color_theme("dark-blue")

# Criando a janela Principal
janela = ctk.CTk()
janela.title("Mercado Facil")  # Define o titulo da Janela
janela.geometry("400x300")  # Define o tamanho da Janela



janela.mainloop()