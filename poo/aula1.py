from usuario import User
from contato import  Contato
from endereco import  Endereco
class Conta:


    n_contas=1
# public
# private  self.__<nome do atributo>
# protected self._<nome do atributo>

    def __init__(self, user:User,saldo:[int,float]=None):
        self.__user=user
        self.__n_conta=Conta.n_contas
        self.__saldo=saldo
        Conta.add_n_conta()


#getter de saldo
    @property
    def saldo(self):

        return self.__saldo

#@setter de salado
    @saldo.setter
    def saldo(self,valor):
        self.__saldo=valor

    def sacar(self,valor):
        pass

    @property
    def n_conta(self):
        return self.__n_conta


    #getters
    #Setters
    @property
    def user(self):

        return self.__user

    @user.setter
    def user(self,user):
        self.__user=user


    @classmethod
    def add_n_conta(cls):
        cls.n_contas+=1



class ContaCorrente(Conta):

    def __init__(self,user:User,saldo:[int,float]=None,limite:float=500):
        super().__init__(user,saldo)
        self.limite=limite

    def sacar(self,valor):
        if valor<=self.saldo:
            self.saldo-=valor
        else:
            pass








class ContaPoupanca(Conta):

   def sacar(self,valor):
       if valor<=self.saldo:
           self.saldo-=valor




endereco1=Endereco("José Rocha Lima", "123","Santana", "São Paulo", "SP")
contato1=Contato("1145454545","carlos@gmail.com")
usuario1=User("Carlos","345677889900",contato1,endereco1)
usuario2=User("Maria","9956889900",contato1,endereco1)
usuario3=User("Pedro","9956889900",contato1,endereco1)

cc1=ContaCorrente(saldo=5687,user=usuario3)
conta1=Conta(usuario1,10000)

print(f"Conta corrente {cc1.sacar(3)}")

print(Conta.n_contas)


conta2=Conta(usuario2,2000)

conta3=Conta(usuario2,2000)




print(conta1.n_conta)
print(conta2.n_conta)
print(conta3.n_conta)

