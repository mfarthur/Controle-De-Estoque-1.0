from tkinter import ttk
from tkinter import *
from tkinter import messagebox
import tkinter as tk
import DataBaser


root = Tk()

class Home():

    def __init__(self):
            self.root = root
            self.home_page()
            self.register_page

            root.mainloop()

    def home_page(self):
        self.root.title("CONTROLE DE ESTOQUE")
        self.root.configure(background= 'white')
        self.root.geometry("900x500")
        self.root.resizable(False, False)
        self.img = PhotoImage(file="imagens/Login.png")
        self.lb_imagem = Label(root, image=self.img).pack()
        
        # ============= LOGIN_PAGE ==================
        self.userLabel = Label(self.root, text="Usuário:", font=("Nasalization", 12),bg="white")
        self.userLabel.place(x=440, y=160) 
        self.userEntry = ttk.Entry(self.root, width=40)
        self.userEntry.place(x=510, y=160)

        self.passLabel = Label(self.root, text="Senha:",font=("Nasalization", 12), bg="white")
        self.passLabel.place(x=440, y=210) 
        self.passEntry = ttk.Entry(self.root, width=40, show="*")
        self.passEntry.place(x=510, y=210)

        self.loginButton = ttk.Button(self.root, text="Login", width=10, command=self.Login)
        self.loginButton.place(x=740, y=300)

        self.registerButton = ttk.Button(self.root, text="Cadastrar",width=10, command=self.register_page)
        self.registerButton.place(x=140, y=250) 

        # ============ REGISTER_PAGE ================

    def register_page(self):

        self.loginButton.place(x=5000)
        self.registerButton.place(x=5000)

        self.nomeLabel = Label(self.root, text="Nome", font=("Nasalization",12))
        self.nomeLabel.place(x=440, y=80)
        self.nomeEntry = ttk.Entry(self.root, width=40)
        self.nomeEntry.place(x=510, y=80)

        self.emailLabel = Label(self.root, text="Email", font=("Nasalization",12))
        self.emailLabel.place(x=440, y=120)
        self.emailEntry = ttk.Entry(self.root, width=40)
        self.emailEntry.place(x=510, y=120)
    

        self.registerButton2 = ttk.Button(self.root, text="Cadastrar", width=10, command=self.registrarDB)
        self.registerButton2.place(x=750, y=300)
        
        self.voltarButton = ttk.Button(self.root, text="Voltar", width=10, command=self.voltar_login)
        self.voltarButton.place(x=750, y=450)


    def registrarDB(self):
        self.Name = self.nomeEntry.get()
        self.Email = self.emailEntry.get()
        self.User = self.userEntry.get()
        self.Pass = self.passEntry.get()

        if( self.Name == "" and self.Email == "" and self.User == "" and self.Pass== ""):
            messagebox.showerror(title="Register Error", message="Preencha Todos os Campos")
        else:
            DataBaser.cursor.execute("""
            INSERT INTO Users(Name, Email, User, Password) VALUES(?,?,?,?)
            """,(self.Name, self.Email, self.User, self.Pass))
            DataBaser.conn.commit()
            messagebox.showinfo(title="Register Info", message="Conta Criada Com Sucesso")
    
    def Login(self):
        User = self.userEntry.get()
        Pass = self.passEntry.get()
        
        DataBaser.cursor.execute("""
            SELECT * FROM Users
            WHERE (User = ? and Password = ?)
        """, (User, Pass) )
        VerifyLogin = DataBaser.cursor.fetchone()
        try:
            if (User in VerifyLogin and Pass in VerifyLogin):
                root.destroy()
                import programa
        except: 
            print('erro')


    def voltar_login(self):
        self.nomeLabel.place(x=5000)
        self.nomeEntry.place(x=5000)
        self.emailEntry.place(x=5000)
        self.emailLabel.place(x=5000)
        self.registerButton2.place(x=5000)
        self.voltarButton.place(x=5000)

        self.loginButton.place(x=740)
        self.registerButton.place(x=140)


Home()