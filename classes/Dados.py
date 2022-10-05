from typing import List
from classes.Vendedor import Vendedor
from classes.Produto import Produto
from classes.Venda import Venda


class Dados:
    vededores: List[Vendedor]  = []
    produtos: List[Produto] = []
    vendas: List[Venda] = []
    __info: str = ""

    def addVenda(self, venda: Venda):
        self.vendas.append(venda)

    def addVendedor(self, vendedor: Vendedor):
        if vendedor.validarCadastro():
            if self.buscarVendedor(vendedor.matricula) == None:
                self.vededores.append(vendedor)
                self.__info = "Vendedor cadastrado com sucesso"
                return True
            else:
                self.__info = "Vendedor já cadastrado"
        else:
            self.__info = vendedor.getInfo()
        return False
    
    def buscarVendedor(self, matricula: int):
        for vendedor in self.vededores:
            if vendedor.matricula == matricula:
                return vendedor
        self.__info = "Vendedor não encotrado"
        return None

    def addProduto(self, produto: Produto):
        if produto.validarCadastro():            
            if self.buscarProduto(produto.codigo) == None:
                self.produtos.append(produto)
                self.__info = "Produto cadastrado com sucesso"
                return True
            else:
                self.__info = "Produto já cadastrado"
        else:
            self.__info = produto.getInfo()
        return False
    
    def buscarProduto(self, codigo: int):
        for produto in self.produtos:            
            if produto.codigo == codigo:
                return produto
        self.__info = "Produto não encotrado"
        return None

    def getInfo(self):
        return self.__info