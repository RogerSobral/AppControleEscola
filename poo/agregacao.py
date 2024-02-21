from datetime import datetime as dt

class ShoppingCart:

    def __init__(self,data=dt.today(), cpf=None):
        self.cpf=cpf
        self.data=data
        self.__products=[]

    @property
    def products(self):
        return self.__products

    @products.setter
    def products(self, product):
        self.__products.append(product)


class Product:

    def __init__(self, descript:str, value:[float, int]=0):
        self.descript=descript
        self.value=value




if __name__ == '__main__':

    p1=Product("Rice",30.00)
    p2=Product("Beans",7.50)
    p3=Product("Meat",35.70)

    cartOne=ShoppingCart(cpf="333.333.333-67")
    cartOne.products = p1
    cartOne.products = p2
    cartOne.products = p3

    for product in cartOne.products:
        print(f"Name: {product.descript}  R$ {product.value}")
