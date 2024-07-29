import customtkinter as Ctk
from tkinter import messagebox
import bcrypt
import mysql.connector

class TelaLogin:
    def __init__(self, root):
        self.root = root
        self.top = Ctk.CTkToplevel(self.root)
        self.top.geometry("400x490")
        self.top.title("Login")

        self.login_label = Ctk.CTkLabel(self.top, text="Login", font=("OCR A Std", 40, "bold"))
        self.email_label = Ctk.CTkLabel(self.top, text="E-mail", font=("OCR A Std", 10, "bold"))
        self.email_entry = Ctk.CTkEntry(self.top)
        self.senha_label = Ctk.CTkLabel(self.top, text="Senha", font=("OCR A Std", 10, "bold"))
        self.senha_entry = Ctk.CTkEntry(self.top, show="*")
        self.login_button = Ctk.CTkButton(self.top, text="Entrar", font=("OCR A Std", 10, "bold"), command=self.verificar_login)

        self.login_label.pack(padx=10, pady=50)
        self.email_label.pack(padx=10, pady=0)
        self.email_entry.pack(padx=2, pady=2)
        self.senha_label.pack(padx=10, pady=2)
        self.senha_entry.pack(padx=10, pady=2)
        self.login_button.pack(padx=40, pady=40)

    def verificar_login(self):
        email = self.email_entry.get()
        senha = self.senha_entry.get().encode("utf-8")

        if email and senha:
            try:
                conexao = mysql.connector.connect(
                    host="127.0.0.1",
                    user="root",
                    password="",
                    database="hoteladmin"
                )
                cursor = conexao.cursor()
                comando = "SELECT senha FROM usuarios WHERE email = %s"
                valores = (email,)
                cursor.execute(comando, valores)
                resultado = cursor.fetchone()

                if resultado and bcrypt.checkpw(senha, resultado[0].encode("utf-8")):
                    messagebox.showinfo("Login bem-sucedido", "Parabéns, você se logou com sucesso!")
                else:
                    messagebox.showinfo("Erro de login", "E-mail ou senha incorretos!")
            except mysql.connector.Error as err:
                messagebox.showerror("Erro", f"Erro ao conectar ao banco de dados: {err}")
            finally:
                if conexao.is_connected():
                    cursor.close()
                    conexao.close()
        else:
            messagebox.showwarning("Atenção", "Todos os campos devem ser preenchidos!")
