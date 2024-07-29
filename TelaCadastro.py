import customtkinter as Ctk
from tkinter import messagebox
import mysql.connector
import bcrypt

class TelaCadastro:
    def __init__(self, root):
        self.root = root
        self.top = Ctk.CTkToplevel(self.root)
        self.top.geometry("400x490")
        self.top.title("Cadastro")

        self.cadastro_label = Ctk.CTkLabel(self.top, text="Cadastro", font=("OCR A Std", 40, "bold"))
        self.email_label = Ctk.CTkLabel(self.top, text="E-mail", font=("OCR A Std", 10, "bold"))
        self.email_entry = Ctk.CTkEntry(self.top)
        self.senha_label = Ctk.CTkLabel(self.top, text="Senha", font=("OCR A Std", 10, "bold"))
        self.senha_entry = Ctk.CTkEntry(self.top, show="*")
        self.cadastro_button = Ctk.CTkButton(self.top, text="Cadastrar", font=("OCR A Std", 10, "bold"), command=self.realizar_cadastro)

        self.cadastro_label.pack(padx=10, pady=50)
        self.email_label.pack(padx=10, pady=0)
        self.email_entry.pack(padx=2, pady=2)
        self.senha_label.pack(padx=10, pady=2)
        self.senha_entry.pack(padx=10, pady=2)
        self.cadastro_button.pack(padx=40, pady=40)

    def realizar_cadastro(self):
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

                comando = "SELECT email FROM usuarios WHERE email = %s"
                valores = (email,)
                cursor.execute(comando, valores)
                resultado = cursor.fetchone()

                if resultado:
                    messagebox.showwarning("Atenção", "E-mail já cadastrado!")
                else:
                    hashed_password = bcrypt.hashpw(senha, bcrypt.gensalt())
                    comando = "INSERT INTO usuarios (email, senha) VALUES (%s, %s)"
                    valores = (email, hashed_password)
                    cursor.execute(comando, valores)
                    conexao.commit()
                    messagebox.showinfo("Cadastro bem-sucedido", "Cadastro realizado com sucesso!")
                    self.top.destroy()
                    self.root.deiconify()
            except mysql.connector.Error as err:
                messagebox.showerror("Erro", f"Erro ao conectar ao banco de dados: {err}")
            finally:
                if conexao.is_connected():
                    cursor.close()
                    conexao.close()
        else:
            messagebox.showwarning("Atenção", "Todos os campos devem ser preenchidos!")
