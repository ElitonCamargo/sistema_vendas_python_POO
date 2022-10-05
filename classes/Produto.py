class Produto:
    codigo: int = 0
    nome: str = ""
    valor: float = 0.00
    quantidade: float = 0
    __info: str = ""

    def __init__(self,codigo: int, nome: str, valor: float, quantidade: int):
        self.codigo = codigo
        self.nome = nome
        self.valor= valor
        self.quantidade = quantidade

    def validarCadastro(self):
        if len(self.nome) < 3:
            self.__info = "Nome inválido"
        elif self.valor <= 0.00:
            self.__info = "Valor inválido"
        elif self.quantidade < 1:
            self.__info = "Quantidade inválida"
        else:
            return True
        return False
    
    def atualizarEstoque(self, quant: int):
        self.quantidade += quant
    
    def haEstoque(self, quant: int):
        if (self.quantidade >= quant):            
            return True
        else:
            self.__info = "Estoque insuficiente"
            return False

    def getInfo(self):
        return self.__info