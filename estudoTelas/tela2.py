from flet import *


class Login(UserControl):

    def build(self):
        image=Image(col={"":12,"sm":8,"md":3},src="img_login_escola_p.png")
        lineImg=ResponsiveRow(controls=[image],alignment=MainAxisAlignment.CENTER)
        iconName=Icon(col=1,name=icons.BOY)
        name=TextField(col={"":11,"sm":8,"md":6},label="Digite o seu nome")
        iconPassword=Icon(col=1,name=icons.PASSWORD)
        password=TextField(col=6,label="Digite o seu Password")
        btnEnter=ElevatedButton("Entrar",
                                style=ButtonStyle(
                                    color="#FFFFFF", #cor da fonte
                                    bgcolor={
                                        MaterialState.HOVERED:"#9367f2",
                                        MaterialState.DEFAULT:"#7b44f2"
                                    }, #     Cor de fundo
                                    shape=RoundedRectangleBorder(radius=0),

                                ),
                                width=250


                                )
        lineBtn=ResponsiveRow(controls=[btnEnter],alignment=MainAxisAlignment.CENTER)
        line1=ResponsiveRow(controls=[iconName,name],alignment=MainAxisAlignment.CENTER)
        line2=ResponsiveRow(controls=[iconPassword,password],alignment=MainAxisAlignment.CENTER)

        colLogin=Column(
            controls=[
                lineImg,
                line1,
                line2,
                lineBtn
            ],
            alignment=MainAxisAlignment.CENTER

        )

        return colLogin



def main(page:Page):
    page.title="Pagina de estudo"

    page.add(Login())
    page.update()


app(target=main)