from classes.Vendedor import Vendedor
from classes.Produto import Produto
from classes.Venda import Venda
from classes.Dados import Dados

dados = Dados()

def cadastrarProduto():
    global dados

    result = dados.addProduto(
        Produto(
            int(input("Código: ")),
            input("Nome: "),
            float(input("Valor: R$")),
            int(input("Quantidade: "))
        )
    )
    print(dados.getInfo())
    msg = "Cadastrar novo produto? S/n: " if result else "Tentar cadastrar novamente? S/n: "
    if((input(msg)).upper() == "S"):
        cadastrarProduto()

def cadastrarVendedor():
    global dados

    result = dados.addVendedor(
        Vendedor(
            int(input("Matricula: ")),
            input("Nome: "),
            float(input("Salário: "))
        )
    )
    print(dados.getInfo())
    msg = "Cadastrar novo vendedor? S/n: " if result else "Tentar cadastrar novamente? S/n: "
    if((input(msg)).upper() == "S"):
        cadastrarVendedor()

def cadastrarVenda():
    global dados
    codigo_vendedor =   int(input("Código do Vendedor   : "))
    codigo_produto =    int(input("Código do Produto    : "))
    quantidade =        int(input("Quantidade de Produto: "))
    codigo_venda = len(dados.vendas) + 1

    v: Vendedor = dados.buscarVendedor(codigo_vendedor)
    p: Produto = dados.buscarProduto(codigo_produto)
    if v != None and p != None:
        if p.haEstoque(quantidade):
            p.atualizarEstoque(-quantidade)
            venda = Venda(codigo_venda,v,p,quantidade)
            dados.addVenda(venda)
            v.addComissao(venda.getValorVenda()*0.1)
            print("Venda realizada com sucesso!!!")
        else:
            print("Erro: ", p.getInfo())
    else:
        print("Erro: ", dados.getInfo())
    
    if (input("Cadastrar nova venda: S/n " )).upper() == "S":
        cadastrarVenda()


def exibirHistoricoVendas():
    global dados
    if len(dados.vendas) > 0:
        for venda in dados.vendas:
            print(f'ID: {venda.codig}, Vendedor: {venda.vendedor.nome}, Produto: {venda.produto.nome}, Quant x Valor: {venda.quantidade} * {venda.produto.valor} = R${venda.valor}')
    else:
        print("Não há vendas cadastradas!!!")

def exibirEstoqueDeProdutos():
    global dados
    if len(dados.produtos) > 0:
        for produto in dados.produtos:
            print(f'Código: {produto.codigo}, Nome: {produto.nome}, Valor: {produto.valor}, Quant_Est: {produto.quantidade}')
    else:
        print("Não há produtos cadastradas!!!")

def exibirListaDeVendedores():
    global dados
    if len(dados.vededores) > 0:
        for vendedor in dados.vededores:
            print(f'Matricula: {vendedor.matricula}, Nome: {vendedor.nome}, Salário + Comissão R${vendedor.salario} + {vendedor.comissao} = {vendedor.getSalarioTotal()}')
    else:
        print("Não há produtos cadastradas!!!")

exibirMenu = True
while exibirMenu:
    print("*****************************")        
    print("Cadastrar Produto         : 1")
    print("Cadastrar Vendedor        : 2")
    print("Cadastrar Venda           : 3")
    print("Exibir hitórico de vendas : 4")
    print("Exibir estoque de produtos: 5")
    print("Exibir lista de venderores: 6")
    print("Finalizar sistema         : 7")    
    print("")  
    codigo = input("Função escolhida: ")
    print("*****************************")  
    if codigo != "7":
        if codigo == "1":
            print("Funçõa em execução ->1: Cadastrar Produto         ")
            cadastrarProduto()
        elif codigo == "2":
            print("Funçõa em execução ->2: Cadastrar Vendedor        ")
            cadastrarVendedor()
        elif codigo == "3":
            print("Funçõa em execução ->3: Cadastrar Venda           ")
            cadastrarVenda()
        elif codigo == "4":
            print("Funçõa em execução ->4: Exibir hitórico de vendas ")
            exibirHistoricoVendas()
        elif codigo == "5":
            print("Funçõa em execução ->5: Exibir estoque de produtos")
            exibirEstoqueDeProdutos()
        elif codigo == "6":
            print("Funçõa em execução ->6: Exibir lista de venderores")
            exibirListaDeVendedores()
        else:
            print("Função invalida!!!")
    else:
        exibirMenu = False