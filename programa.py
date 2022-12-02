from tkinter import *
import tkinter as tk
from tkinter import ttk
from movimentacoes import *
import pandas as pd
from pandas import *
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import movimentacoes as fb

# Criando uma variavel para identificar a janela
root = Tk()

class Home():

    def __init__(self):
            self.root = root
            self.home_page()
            self.frames_home()
            self.botoes_home()
            self.tabela_est()

            root.mainloop()
 

    def home_page(self):
        self.root.title("CONTROLE DE ESTOQUE")
        self.root.configure(background= '#FF961E')
        self.root.geometry("1080x720")
        self.root.resizable(False, False)
        self.root.maxsize(width=1080, height=720)
        self.root.minsize(width=720, height=550)
        self.img = PhotoImage(file="imagens/programa.png")
        self.lb_imagem = Label(root, image=self.img).pack()
    
    def frames_home(self):
        self.frame1 = Frame(self.root, bg = '#BEBEBE',highlightbackground= 'black', highlightthickness=3)
        self.frame1.place(relx=0.1, rely=0.15, relwidth=0.8, relheight=0.75)


    def botoes_home(self):
        self.botao_estoque = Button(self.root, text="ESTOQUE", command=self.estoque_page)
        self.botao_estoque.place(relx = 0.40, rely=0.09, relwidth= 0.12, relheight=0.05)
        self.botao_estoque.config(font = ("Helvetica", 12))
        self.root.deiconify()
        
        self.botao_graficos = Button(self.root, text="GRÁFICOS", command= self.graficos_page)
        self.botao_graficos.place(relx = 0.55, rely=0.09, relwidth= 0.12, relheight=0.05)
        self.botao_graficos.config(font = ("Helvetica", 12))

        self.botao_alteracoes = Button(self.root, text="ALTERAÇÕES", command= self.alteracoes_page)
        self.botao_alteracoes.place(relx = 0.70, rely=0.09, relwidth= 0.12, relheight=0.05)
        self.botao_alteracoes.config(font = ("Helvetica", 12))

        self.refresh = Button(self.root, text="⟲", command=self.tabela_est)
        self.refresh.place(relx = 0.85, rely=0.09, relwidth= 0.04, relheight=0.05)
        self.refresh.config(font = ("Arial", 16))
        
    def estoque_page(self):
        self.movimentacao = tk.Toplevel()
        self.movimentacao.title("ESTOQUE")
        self.movimentacao.configure(background= '#BCEAD5')
        self.movimentacao.geometry("1080x720")
        self.movimentacao.resizable(False, False)
        self.movimentacao.maxsize(width=1220, height=880)
        self.movimentacao.minsize(width=720, height=550)


        self.frame5 = Frame(self.movimentacao, bg = '#BEBEBE',highlightbackground= 'black', highlightthickness=3)
        self.frame5.place(relx=0.25, rely=0.07, relwidth=0.7, relheight=0.85)

        self.tabela_est2()
        
        self.refresh2 = Button(self.movimentacao, text="⟲", command=self.tabela_est2)
        self.refresh2.place(relx = 0.2, rely=0.86, relwidth= 0.05, relheight=0.06)
        self.refresh2.config(font = ("Arial", 19))
        #BOTAO ADICIONAR
        self.botao_adicionar = Button(self.movimentacao, text="Adicionar Produto",command=self.adicionar_page)
        self.botao_adicionar.place(relx = 0.05, rely=0.1, relwidth= 0.12, relheight=0.04)
        self.root.deiconify()
        #BOTAO REMOVER
        self.botao_remover = Button(self.movimentacao, text="Remover", command=self.remover_page)
        self.botao_remover.place(relx = 0.05, rely=0.2, relwidth= 0.12, relheight=0.04)


        self.botao_somar = Button(self.movimentacao, text="Somar", command=self.somar_page)
        self.botao_somar.place(relx = 0.05, rely=0.3, relwidth= 0.12, relheight=0.04)

        self.botao_subtrair = Button(self.movimentacao, text="Subtrair",command=self.subtrair_page)
        self.botao_subtrair.place(relx = 0.05, rely=0.4, relwidth= 0.12, relheight=0.04)
        self.root.deiconify()
        #BOTAO VOLTAR
        self.botao_voltar = tk.Button(self.movimentacao, text= "Voltar", command=self.movimentacao.destroy)
        self.botao_voltar.place(relx = 0.02, rely=0.90, relwidth= 0.12, relheight=0.04)

        self.listaProdutos = ttk.Treeview(self.movimentacao, height=3, columns=("col1", "col2", "col3"))
        self.listaProdutos.heading("#0", text="")
        self.listaProdutos.heading("#1", text="Produto")
        self.listaProdutos.heading("#2", text="Valor")
        self.listaProdutos.heading("#3", text="Quantidade")

        self.listaProdutos.column("#0", width=1)
        self.listaProdutos.column("#1", width=100)
        self.listaProdutos.column("#2", width=50)
        self.listaProdutos.column("#3", width=50)



    def tabela_est(self):
        arquivo = pd.read_excel(arq1)
        self.estoquescroll = Scrollbar(self.frame1)
        self.estoquescroll.pack(side=RIGHT, fill=Y)
        self.style = ttk.Style()
        self.style.theme_use("default")
        self.estoque = ttk.Treeview(self.frame1, yscrollcommand=self.estoquescroll.set)
        self.estoquescroll.config(command=self.estoque.yview)
        self.estoque.delete(*self.estoque.get_children())
        self.estoque["column"] = list(arquivo.columns)
        self.estoque["show"] = "headings"

        for column in self.estoque["column"]:
            self.estoque.heading(column, text=column)
        

        arquivo_rows = arquivo.to_numpy().tolist()
        
        for row in arquivo_rows:
            self.estoque.insert("", "end", values=row)

        self.estoque.place(relx = 0.0001, rely=0.0001, relwidth= 0.968, relheight=0.9999)

    def tabela_est2(self):
        arquivo = pd.read_excel(arq1)
        self.estoquescroll = Scrollbar(self.frame5)
        self.estoquescroll.pack(side=RIGHT, fill=Y)
        self.style = ttk.Style()
        self.style.theme_use("default")
        self.estoque = ttk.Treeview(self.frame5, yscrollcommand=self.estoquescroll.set)
        self.estoquescroll.config(command=self.estoque.yview)
        self.estoque.delete(*self.estoque.get_children())
        self.estoque["column"] = list(arquivo.columns)
        self.estoque["show"] = "headings"

        for column in self.estoque["column"]:
            self.estoque.heading(column, text=column)
        

        arquivo_rows = arquivo.to_numpy().tolist()
        
        for row in arquivo_rows:
            self.estoque.insert("", "end", values=row)

        self.estoque.place(relx = 0.0001, rely=0.0001, relwidth= 0.978, relheight=0.9999)

    def tabela_hist(self):
        arquivo = pd.read_excel(arq2)
        self.historicoscroll = Scrollbar(self.frame2)
        self.historicoscroll.pack(side=RIGHT, fill=Y)
        self.style = ttk.Style()
        self.style.theme_use("default")
        self.historico = ttk.Treeview(self.frame2, yscrollcommand=self.historicoscroll.set)
        self.historicoscroll.config(command=self.historico.yview)
        self.historico.delete(*self.historico.get_children())
        self.historico["column"] = list(arquivo.columns)
        self.historico["show"] = "headings"

        for column in self.historico["column"]:
            self.historico.heading(column, text=column)
        

        arquivo_rows = arquivo.to_numpy().tolist()
        
        for row in arquivo_rows:
            self.historico.insert("", "end", values=row)

        self.historico.place(relx = 0.0001, rely=0.0001, relwidth= 0.980, relheight=0.9999)


    def adicionar_page(self):
        self.adicionar = tk.Toplevel()
        self.adicionar.title("adicionar")
        self.adicionar.configure(background= '#8EC3B0')
        self.adicionar.geometry("700x300")
        

        self.x = StringVar()
        self.y = StringVar()
        self.z = IntVar()
        self.w = IntVar()

        self.lb_produto = Label(self.adicionar, text = "Produto:",bg="#8EC3B0")
        self.lb_produto.place(relx=0.03, rely=0.2, relwidth=0.3, relheight=0.1)        
        self.entry_produto = Entry(self.adicionar, textvariable=self.x)
        self.entry_produto.place(relx=0.3, rely=0.2, relwidth=0.6, relheight=0.1)

        self.lb_descricao = Label(self.adicionar, text = "Descricao:",bg="#8EC3B0")
        self.lb_descricao.place(relx=0.03, rely=0.32, relwidth=0.3, relheight=0.1)        
        self.entry_descricao = Entry(self.adicionar, textvariable=self.y)
        self.entry_descricao.place(relx=0.3, rely=0.32, relwidth=0.6, relheight=0.1)

        self.lb_preco = Label(self.adicionar, text = "Preco:",bg="#8EC3B0")
        self.lb_preco.place(relx=0.03, rely=0.44, relwidth=0.3, relheight=0.1)        
        self.entry_lb_preco = Entry(self.adicionar, textvariable=self.z)
        self.entry_lb_preco.place(relx=0.3, rely=0.44, relwidth=0.1, relheight=0.1)
       
        self.lb_quantidade = Label(self.adicionar, text = "Quantidade:",bg="#8EC3B0")
        self.lb_quantidade.place(relx=0.03, rely=0.56, relwidth=0.3, relheight=0.1)        
        self.entry_quantidade = Entry(self.adicionar, textvariable=self.w)
        self.entry_quantidade.place(relx=0.3, rely=0.56, relwidth=0.1, relheight=0.1)

        self.botao_adicionar = tk.Button(self.adicionar, text= "Adicionar", command=lambda 
        :fb.cadastrarProduto(self.x.get(),self.y.get(),self.z.get(),self.w.get()))
        self.botao_adicionar.place(relx = 0.7, rely=0.7, relwidth= 0.2, relheight=0.2)

    
        self.botao_fechar = tk.Button(self.adicionar, text= "Fechar",bd = 0.3, command=self.adicionar.destroy)
        self.botao_fechar.place(relx = 0.05, rely=0.80, relwidth= 0.1, relheight=0.1)
        
    
    def remover_page(self):
        self.remover = tk.Toplevel()
        self.remover.title("remover")
        self.remover.configure(background= '#8EC3B0')
        self.remover.geometry("350x150")
        
        x = StringVar()
        self.lb_nome = Label(self.remover,bg="#8EC3B0", text = "ID Produto:")
        self.lb_nome.place(relx=0.1, rely=0.1, relwidth=0.3, relheight=0.22)        
        self.entry_nome = Entry(self.remover, textvariable=x)
        self.entry_nome.place(relx=0.5, rely=0.1, relwidth=0.4, relheight=0.25)
        self.botao_remover = tk.Button(self.remover, text= "Remover", 
        command= lambda :fb.removerProduto(x.get()))
        self.botao_remover.place(relx = 0.6, rely=0.5, relwidth= 0.3, relheight=0.2)
        self.botao_fechar = tk.Button(self.remover, text= "Fechar", command=self.remover.destroy)
        self.botao_fechar.place(relx = 0.08, rely=0.80, relwidth= 0.15, relheight=0.10)

    def somar_page(self):
        self.somar = tk.Toplevel()
        self.somar.title("somar")
        self.somar.configure(background= '#8EC3B0')
        self.somar.geometry("500x200")

        x = StringVar()
        y = StringVar()
        z = IntVar()
        
        self.lb_produto1 = Label(self.somar,bg="#8EC3B0", text = "Produto:")
        self.lb_produto1.place(relx=0.03, rely=0.1, relwidth=0.3, relheight=0.1)        
        self.entry_produto1 = Entry(self.somar, textvariable=x)
        self.entry_produto1.place(relx=0.3, rely=0.1, relwidth=0.6, relheight=0.1)

        self.lb_id1 = Label(self.somar,bg="#8EC3B0", text = "ID:")
        self.lb_id1.place(relx=0.03, rely=0.22, relwidth=0.3, relheight=0.1)        
        self.entry_id1 = Entry(self.somar, textvariable=y)
        self.entry_id1.place(relx=0.3, rely=0.22, relwidth=0.6, relheight=0.1)

        self.lb_quantidade1 = Label(self.somar,bg="#8EC3B0", text = "Quantidade:")
        self.lb_quantidade1.place(relx=0.03, rely=0.33, relwidth=0.3, relheight=0.1)        
        self.entry_quantidade1 = Entry(self.somar, textvariable=z)
        self.entry_quantidade1.place(relx=0.3, rely=0.33, relwidth=0.4, relheight=0.1)
             
        self.somarBotao = tk.Button(self.somar, text= "Somar", 
        command= lambda :fb.aumentarQuantidade(x.get(),y.get(),z.get()))
        self.somarBotao.place(relx = 0.6, rely=0.6, relwidth= 0.3, relheight=0.2)
        self.botao_fechar = tk.Button(self.somar, text= "Fechar", command=self.somar.destroy)
        self.botao_fechar.place(relx = 0.06, rely=0.7, relwidth= 0.15, relheight=0.10)
    
    def subtrair_page(self):
        self.subtrair = tk.Toplevel()
        self.subtrair.title("subtrair")
        self.subtrair.configure(background= '#8EC3B0')
        self.subtrair.geometry("500x200")

        x = StringVar()
        y = StringVar()
        z = IntVar()
        
        self.lb_produto2 = Label(self.subtrair,bg="#8EC3B0", text = "Produto:")
        self.lb_produto2.place(relx=0.03, rely=0.1, relwidth=0.3, relheight=0.1)        
        self.entry_produto2 = Entry(self.subtrair, textvariable=x)
        self.entry_produto2.place(relx=0.3, rely=0.1, relwidth=0.6, relheight=0.1)

        self.lb_id2 = Label(self.subtrair,bg="#8EC3B0", text = "ID:")
        self.lb_id2.place(relx=0.03, rely=0.22, relwidth=0.3, relheight=0.1)        
        self.entry_id2 = Entry(self.subtrair, textvariable=y)
        self.entry_id2.place(relx=0.3, rely=0.22, relwidth=0.6, relheight=0.1)

        self.lb_quantidade2 = Label(self.subtrair,bg="#8EC3B0", text = "Quantidade:")
        self.lb_quantidade2.place(relx=0.03, rely=0.33, relwidth=0.3, relheight=0.1)        
        self.entry_quantidade2 = Entry(self.subtrair, textvariable=z)
        self.entry_quantidade2.place(relx=0.3, rely=0.33, relwidth=0.4, relheight=0.1)
             
        self.somarBotao = tk.Button(self.subtrair,bg="#EB6440", text= "Subtrair", 
        command= lambda :fb.reduzirQuantidade(x.get(),y.get(),z.get()))
        self.somarBotao.place(relx = 0.6, rely=0.6, relwidth= 0.3, relheight=0.2)
        self.botao_fechar = tk.Button(self.subtrair, text= "Fechar", command=self.subtrair.destroy)
        self.botao_fechar.place(relx = 0.06, rely=0.7, relwidth= 0.15, relheight=0.10)


    def alteracoes_page(self):
        self.alteracoes = tk.Toplevel()
        self.alteracoes.title("Histórico de Alteração")
        self.alteracoes.configure(background= '#000000')
        self.alteracoes.geometry("960x620")
        self.alteracoes.resizable(False, False)
        self.alteracoes.maxsize(width=1220, height=880)
        self.alteracoes.minsize(width=720, height=550)

        self.frame2 = Frame(self.alteracoes, bg = '#000000', highlightbackground= 'black', highlightthickness=3)
        self.frame2.place(relx=0.05, rely=0.05, relwidth=0.90, relheight=0.90)

        self.tabela_hist()

        self.botao_voltar = tk.Button(self.alteracoes, text= "Voltar", command=self.alteracoes.destroy)
        self.botao_voltar.place(relx = 0.45, rely=0.0, relwidth= 0.10, relheight=0.05)

    def grafico_vB(self):
        figura = plt.Figure(figsize=(6,4), dpi=108)
        ax = figura.add_subplot(111)

        canva = FigureCanvasTkAgg(figura, self.frame3)
        canva.get_tk_widget().grid(row=0, column=0)

        arquivoGraf = pd.read_excel(arq3)
        arquivoGraf3 = arquivoGraf[['Produto', 'Unidades Vendidas']]
        arquivoGraf2 = arquivoGraf3.loc[(arquivoGraf3['Unidades Vendidas'] == 0)]
        arquivoGrafFinal = arquivoGraf3.drop(arquivoGraf2.index)
        plt.title("Produtos Vendidos no Mês")
        ax.bar(arquivoGrafFinal['Produto'],arquivoGrafFinal['Unidades Vendidas'])

    def grafico_vP(self):
        figura = plt.Figure(figsize=(6,4), dpi=108)
        ax = figura.add_subplot(111)

        canva = FigureCanvasTkAgg(figura, self.frame3)
        canva.get_tk_widget().grid(row=0, column=0)

        arquivoGraf = pd.read_excel(arq3)
        arquivoGraf3 = arquivoGraf[['Produto', 'Unidades Vendidas']]
        arquivoGraf2 = arquivoGraf3.loc[(arquivoGraf3['Unidades Vendidas'] == 0)]
        arquivoGrafFinal = arquivoGraf3.drop(arquivoGraf2.index)
        y = arquivoGrafFinal['Unidades Vendidas']
        mylabels = arquivoGrafFinal['Produto']
        plt.title("Produtos Vendidos no Mês")
        ax.pie(y, labels = mylabels)
        ax.legend(title = "Produtos")

    def grafico_cB(self):
        figura = plt.Figure(figsize=(6,4), dpi=108)
        ax = figura.add_subplot(111)

        canva = FigureCanvasTkAgg(figura, self.frame3)
        canva.get_tk_widget().grid(row=0, column=0)

        arquivoGraf = pd.read_excel(arq3)
        arquivoGraf3 = arquivoGraf[['Produto', 'Unidades Compradas']]
        arquivoGraf2 = arquivoGraf3.loc[(arquivoGraf3['Unidades Compradas'] == 0)]
        arquivoGrafFinal = arquivoGraf3.drop(arquivoGraf2.index)
        plt.title("Produtos Comprados no Mês")
        ax.bar(arquivoGrafFinal['Produto'],arquivoGrafFinal['Unidades Compradas'])

    def grafico_cP(self):
        figura = plt.Figure(figsize=(6,4), dpi=108)
        ax = figura.add_subplot(111)

        canva = FigureCanvasTkAgg(figura, self.frame3)
        canva.get_tk_widget().grid(row=0, column=0)

        arquivoGraf = pd.read_excel(arq3)
        arquivoGraf3 = arquivoGraf[['Produto', 'Unidades Compradas']]
        arquivoGraf2 = arquivoGraf3.loc[(arquivoGraf3['Unidades Compradas'] == 0)]
        arquivoGrafFinal = arquivoGraf3.drop(arquivoGraf2.index)
        y = arquivoGrafFinal['Unidades Compradas']
        mylabels = arquivoGrafFinal['Produto']
        plt.title("Produtos Comprados no Mês")
        ax.pie(y, labels = mylabels)
        ax.legend(title = "Produtos")

    def grafico_rB(self):
        figura = plt.Figure(figsize=(6,4), dpi=108)
        ax = figura.add_subplot(111)

        canva = FigureCanvasTkAgg(figura, self.frame3)
        canva.get_tk_widget().grid(row=0, column=0)

        arquivoGraf = pd.read_excel(arq3)
        arquivoGraf3 = arquivoGraf[['Produto', 'Receita Gerada']]
        arquivoGraf2 = arquivoGraf3.loc[(arquivoGraf3['Receita Gerada'] == 0)]
        arquivoGrafFinal = arquivoGraf3.drop(arquivoGraf2.index)
        plt.title("Receita gerada no Mês")
        ax.bar(arquivoGrafFinal['Produto'],arquivoGrafFinal['Receita Gerada'])

    def grafico_rP(self):
        figura = plt.Figure(figsize=(6,4), dpi=108)
        ax = figura.add_subplot(111)

        canva = FigureCanvasTkAgg(figura, self.frame3)
        canva.get_tk_widget().grid(row=0, column=0)

        arquivoGraf = pd.read_excel(arq3)
        arquivoGraf3 = arquivoGraf[['Produto', 'Receita Gerada']]
        arquivoGraf2 = arquivoGraf3.loc[(arquivoGraf3['Receita Gerada'] == 0)]
        arquivoGrafFinal = arquivoGraf3.drop(arquivoGraf2.index)

        y = arquivoGrafFinal['Receita Gerada']
        mylabels = arquivoGrafFinal['Produto']

        plt.title("Receita gerada no Mês")
        ax.pie(y, labels = mylabels)


    def graficos_page(self):
        self.graficos = tk.Toplevel()
        self.graficos.title("Gráficos")
        self.graficos.configure(background= '#8EC3B0')
        self.graficos.geometry("940x620")
        self.graficos.resizable(False, False)
        
        self.frame3 = Frame(self.graficos, bg = '#000000',highlightbackground= 'black', highlightthickness=3)
        self.frame3.place(relx=0.15, rely=0.17, relwidth=0.7, relheight=0.7)

        self.tipo_grafico1 = Label(self.graficos, text = "Gráfico em Barras",bg="#8EC3B0")
        self.tipo_grafico1.place(relx=0.10, rely=0.00, relwidth=0.34, relheight=0.10)
        self.tipo_grafico1.config(font = ("Helvetica", 14))

        self.tipo_grafico2 = Label(self.graficos, text = "Gráfico em Pizza",bg="#8EC3B0")
        self.tipo_grafico2.place(relx=0.56, rely=0.00, relwidth=0.34, relheight=0.10)
        self.tipo_grafico2.config(font = ("Helvetica", 14))

        self.botao_graf_Vb = tk.Button(self.graficos, text="Vendas(Unid.)", command=self.grafico_vB)
        self.botao_graf_Vb.place(relx = 0.10, rely=0.1, relwidth= 0.12, relheight=0.05)

        self.botao_graf_Cb = tk.Button(self.graficos, text="Gastos", command=self.grafico_cB)
        self.botao_graf_Cb.place(relx = 0.22, rely=0.1, relwidth= 0.12, relheight=0.05)

        self.botao_graf_Rb = tk.Button(self.graficos, text="Vendas(R$)", command=self.grafico_rB)
        self.botao_graf_Rb.place(relx = 0.34, rely=0.1, relwidth= 0.12, relheight=0.05)

        self.botao_graf_Vp = tk.Button(self.graficos, text="Vendas(Unid.)", command=self.grafico_vP)
        self.botao_graf_Vp.place(relx = 0.56, rely=0.1, relwidth= 0.12, relheight=0.05)

        self.botao_graf_Cp = tk.Button(self.graficos, text="Gastos", command=self.grafico_cP)
        self.botao_graf_Cp.place(relx = 0.68, rely=0.1, relwidth= 0.12, relheight=0.05)

        self.botao_graf_Rp = tk.Button(self.graficos, text="Vendas(R$)", command=self.grafico_rP)
        self.botao_graf_Rp.place(relx = 0.80, rely=0.1, relwidth= 0.12, relheight=0.05)






        self.botao_voltar = tk.Button(self.graficos, text= "Voltar", command=self.graficos.destroy)
        self.botao_voltar.place(relx = 0.45, rely=0.90, relwidth= 0.10, relheight=0.05)

Home()