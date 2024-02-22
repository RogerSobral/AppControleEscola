
class Product:

    def __init__(self, descript, price, brand):
        self.descript=descript
        self.price=price
        self.brand=brand


    def __str__(self):
        return f"Descrição: {self.descript} R$ {self.price} Marca: {self.brand}"
