import customtkinter as Ctk
from TelaLogin import TelaLogin
from TelaCadastro import TelaCadastro

class TelaPrincipal:
    def __init__(self, root):
        self.root = root
        self.root.geometry("400x490")
        self.root.title("Menu Principal")

        self.menu_label = Ctk.CTkLabel(self.root, text="Menu Principal", font=("OCR A Std", 40, "bold"))
        self.botao_ncd = Ctk.CTkButton(self.root, text="Novo Cadastro", command=self.abrir_cadastro)
        self.botao_jcd = Ctk.CTkButton(self.root, text="Já tenho cadastro", command=self.abrir_login)

        self.menu_label.pack(padx=10, pady=10)
        self.botao_ncd.pack(padx=120, pady=10)
        self.botao_jcd.pack(padx=10, pady=10)

    def abrir_login(self):
        self.root.withdraw()  # Esconde a tela principal
        TelaLogin(self.root)  # Abre a tela de login

    def abrir_cadastro(self):
        self.root.withdraw()  # Esconde a tela principal
        TelaCadastro(self.root)  # Abre a tela de cadastro

if __name__ == "__main__":
    Ctk.set_appearance_mode("dark")
    root = Ctk.CTk()
    TelaPrincipal(root)
    root.mainloop()
