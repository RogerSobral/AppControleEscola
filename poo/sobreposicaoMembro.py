from abc import ABC,abstractmethod

class Pessoa(ABC):
    def __init__(self, nome, cpf):
        self.nome=nome
        self.cpf=cpf

    @abstractmethod
    def punchTheClock(self,hour):pass


class Funcionario(Pessoa):

    def __init__(self,nome, cpf, registro):
        super().__init__(nome, cpf)
        self.registro=registro
        self.hora=None


class Gerente(Funcionario):
    def __init__(self,nome, cpf, registro, setor):
        super().__init__(nome, cpf, registro)
        self.setor = setor

    def punchTheClock(self,hour):
        self.hora=hour

    def __str__(self):
        return f"Nome: {self.nome} Registro: {self.registro} Setor: {self.setor}"


    def __float__(self):
        return 123.67

    def __eq__(self, other):
        return  self.nome== other.nome and self.registro== other.registro

    def __le__(self, other):
        return self.nome<=other.nome


if __name__ == '__main__':

    g1=Gerente("Pedro","232323232323","ar002","Compras")
    g2=Gerente("Aedro","232323232323","a002","Compras")

    print(g1<=g2)