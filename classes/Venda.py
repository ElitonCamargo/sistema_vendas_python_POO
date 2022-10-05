from classes.Vendedor import Vendedor
from classes.Produto import Produto

class Venda:
    codig: int = 0  
    vendedor: Vendedor
    produto: Produto
    quantidade: int = 0
    valor: float = 0
    __info: str = ""

    def getInfo(self):
        return self.__info

    def __init__(self, codigo: int, vendedor: Vendedor, produto: Produto, quantidade: int):
        self.codig = codigo
        self.vendedor = vendedor
        self.produto = produto
        self.quantidade = quantidade

    def getValorVenda(self):
        self.valor = self.produto.valor * self.quantidade
        return self.valor