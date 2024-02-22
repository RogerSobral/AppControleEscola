from flet import *
from cliente import Customer
from produto import Product
from carrinhoCompras import ShoppingCart
class ViewRegisterProduct(UserControl):

    def __init__(self):
        super().__init__()
        self.cart=ShoppingCart()

    def build(self):

        # functions
        def registerCustomer(e):
            c1=Customer(name.value,cpf.value)
            response.value=str(c1)
            response.update()


        def registerProduct(e):
            p1=Product(brand=brand.value,descript=descript.value,price=price.value)
            self.cart.addProduct(p1)

            for prod in self.cart.listProducts:
                responseProduct.value=prod
                responseProduct.update()



        # customer
        title1=Text("Cadastro de Cliente")
        name=TextField(col={"":12,"sm":6},label="Nome")
        cpf=TextField(col={"":12,"sm":6},label="CPF")
        lineCustomer = ResponsiveRow(controls=[
            name,
            cpf,
        ])
        btnRegisterCustomer=ElevatedButton(text="Cadastrar Cliente",on_click=registerCustomer)
        response=Text()

        # Register Product
        title2=Text("Cadastro de produtos")
        descript=TextField(col={"":12,"sm":4, "md":3},label="Descrição do Produto")
        price=TextField(col={"":6,"sm":3}, label="Valor",prefix_text="R$")
        brand = TextField(col={"": 6, "sm": 3}, label="Marca")
        lineProducts=ResponsiveRow(controls=[
            descript,
            price,
            brand
        ])

        btnRegisterProducts = ElevatedButton(text="Cadastrar Produto", on_click=registerProduct)

        responseProduct=Text()

        return Column(controls=[
           title1,
           lineCustomer,
           btnRegisterCustomer,
           response,
           title2,
           lineProducts,
           btnRegisterProducts,
           responseProduct
        ])

def main(page:Page):
    # set up my page
    page.title="Cadastrar Produto"
    page.horizontal_alignment="center"

    page.window_center()

    # set up of views
    viewRegisterProd=ViewRegisterProduct()

    page.add(viewRegisterProd)

#hot reload
    page.update()


if __name__ == '__main__':
    app(target=main)