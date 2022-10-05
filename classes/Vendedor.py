class Vendedor:
    matricula: int = 0
    nome: str = ""
    salario: float = 0.00
    comissao: float = 0.00
    __info: str = ""

    def getInfo(self):
        return self.__info

    def __init__(self, matricula:int, nome: str , salario: float):
        self.matricula = matricula
        self.nome = nome
        self.salario = salario

    def addComissao(self, valor: float):
        self.comissao += valor

    def getSalarioTotal(self):
        return self.comissao + self.salario

    def validarCadastro(self):
        if len(self.nome) < 3:
            self.__info = "Nome inválido"
        elif self.salario < 1000.00:
            self.__info = "Salário inválido"       
        else:
            return True
        return False
        

