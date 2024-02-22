
from cliente import Customer
class ShoppingCart:

    def __init__(self,customer:Customer=None):
        self.customer=customer
        self.listProducts=[]


    def addProduct(self,product):
        self.listProducts.append(product)