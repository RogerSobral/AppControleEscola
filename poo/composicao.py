
# Composição = ela é dona objeto,
# sendo assim vamos instanciar uma classe dentro da outra
# Associação - Usa
# Agregação - Tem
# Composição - é Dono
# Herença - É

class Contato:
    def __init__(self,telefone=None, email=None):
        self.__telefone = telefone
        self.__email = email

    @property
    def telefone(self):
        return self.telefone

    @telefone.setter
    def telefone(self, telefone):
        self.__telefone = telefone

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email):
        self.__email=email

class Pessoa:

    def __init__(self, nome, cpf):
        self.nome=nome
        self.cpf=cpf
        self.contato=Contato()

    def addContato(self,telefone=None, email=None):
        self.contato.telefone=telefone
        self.contato.email=email


if __name__ == '__main__':
    p1=Pessoa("Carlos","232.232.333-67")
    p1.addContato("1145454545",email="carlos@gmail.com")