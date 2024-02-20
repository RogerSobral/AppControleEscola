# _*_ econding: utf-8 _*_

# Associação
# A associação entre dois objetos ocorre quando
# eles são completamente independentes entre si
# mas eventualmente estão relacionados.
# Ela pode ser considerada uma relação de muitos para muitos.
# Não há propriedade (ownership) nem dependência entre eles.
# A relação é eventual.

class Escritor:
  def __init__(self, nome):
      self.__nome=nome
      self.__ferramenta=None

  #Criando um getter
  @property
  def nome(self):
    return self.__nome


  @property
  def ferramenta(self):
    return self.__ferramenta

  @ferramenta.setter
  def ferramenta(self, equipamento):
    self.__ferramenta=equipamento



class Caneta:

  def __init__(self, marca):
    self.__marca=marca

  @property
  def marca(self):
    return self.__marca

  def escrever(self):
    print("A caneta esta escrevendo")


class Maquina:
  def escrever(self):
    print("A maquina esta escrevendo")


# Agregação

# O tipo de associação agregação pode ser classificada basicamente
# de duas formas: agregação de composição e agregação compartilhada
# (ou reflexiva).

# Agregações Esses tipos de relações são chamados assim
# porque agregam valor para o objeto relacionado.
# Esse é um tipo especializado de associação que nos permite encarar a relação entre os objetos como: Todo/Parte.

# Todo  Parte significa que um dos lados da associação (um classe)
# é chamado de Todo e o outro lado é chamado de Parte,
#  já que a parte nos permite pensar que: A Parte está contida no Todo.

# Agregação (ou agregação compartilhada)
# Essa também é uma relação todo parte, porém,
#  nesse caso dizemos que a parte é compartilhada por outros
#  (por isso agregação compartilhada).
#  Isso significa que a parte de um tipo A está contida em um tipo B,
#  quando esse tem relação de agregação entre eles, porém,
#  essa mesma parte A não existe somente para compor B,
#  essa parte pode agregar outros tipos.





if __name__ == '__main__':

    escritor = Escritor("Carlos")
    caneta = Caneta("Castell")
    maquina = Maquina()

    escritor.ferramenta=caneta
    print(escritor.ferramenta)

    escritor.ferramenta=maquina
    escritor.ferramenta.escrever()
