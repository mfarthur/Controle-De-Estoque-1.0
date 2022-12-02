import time
import pandas as pd
import auxiliar as aux

arq1 = "estoque.xlsx"
arq2 = "historico.xlsx"
arq3 = "graficos.xlsx"

est = aux.abrirArquivo(arq1)
hist = aux.abrirArquivo(arq2)
graf = aux.abrirArquivo(arq3)

dictest = {}
dicthist = {}
dictgraf = {}
registro = {
        'João': '1908', 
        'Kezia': '1234',
        'Matheus': '0000',
        'Arthur': '4311',
        'Werlys': '5433'

    }
def login(registro): 
    v_usuario = 0
    v_senha = 0
    while v_usuario == 0 or v_senha == 0:
        id = input('Digite seu ID: ')
        v_usuario = 0
        v_senha = 0
        for nome in registro:
            if nome == id:
                v_usuario = 1
            
                senha = input('Digite a senha: ')
                if senha == registro[id]:
                    print('Login efetuado com sucesso!')            
                    return id
                else:
                    print('Login Invalido! ')
            
                break 
        if v_usuario == 0:
            print('Login Invalido!')
           
            
nome = login(registro)
titulo = "Opções:"
menu = ['1 - Mostrar estoque',
'2 - Mostrar Histórico',
'3 - Mostrar vendas do mês',
'4 - Cadastrar produto', 
'5 - Remover produto do estoque', 
'6 - Adiconar produto',
'7 - Remover do produto',
'8 - Alterar preço',
'0 - Sair do programa']

aux.avisos(est)

aux.mostrarMenu(titulo, menu)

opcao = -1
while opcao != 0:
    opcao = aux.verifyInt("Digite uma Opção: ")
    if opcao == 1:
        aux.mostrarTabela(est)
    elif opcao == 2:
        hist = aux.abrirArquivo(arq2)
        aux.mostrarTabela(hist)
    elif opcao == 3:
        graf = aux.abrirArquivo(arq3)
        aux.mostrarTabela(graf)

    elif opcao == 4:
        prod = aux.tratarString("Nome do Produto: ")
        desc = aux.tratarString("Descrição do Produto: ")
        preco = aux.verifyFloat()
        quant = aux.verifyInt()
        est = aux.cadastrarProduto(prod,desc,preco,quant)

    elif opcao == 5:
        aux.mostrarTabela(est)
        est = aux.verifyIndex(est)

    elif opcao == 6:
        aux.mostrarTabela(est)
        prod = aux.tratarString("Nome do Produto: ")
        ident = aux.tratarString("ID: ")
        quant = aux.verifyInt()
        est = aux.aumentarQuantidade(est,nome,prod,ident,quant)

    elif opcao == 7:
        aux.mostrarTabela(est)
        prod = aux.tratarString("Nome do Produto: ")
        ident = aux.tratarString("ID: ")
        quant = aux.verifyInt()
        est = aux.reduzirQuantidade(est,nome,prod,ident,quant)

    elif opcao == 8:
        aux.mostrarTabela(est)
        prod = aux.tratarString("Nome do Produto: ")
        ident = aux.tratarString("ID: ")
        preço = aux.verifyFloat()
        est = aux.alterarPreco(est,nome,prod,ident,quant)

aux.escreverArquivo(arq1, est)