from flet import *


def main(page:Page):
    page.title="Login"
    page.window_width=450
    page.window_max_width=450
    page.window_min_width=450
    page.window_center()
    page.horizontal_alignment=MainAxisAlignment.CENTER

    img_logo=Image(src="img_login.png")
    input_login=TextField(label="Login")
    input_password=TextField(label="Password")
    btn_enter= ElevatedButton(text="Entrar")
    icon_google=IconButton(icon=icons.GITE)
    icon_gitHup = IconButton(icon=icons.ADD)
    line1=Row(controls=[img_logo], alignment=MainAxisAlignment.CENTER)
    line2=Row(controls=[input_login],alignment=MainAxisAlignment.CENTER)
    line3=Row(controls=[input_password],alignment=MainAxisAlignment.CENTER)
    line4=Row(controls=[btn_enter],alignment=MainAxisAlignment.CENTER)
    line5=Row(controls=[icon_google,icon_gitHup],alignment=MainAxisAlignment.SPACE_AROUND)
    coluna=Column(controls=[line1,
                            line2,
                            line3,
                            line4,
                            line5],

                  alignment=MainAxisAlignment.CENTER)
    page.add(coluna)
    page.update()



app(target=main)